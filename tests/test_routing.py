import unittest

from geniusrouter.routing import extract_prompt, merge_tiers, semantic_route


class TestRouting(unittest.TestCase):
    def test_extract_prompt_from_messages(self):
        messages = [
            {"role": "system", "content": "You are helpful."},
            {"role": "user", "content": "Design an architecture."},
        ]
        self.assertIn("Design an architecture", extract_prompt(messages))

    def test_semantic_route_high(self):
        self.assertEqual(semantic_route("Design a multi-step architecture strategy"), "high")

    def test_semantic_route_low(self):
        self.assertEqual(semantic_route("hello quick summary"), "low")

    def test_merge_prevents_under_routing(self):
        self.assertEqual(merge_tiers("high", "medium"), "high")
        self.assertEqual(merge_tiers("low", "medium"), "medium")
        self.assertEqual(merge_tiers("unknown", "unknown"), "medium")


if __name__ == "__main__":
    unittest.main()