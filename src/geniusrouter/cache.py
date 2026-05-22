from __future__ import annotations

import hashlib
import json
from typing import Any


def stable_cache_key(messages: list[dict[str, Any]], selected_model: str, config_version: str = "GeniusRouter-SA-v0.2") -> str:
    payload = {
        "messages": messages,
        "selected_model": selected_model,
        "config_version": config_version,
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


class NullCache:
    enabled = False

    async def get(self, key: str):
        return None

    async def setex(self, key: str, ttl: int, value: str):
        return None