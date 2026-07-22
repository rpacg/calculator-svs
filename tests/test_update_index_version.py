import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("update_index_version", ROOT / "update_index_version.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class UpdateIndexVersionTests(unittest.TestCase):
    def test_sync_index_to_latest_version_updates_title_and_footer(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            (tmp_path / "Score Calculator SVS v9.3.18.html").write_text(
                "<html><title>Old</title><footer>V9.3.18</footer></html>",
                encoding="utf-8",
            )
            (tmp_path / "Score Calculator SVS v9.3.19.html").write_text(
                "<html><title>New</title><footer>V9.3.19</footer></html>",
                encoding="utf-8",
            )
            index_path = tmp_path / "index.html"
            index_path.write_text(
                "<title>SVS Championship — Kalkulator Skor v9.3.18</title><footer>SVS CHAMPIONSHIP V9.3.18</footer>",
                encoding="utf-8",
            )

            changed, version = MODULE.sync_index_to_latest_version(tmp_path, index_path)

            self.assertTrue(changed)
            self.assertEqual(version, "v9.3.19")
            text = index_path.read_text(encoding="utf-8")
            self.assertIn("v9.3.19", text)
            self.assertIn("V9.3.19", text)


if __name__ == "__main__":
    unittest.main()
