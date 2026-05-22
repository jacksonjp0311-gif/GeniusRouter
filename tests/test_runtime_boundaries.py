import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestRuntimeBoundaries(unittest.TestCase):
    def test_docs_architecture_exists(self):
        path = ROOT / "docs" / "software_architecture" / "geniusrouter_sa_v0_1_full_software_architecture.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("No routing claim without routing evidence", text)

    def test_v02_release_note_exists(self):
        path = ROOT / "docs" / "release_notes" / "v0_2_runtime_hardening.md"
        self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()