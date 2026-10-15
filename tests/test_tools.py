"""Focused portability and acquisition checks. Not linguistic validation.

Ge'ez Lab / https://ethiopiancanon.com. MIT.
"""

import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("make_chunks", ROOT / "make_chunks.py")
chunks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chunks)


class Response(io.BytesIO):
    def __init__(self, data, content_type="image/jpeg"):
        super().__init__(data)
        self.headers = {"Content-Type": content_type}


class AcquisitionTests(unittest.TestCase):
    def test_shared_boundary_is_one_image_with_two_allocations(self):
        rows = chunks.build_index()
        by_code = {r["code"]: r for r in rows}
        self.assertEqual(len(rows), 249)
        self.assertEqual(len(by_code), 249)
        self.assertEqual(by_code["MAIX1-241R"]["catalogue_books"], "VI;VII")
        self.assertEqual(rows[0]["canvas"], 309)
        self.assertEqual(rows[-1]["canvas"], 557)

    def test_html_response_does_not_replace_an_existing_image(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "image.jpg"
            target.write_bytes(b"existing image")
            with self.assertRaises(ValueError):
                chunks.fetch_image("https://example.org/image", target,
                                   opener=lambda *a, **k: Response(b"<html>login</html>", "text/html"))
            self.assertEqual(target.read_bytes(), b"existing image")
            self.assertFalse(target.with_suffix(".jpg.part").exists())

    def test_truncated_response_is_not_installed(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "image.jpg"
            with self.assertRaises(ValueError):
                chunks.fetch_image("https://example.org/image", target,
                                   opener=lambda *a, **k: Response(b"\xff\xd8\xfftruncated"))
            self.assertFalse(target.exists())
            self.assertFalse(target.with_suffix(".jpg.part").exists())

    def test_transport_complete_image_is_installed_atomically(self):
        payload = b"\xff\xd8\xfftransport-test\xff\xd9"
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "nested" / "image.jpg"
            chunks.fetch_image("https://example.org/image", target,
                               opener=lambda *a, **k: Response(payload))
            self.assertEqual(target.read_bytes(), payload)
            self.assertFalse(target.with_suffix(".jpg.part").exists())


class PortabilityTests(unittest.TestCase):
    def test_tools_find_corpus_from_an_unrelated_working_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            for script, args, expected in [
                ("tgrep.py", ["ኤርምያስ"], "hit(s) in transcription"),
                ("seams.py", [], "67 adjacent seams available, 0 gaps"),
                ("ab/cross.py", ["153R"], "THE TEST"),
                ("ab/score_ab.py", [], "MEAN"),
            ]:
                with self.subTest(script=script):
                    result = subprocess.run([sys.executable, str(ROOT / script), *args],
                                            cwd=directory, capture_output=True, text=True, timeout=30)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIn(expected, result.stdout)

    def test_search_does_not_match_commentary(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([sys.executable, str(ROOT / "tgrep.py"), "Falsifiers"],
                                    cwd=directory, capture_output=True, text=True, timeout=30)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("0 hit(s) in transcription", result.stdout)


if __name__ == "__main__":
    unittest.main()
