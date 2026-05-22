from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def append_routing_decision(decision: dict[str, Any], root: str | Path = ".") -> Path:
    base = Path(root) / "artifacts" / "routing_decisions"
    base.mkdir(parents=True, exist_ok=True)
    path = base / "routing_decisions.jsonl"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(decision, sort_keys=True) + "\n")
    return path