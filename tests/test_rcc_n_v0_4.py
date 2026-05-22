import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestGeniusRouterRCCNV04(unittest.TestCase):
    def test_rcc_nexus_index_exists(self):
        path = ROOT / "docs" / "context" / "rcc_nexus_index.json"
        self.assertTrue(path.exists())
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["schema"], "GeniusRouter-RCC-N-v0.4-nexus-index")

    def test_route_map_exists(self):
        path = ROOT / "rcc" / "nexus" / "route_map.json"
        self.assertTrue(path.exists())
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["schema"], "GeniusRouter-RCC-N-v0.4-route-map")
        self.assertTrue(data["routes"])

    def test_rcc_checker_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/rcc/check_rcc_nexus.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()