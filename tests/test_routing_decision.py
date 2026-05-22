import unittest

from geniusrouter.schemas import RoutingDecision


class TestRoutingDecision(unittest.TestCase):
    def test_decision_validates_and_serializes(self):
        decision = RoutingDecision(
            schema="GeniusRouter-SA-v0.2-routing-decision",
            request_id="abc",
            timestamp="2026-05-22T00:00:00Z",
            semantic_tier="low",
            classifier_tier="medium",
            final_tier="medium",
            selected_model="ollama/medium",
            provider="ollama",
            cache_enabled=True,
            cache_hit=False,
            cache_key="x" * 64,
            fallback_used=False,
            fallback_reason=None,
            latency_ms=1.2,
        )
        data = decision.to_dict()
        self.assertEqual(data["final_tier"], "medium")

    def test_unknown_final_tier_fails(self):
        decision = RoutingDecision(
            schema="GeniusRouter-SA-v0.2-routing-decision",
            request_id="abc",
            timestamp="now",
            semantic_tier="unknown",
            classifier_tier="unknown",
            final_tier="unknown",
            selected_model="",
            provider="",
            cache_enabled=False,
            cache_hit=False,
            cache_key="",
            fallback_used=False,
            fallback_reason=None,
            latency_ms=None,
        )
        with self.assertRaises(ValueError):
            decision.to_dict()


if __name__ == "__main__":
    unittest.main()