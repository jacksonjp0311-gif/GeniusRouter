import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from geniusrouter.main import app


class TestGeniusRouterV03SmokeValidation(unittest.TestCase):
    def test_health_endpoint_smoke(self):
        client = TestClient(app)
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["router"], "GeniusRouter")
        self.assertEqual(body["architecture_layer"], "GeniusRouter-SA v0.2")
        self.assertIn("claim_boundary", body)

    def test_chat_endpoint_emits_routing_decision_with_mocked_provider(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            os.environ["GENIUSROUTER_ARTIFACT_ROOT"] = temp_dir
            os.environ["GENIUSROUTER_DEBUG_ROUTING"] = "true"

            response_payload = {
                "id": "chatcmpl-test",
                "object": "chat.completion",
                "choices": [
                    {
                        "index": 0,
                        "message": {"role": "assistant", "content": "ok"},
                        "finish_reason": "stop",
                    }
                ],
                "model": "mocked-provider",
            }

            with patch("geniusrouter.main.classify_iq", new=AsyncMock(return_value="medium")):
                with patch("geniusrouter.main.call_model", new=AsyncMock(return_value=response_payload)):
                    client = TestClient(app)
                    response = client.post(
                        "/v1/chat/completions",
                        json={
                            "model": "geniusrouter/auto",
                            "messages": [
                                {
                                    "role": "user",
                                    "content": "Design a routing architecture test.",
                                }
                            ],
                        },
                    )

            self.assertEqual(response.status_code, 200)
            body = response.json()
            self.assertIn("_geniusrouter", body)
            decision = body["_geniusrouter"]["routing_decision"]
            self.assertEqual(decision["schema"], "GeniusRouter-SA-v0.2-routing-decision")
            self.assertEqual(decision["final_tier"], "high")
            self.assertEqual(decision["provider"], "openrouter")

            log_path = Path(temp_dir) / "artifacts" / "routing_decisions" / "routing_decisions.jsonl"
            self.assertTrue(log_path.exists())
            records = [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines()]
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0]["request_id"], decision["request_id"])

    def test_v03_smoke_runner_exists(self):
        path = Path(__file__).resolve().parents[1] / "scripts" / "release" / "run_smoke_validation_v0_3.py"
        self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()