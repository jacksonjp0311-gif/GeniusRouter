from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Literal


Tier = Literal["low", "medium", "high", "unknown"]


VALID_TIERS = {"low", "medium", "high", "unknown"}


@dataclass
class RoutingDecision:
    schema: str
    request_id: str
    timestamp: str
    semantic_tier: str
    classifier_tier: str
    final_tier: str
    selected_model: str
    provider: str
    cache_enabled: bool
    cache_hit: bool
    cache_key: str
    fallback_used: bool
    fallback_reason: str | None
    latency_ms: float | None
    claim_boundary: str = "routing decision evidence, not proof of optimal routing"

    def validate(self) -> None:
        for field_name in ("semantic_tier", "classifier_tier", "final_tier"):
            value = getattr(self, field_name)
            if value not in VALID_TIERS:
                raise ValueError(f"Invalid {field_name}: {value}")
        if self.final_tier == "unknown":
            raise ValueError("final_tier must resolve to low, medium, or high")
        if not self.schema:
            raise ValueError("schema is required")
        if not self.request_id:
            raise ValueError("request_id is required")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)