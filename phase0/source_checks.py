"""Deterministic source checks for already-confirmed Nexus V1 failure modes."""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class SourceCheck:
    id: str
    title: str
    file: str
    gold_cases: tuple[str, ...]
    predicate: Callable[[str], bool]


def _contains_all(*needles: str) -> Callable[[str], bool]:
    return lambda text: all(needle in text for needle in needles)


CHECKS = (
    SourceCheck("V1-QUEUE-001", "Router acknowledges coding queue without enqueue", "app/core/router.py", ("COD-002", "ROU-002"), lambda t: "_handle_coding" in t and "enqueue_task(" not in t),
    SourceCheck("V1-QUEUE-002", "Router acknowledges research queue without enqueue", "app/core/router.py", ("COD-003", "ROU-003"), lambda t: "_handle_research" in t and "enqueue_task(" not in t),
    SourceCheck("V1-QUEUE-003", "Router acknowledges automation queue without enqueue", "app/core/router.py", ("COD-004", "ROU-004"), lambda t: "_handle_automation" in t and "enqueue_task(" not in t),
    SourceCheck("V1-EVENT-001", "Event bus is process-local singleton", "app/events/bus.py", ("COD-006",), _contains_all("asyncio.Queue()", "bus = EventBus()")),
    SourceCheck("V1-ASYNC-001", "Async model method directly calls synchronous method", "app/core/llm.py", ("COD-005",), _contains_all("async def generate_response_async", "return self.generate_response(")),
    SourceCheck("V1-MEM-001", "Conversation history is newest-first", "app/core/memory.py", ("COD-001", "MEM-001"), _contains_all(".lpush(", ".lrange(")),
    SourceCheck("V1-PROVIDER-001", "Business logic constructs Ollama client directly", "app/core/llm.py", (), _contains_all("ollama.Client(")),
    SourceCheck("V1-HOST-001", "Router executes host command directly", "app/core/router.py", ("SEC-029",), _contains_all("os.system(")),
    SourceCheck("V1-HOST-002", "Router captures host screenshot directly", "app/core/router.py", ("AUT-004",), _contains_all("pyautogui.screenshot(")),
    SourceCheck("V1-HEALTH-001", "Health endpoint is static", "app/main.py", ("COD-010",), _contains_all('return {"status": "healthy"}')),
    SourceCheck("V1-DATETIME-001", "Task datetime default evaluated at import time", "app/models/task.py", ("COD-007",), _contains_all("created_at: datetime = datetime.now()")),
    SourceCheck("V1-VERIFY-001", "Verifier can pass despite separately recorded errors", "app/self_improvement/verifier.py", ("COD-049", "GOV-020"), _contains_all('if patched_tests["total"] > 0 and patched_tests["passed"] == patched_tests["total"]:', "elif errors:", 'status = "passed"')),
)


def run(v1_root: Path) -> list[dict]:
    results: list[dict] = []
    for check in CHECKS:
        path = v1_root / check.file
        if not path.is_file():
            results.append({
                "id": check.id,
                "title": check.title,
                "file": check.file,
                "status": "blocked",
                "detected": None,
                "reason": "source file missing",
                "gold_cases": list(check.gold_cases),
            })
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        detected = bool(check.predicate(text))
        results.append({
            "id": check.id,
            "title": check.title,
            "file": check.file,
            "status": "observed" if detected else "not_observed",
            "detected": detected,
            "gold_cases": list(check.gold_cases),
        })
    return results
