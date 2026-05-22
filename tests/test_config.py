import unittest

from geniusrouter.config import ConfigError, validate_config


VALID_CONFIG = {
    "routing": {
        "low_iq": "ollama/small",
        "medium_iq": "ollama/medium",
        "high_iq": "openrouter/high",
    },
    "local_rigs": {"low_url": "", "medium_url": "", "high_url": ""},
    "classifier": {"model": "granite4:350m", "enabled": True},
    "cache": {"enabled": True, "ttl_seconds": 3600},
}


class TestConfigValidation(unittest.TestCase):
    def test_valid_config_loads(self):
        cfg = validate_config(VALID_CONFIG)
        self.assertEqual(cfg.routing.low_iq, "ollama/small")
        self.assertTrue(cfg.classifier.enabled)
        self.assertEqual(cfg.cache.ttl_seconds, 3600)

    def test_missing_routing_fails(self):
        with self.assertRaises(ConfigError):
            validate_config({"cache": {"enabled": True}})

    def test_bad_ttl_fails(self):
        bad = dict(VALID_CONFIG)
        bad["cache"] = {"enabled": True, "ttl_seconds": 0}
        with self.assertRaises(ConfigError):
            validate_config(bad)


if __name__ == "__main__":
    unittest.main()