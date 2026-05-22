from __future__ import annotations

from typing import Any


async def call_model(model: str, messages: list[dict[str, Any]], extra: dict[str, Any]) -> dict[str, Any]:
    import litellm

    response = await litellm.acompletion(
        model=model,
        messages=messages,
        **extra,
    )
    if hasattr(response, "model_dump"):
        return response.model_dump()
    return dict(response)