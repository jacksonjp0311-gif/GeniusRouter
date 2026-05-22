from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from geniusrouter.main import app


def run_smoke_validation() -> dict:
    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)
        os.environ["GENIUSROUTER_ARTIFACT_ROOT"] = str(temp)
        os.environ["GENIUSROUTER_DEBUG_ROUTING"] = "true"

        response_payload = {
            "id": "chatcmpl-smoke",
            "object": "chat.completion",
            "choices": [
                {
                    "index": 0,
                    "message": {"role": "assistant", "content": "smoke-ok"},
                    "finish_reason": "stop",
                }
            ],
            "model": "mocked-provider",
        }

        with patch("geniusrouter.main.classify_iq", new=AsyncMock(return_value="medium")):
            with patch("geniusrouter.main.call_model", new=AsyncMock(return_value=response_payload)):
                client = TestClient(app)

                health = client.get("/health")
                chat = client.post(
                    "/v1/chat/completions",
                    json={
                        "model": "geniusrouter/auto",
                        "messages": [
                            {
                                "role": "user",
                                "content": "Design a simple routing test architecture.",
                            }
                        ],
                    },
                )

        routing_log = temp / "artifacts" / "routing_decisions" / "routing_decisions.jsonl"
        routing_records = []
        if routing_log.exists():
            routing_records = [
                json.loads(line)
                for line in routing_log.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]

        report = {
            "schema": "GeniusRouter-SA-v0.3-smoke-validation-report",
            "status": "pass" if health.status_code == 200 and chat.status_code == 200 and routing_records else "fail",
            "health_status_code": health.status_code,
            "chat_status_code": chat.status_code,
            "routing_records": len(routing_records),
            "routing_record_schema": routing_records[0].get("schema") if routing_records else None,
            "final_tier": routing_records[0].get("final_tier") if routing_records else None,
            "selected_model": routing_records[0].get("selected_model") if routing_records else None,
            "provider": routing_records[0].get("provider") if routing_records else None,
            "debug_routing_metadata_present": "_geniusrouter" in chat.json() if chat.status_code == 200 else False,
            "claim_boundary": "Smoke validation checks local endpoint and routing-record emission with mocked provider. It does not prove routing quality, provider reliability, cost savings, production readiness, or benchmark validity.",
        }

        if report["status"] != "pass":
            raise SystemExit(json.dumps(report, indent=2))

        return report


def main() -> None:
    report = run_smoke_validation()
    out_dir = Path("reports") / "smoke"
    out_dir.mkdir(parents=True, exist_ok=True)
    latest = out_dir / "latest_smoke_validation_report.json"
    latest.write_text(json.dumps(report, indent=2), encoding="utf-8")

    md = out_dir / "latest_smoke_validation_report.md"
    md.write_text(
        "# GeniusRouter-SA v0.3 Smoke Validation Report\n\n"
        f"- Status: {report['status']}\n"
        f"- Health status code: {report['health_status_code']}\n"
        f"- Chat status code: {report['chat_status_code']}\n"
        f"- Routing records emitted: {report['routing_records']}\n"
        f"- Routing schema: {report['routing_record_schema']}\n"
        f"- Final tier: {report['final_tier']}\n"
        f"- Selected model: {report['selected_model']}\n"
        f"- Provider: {report['provider']}\n"
        f"- Debug routing metadata present: {report['debug_routing_metadata_present']}\n\n"
        f"Boundary: {report['claim_boundary']}\n",
        encoding="utf-8",
    )

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()