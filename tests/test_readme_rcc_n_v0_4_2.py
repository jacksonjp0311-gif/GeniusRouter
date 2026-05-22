import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestGeniusRouterReadmeRCCNV042(unittest.TestCase):
    def test_root_readme_trisection_present(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        required = [
            "Human Director Box",
            "# PART I - Human README",
            "# PART II - RCC Nexus README",
            "# PART III - AI Agent README",
            "GeniusRouter-SA v0.4.2",
            "Current Versioned Documentation Stack",
            "GeniusRouter-SA v0.4.2 README / RCC-N Alignment",
        ]
        for marker in required:
            self.assertIn(marker, text)

    def test_context_indexes_v042(self):
        repo = json.loads((ROOT / "docs/context/repository_context_index.json").read_text(encoding="utf-8"))
        nexus = json.loads((ROOT / "docs/context/rcc_nexus_index.json").read_text(encoding="utf-8"))
        self.assertEqual(repo["current_layer"], "GeniusRouter-SA v0.4.2")
        self.assertEqual(nexus["current_layer"], "GeniusRouter-SA v0.4.2")
        self.assertEqual(nexus["readme_trisection_status"], "full-root-readme-aligned")

    def test_rcc_checker_still_passes(self):
        result = subprocess.run(
            [sys.executable, "scripts/rcc/check_rcc_nexus.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()