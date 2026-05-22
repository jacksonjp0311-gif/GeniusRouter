from __future__ import annotations

from typing import Any

from .config import GeniusRouterConfig


TIER_RANK = {"unknown": 0, "low": 1, "medium": 2, "high": 3}
RANK_TIER = {value: key for key, value in TIER_RANK.items()}


LOW_TERMS = {
    "hello", "hi", "simple", "quick", "translate", "summarize", "summary",
    "rewrite", "format", "basic", "list"
}

MEDIUM_TERMS = {
    "explain", "code", "function", "compare", "debug", "fix", "draft",
    "implement", "test", "api"
}

HIGH_TERMS = {
    "architecture", "strategy", "multi-step", "reason", "analyze", "design",
    "research", "optimize", "prove", "security", "system", "roadmap"
}


def normalize_tier(value: str | None) -> str:
    if not value:
        return "unknown"
    tier = str(value).strip().lower()
    if tier in {"low", "medium", "high"}:
        return tier
    if "high" in tier:
        return "high"
    if "medium" in tier:
        return "medium"
    if "low" in tier:
        return "low"
    return "unknown"


def extract_prompt(messages: list[dict[str, Any]]) -> str:
    parts: list[str] = []
    for message in messages:
        content = message.get("content", "")
        if isinstance(content, str):
            parts.append(content)
        if isinstance(content, list):
            for item in content:
                if isinstance(item, dict) and isinstance(item.get("text"), str):
                    parts.append(item["text"])
    return " ".join(part.strip() for part in parts if part and part.strip()).strip()


def semantic_route(prompt: str) -> str:
    text = prompt.lower()
    high_hits = sum(1 for term in HIGH_TERMS if term in text)
    medium_hits = sum(1 for term in MEDIUM_TERMS if term in text)
    low_hits = sum(1 for term in LOW_TERMS if term in text)

    if high_hits:
        return "high"
    if medium_hits:
        return "medium"
    if low_hits:
        return "low"
    return "medium"


def merge_tiers(semantic_tier: str, classifier_tier: str) -> str:
    semantic = normalize_tier(semantic_tier)
    classifier = normalize_tier(classifier_tier)

    if semantic == classifier and semantic != "unknown":
        return semantic

    if classifier == "high" or semantic == "high":
        return "high"

    if classifier == "medium" or semantic == "medium":
        return "medium"

    if classifier == "low" and semantic == "low":
        return "low"

    return "medium"


def get_model_for_tier(config: GeniusRouterConfig, tier: str) -> tuple[str, str]:
    final_tier = normalize_tier(tier)
    if final_tier == "unknown":
        final_tier = "medium"

    model = {
        "low": config.routing.low_iq,
        "medium": config.routing.medium_iq,
        "high": config.routing.high_iq,
    }[final_tier]

    if model.startswith("ollama/"):
        provider = "ollama"
    elif model.startswith("openrouter/"):
        provider = "openrouter"
    elif model.startswith("openai/"):
        provider = "openai"
    elif model.startswith("anthropic/"):
        provider = "anthropic"
    else:
        provider = "custom"

    return model, provider