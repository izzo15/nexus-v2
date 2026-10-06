"""Gold Set loading and structural validation."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

SUITE_ROOT = Path(__file__).resolve().parents[1] / "evals" / "goldset" / "1.0"
EXPECTED_SPLITS = {"development": 150, "hidden": 50, "held_out": 50}
EXPECTED_CATEGORIES = {
    "coding": 60,
    "research": 35,
    "tools_automation": 30,
    "memory_context": 20,
    "routing_delegation": 15,
    "security_adversarial": 45,
    "resilience_chaos": 25,
    "governance_approval_idempotency": 20,
}
REQUIRED_FIELDS = {
    "id", "version", "suite_version", "category", "split", "title",
    "authoring_status", "hard_gate", "budgets",
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{number}: invalid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{number}: case must be an object")
        records.append(value)
    return records


def load_all(root: Path = SUITE_ROOT) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for split in ("development", "hidden", "held_out"):
        records.extend(load_jsonl(root / split / "cases.jsonl"))
    return records


def validate(root: Path = SUITE_ROOT) -> dict[str, Any]:
    errors: list[str] = []
    all_cases: list[dict[str, Any]] = []
    split_counts: dict[str, int] = {}

    for split, expected_count in EXPECTED_SPLITS.items():
        path = root / split / "cases.jsonl"
        if not path.is_file():
            errors.append(f"missing {path}")
            continue
        cases = load_jsonl(path)
        split_counts[split] = len(cases)
        if len(cases) != expected_count:
            errors.append(f"{split}: expected {expected_count}, got {len(cases)}")
        for case in cases:
            missing = sorted(REQUIRED_FIELDS - case.keys())
            if missing:
                errors.append(f"{case.get('id', '<unknown>')}: missing {missing}")
            if case.get("split") != split:
                errors.append(f"{case.get('id')}: split field does not match directory")
            if case.get("suite_version") != "1.0.0":
                errors.append(f"{case.get('id')}: suite_version must be 1.0.0")
        all_cases.extend(cases)

    ids = [case.get("id") for case in all_cases]
    duplicates = [item for item, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append(f"duplicate case IDs: {duplicates}")

    category_counts = Counter(case.get("category") for case in all_cases)
    for category, expected in EXPECTED_CATEGORIES.items():
        actual = category_counts.get(category, 0)
        if actual != expected:
            errors.append(f"{category}: expected {expected}, got {actual}")

    if len(all_cases) != 250:
        errors.append(f"expected 250 total cases, got {len(all_cases)}")

    return {
        "valid": not errors,
        "errors": errors,
        "total": len(all_cases),
        "split_counts": split_counts,
        "category_counts": dict(category_counts),
    }
