from __future__ import annotations

import json
import os
import time
import uuid
from datetime import datetime, timezone
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .cache import NullCache, stable_cache_key
from .config import ConfigError, load_config
from .providers import call_model
from .routing import extract_prompt, get_model_for_tier, merge_tiers, semantic_route
from .schemas import RoutingDecision
from .telemetry import append_routing_decision

load_dotenv()

app = FastAPI(title="GeniusRouter - 3-Tier LLM Router", version="0.2.0")


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_runtime_config():
    config_path = os.getenv("GENIUSROUTER_CONFIG", "config.yaml")
    return load_config(config_path)


async def classify_iq(prompt: str, config) -> str:
    if not config.classifier.enabled:
        return "medium"
    try:
        import ollama

        resp = ollama.chat(
            model=config.classifier.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Classify exactly: LOW | MEDIUM | HIGH\nPrompt: {prompt[:500]}",
                }
            ],
        )
        tier = resp.get("message", {}).get("content", "").strip().lower()
        if tier in {"low", "medium", "high"}:
            return tier
        return "medium"
    except Exception:
        return "medium"


async def get_cache_client(config):
    if not config.cache.enabled:
        return NullCache()
    try:
        import redis.asyncio as redis

        redis_url = os.getenv("REDIS_URL")
        if not redis_url:
            return NullCache()
        return redis.from_url(redis_url)
    except Exception:
        return NullCache()


@app.get("/health")
async def health():
    try:
        config = _load_runtime_config()
        return {
            "status": "healthy",
            "router": "GeniusRouter",
            "version": "0.2.0",
            "architecture_layer": "GeniusRouter-SA v0.2",
            "config_loaded": True,
            "cache_enabled": config.cache.enabled,
            "classifier_enabled": config.classifier.enabled,
            "providers_configured": {
                "low": bool(config.routing.low_iq),
                "medium": bool(config.routing.medium_iq),
                "high": bool(config.routing.high_iq),
            },
            "claim_boundary": "health status is runtime configuration evidence, not production-readiness proof",
        }
    except ConfigError as exc:
        return JSONResponse(
            status_code=500,
            content={
                "status": "unhealthy",
                "router": "GeniusRouter",
                "config_loaded": False,
                "error": str(exc),
            },
        )


@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    started = time.perf_counter()
    request_id = str(uuid.uuid4())
    cache_hit = False
    fallback_used = False
    fallback_reason = None

    try:
        config = _load_runtime_config()
    except ConfigError as exc:
        return JSONResponse(status_code=500, content={"error": "invalid_config", "detail": str(exc)})

    body = await request.json()
    messages = body.get("messages", [])
    if not isinstance(messages, list):
        return JSONResponse(status_code=400, content={"error": "messages must be a list"})

    prompt = extract_prompt(messages)
    semantic_tier = semantic_route(prompt)
    classifier_tier = await classify_iq(prompt, config)
    final_tier = merge_tiers(semantic_tier, classifier_tier)
    selected_model, provider = get_model_for_tier(config, final_tier)

    key = stable_cache_key(messages, selected_model, config.config_version)
    cache = await get_cache_client(config)

    if config.cache.enabled:
        try:
            cached = await cache.get(key)
            if cached:
                cache_hit = True
                if isinstance(cached, bytes):
                    cached = cached.decode("utf-8")
                return JSONResponse(content=json.loads(cached))
        except Exception as exc:
            fallback_used = True
            fallback_reason = f"cache_get_failed:{type(exc).__name__}"

    extra = {k: v for k, v in body.items() if k not in {"model", "messages"}}

    try:
        result = await call_model(selected_model, messages, extra)
    except Exception as exc:
        fallback_used = True
        fallback_reason = f"provider_failed:{type(exc).__name__}"
        result = {
            "error": "provider_call_failed",
            "detail": str(exc),
            "model": selected_model,
            "tier": final_tier,
        }

    latency_ms = round((time.perf_counter() - started) * 1000.0, 3)

    decision = RoutingDecision(
        schema="GeniusRouter-SA-v0.2-routing-decision",
        request_id=request_id,
        timestamp=_utc_now(),
        semantic_tier=semantic_tier,
        classifier_tier=classifier_tier,
        final_tier=final_tier,
        selected_model=selected_model,
        provider=provider,
        cache_enabled=config.cache.enabled,
        cache_hit=cache_hit,
        cache_key=key,
        fallback_used=fallback_used,
        fallback_reason=fallback_reason,
        latency_ms=latency_ms,
    ).to_dict()

    append_routing_decision(decision)

    if config.cache.enabled and not cache_hit and "error" not in result:
        try:
            await cache.setex(key, config.cache.ttl_seconds, json.dumps(result))
        except Exception:
            pass

    return JSONResponse(content=result)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)