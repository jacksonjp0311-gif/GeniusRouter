import unittest

from geniusrouter.cache import stable_cache_key


class TestStableCacheKey(unittest.TestCase):
    def test_cache_key_is_stable(self):
        messages = [{"role": "user", "content": "hello"}]
        a = stable_cache_key(messages, "ollama/small")
        b = stable_cache_key(messages, "ollama/small")
        self.assertEqual(a, b)
        self.assertEqual(len(a), 64)

    def test_cache_key_changes_by_model(self):
        messages = [{"role": "user", "content": "hello"}]
        a = stable_cache_key(messages, "ollama/small")
        b = stable_cache_key(messages, "openrouter/high")
        self.assertNotEqual(a, b)


if __name__ == "__main__":
    unittest.main()