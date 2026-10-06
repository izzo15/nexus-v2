from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from phase0.source_checks import run


class SourceCheckTests(unittest.TestCase):
    def test_missing_sources_are_blocked_not_passed(self):
        with tempfile.TemporaryDirectory() as tmp:
            results = run(Path(tmp))
            self.assertTrue(results)
            self.assertTrue(all(item["status"] == "blocked" for item in results))

    def test_known_patterns_are_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            samples = {
                "app/core/router.py": "_handle_coding _handle_research _handle_automation os.system( pyautogui.screenshot(",
                "app/events/bus.py": "asyncio.Queue()\nbus = EventBus()",
                "app/core/llm.py": "ollama.Client(\nasync def generate_response_async():\n return self.generate_response(",
                "app/core/memory.py": ".lpush(\n.lrange(",
                "app/main.py": 'return {"status": "healthy"}',
                "app/models/task.py": "created_at: datetime = datetime.now()",
                "app/self_improvement/verifier.py": 'if patched_tests["total"] > 0 and patched_tests["passed"] == patched_tests["total"]:\n status = "passed"\nelif errors:',
            }
            for relative, content in samples.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            results = run(root)
            detected = {item["id"]: item["detected"] for item in results if item["detected"] is not None}
            self.assertTrue(detected["V1-QUEUE-001"])
            self.assertTrue(detected["V1-MEM-001"])
            self.assertTrue(detected["V1-VERIFY-001"])


if __name__ == "__main__":
    unittest.main()
