import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestGeniusRouterV03Docs(unittest.TestCase):
    def test_v03_docs_exist(self):
        required = [
            "docs/architecture_changes/geniusrouter_sa_v0_3_smoke_validation.md",
            "docs/release_notes/v0_3_smoke_validation.md",
            "docs/validation/validation_surface_v0_3.md",
            "scripts/release/run_smoke_validation_v0_3.py",
        ]
        for rel in required:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_context_index_current_layer(self):
        data = json.loads((ROOT / "docs" / "context" / "repository_context_index.json").read_text(encoding="utf-8"))
        self.assertRegex(data["current_layer"], r"^GeniusRouter-SA v0\.(3|4)(\.\d+)?")
        self.assertIn(data["status"], {"smoke-validation-runtime-evidence-layer", "rcc-n-navigation-injection"})


if __name__ == "__main__":
    unittest.main()