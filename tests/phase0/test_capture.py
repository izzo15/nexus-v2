from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from phase0.capture import sha256_file


class CaptureTests(unittest.TestCase):
    def test_sha256_file_is_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.txt"
            path.write_text("nexus\n", encoding="utf-8")
            first = sha256_file(path)
            second = sha256_file(path)
            self.assertEqual(first, second)
            self.assertEqual(len(first), 64)


if __name__ == "__main__":
    unittest.main()
