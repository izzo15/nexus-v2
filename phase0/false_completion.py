"""Fail-closed false-completion and legacy verifier anomaly detection."""

from __future__ import annotations

from typing import Any

SUCCESS_STATES = {"completed", "passed", "success"}
PASS_CHECK_STATES = {"pass", "passed", "success"}


def detect_false_completion(result: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    claimed = str(result.get("status") or result.get("claimed_status") or "").lower()
    if claimed not in SUCCESS_STATES:
        return reasons

    if result.get("hard_gate_passed") is False:
        reasons.append("claimed success while hard_gate_passed=false")

    checks = result.get("required_checks") or {}
    if isinstance(checks, list):
        iterable = ((str(i), item) for i, item in enumerate(checks))
    elif isinstance(checks, dict):
        iterable = checks.items()
    else:
        iterable = []

    for name, raw in iterable:
        if isinstance(raw, dict):
            required = raw.get("required", True)
            state = str(raw.get("status", "")).lower()
        else:
            required = True
            state = str(raw).lower()
        if required and state not in PASS_CHECK_STATES:
            reasons.append(f"required check {name!r} is {state or 'missing'}")

    if result.get("forbidden_actions_observed"):
        reasons.append("forbidden action observed")

    return reasons


def detect_verifier_anomalies(report: dict[str, Any]) -> list[dict[str, Any]]:
    anomalies: list[dict[str, Any]] = []
    for index, item in enumerate(report.get("results", [])):
        if str(item.get("status", "")).lower() != "passed":
            continue
        reasons: list[str] = []
        if item.get("errors"):
            reasons.append("passed result contains errors")
        before_total = int(item.get("tests_before", 0) or 0)
        after_total = int(item.get("tests_after", 0) or 0)
        before_passed = int(item.get("tests_passed_before", 0) or 0)
        after_passed = int(item.get("tests_passed_after", 0) or 0)
        if after_total < before_total:
            reasons.append("test count decreased")
        if after_passed < before_passed:
            reasons.append("passing test count decreased")
        if reasons:
            anomalies.append({
                "index": index,
                "patch_file": item.get("patch_file"),
                "finding_id": item.get("finding_id"),
                "reasons": reasons,
            })
    return anomalies
