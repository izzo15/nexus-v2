"""CLI entry point for Nexus Phase 0."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

from phase0.capture import BASELINE_COMMIT, write_capture
from phase0.false_completion import detect_false_completion, detect_verifier_anomalies
from phase0.goldset import validate as validate_goldset
from phase0.source_checks import run as run_source_checks


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def cmd_validate_goldset(_: argparse.Namespace) -> int:
    result = validate_goldset()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["valid"] else 1


def cmd_capture(args: argparse.Namespace) -> int:
    root = Path(args.v1_root).resolve()
    output = Path(args.output).resolve()
    if not root.is_dir():
        print(f"V1 root not found: {root}", file=sys.stderr)
        return 2
    hashes = write_capture(root, output)
    repo = json.loads((output / "manifests" / "repository.json").read_text(encoding="utf-8"))
    print(json.dumps({"hashes": hashes, "baseline_commit_matches": repo["baseline_commit_matches"]}, indent=2))
    return 0 if repo["baseline_commit_matches"] else 3


def cmd_source_baseline(args: argparse.Namespace) -> int:
    root = Path(args.v1_root).resolve()
    output = Path(args.output).resolve()
    results = run_source_checks(root)
    path = output / "results" / "source_baseline.json"
    _write_json(path, {
        "baseline_commit": BASELINE_COMMIT,
        "checks": results,
        "summary": dict(Counter(item["status"] for item in results)),
    })
    print(path)
    return 0 if all(item["status"] != "blocked" for item in results) else 2


def cmd_evaluate_results(args: argparse.Namespace) -> int:
    results = _load_jsonl(Path(args.results))
    false_items = []
    for record in results:
        reasons = detect_false_completion(record)
        if reasons:
            false_items.append({"case_id": record.get("case_id"), "reasons": reasons})
    summary = {
        "records": len(results),
        "false_completion_count": len(false_items),
        "false_completion_rate": (len(false_items) / len(results)) if results else 0.0,
        "false_completions": false_items,
    }
    output = Path(args.output) / "reports" / "false_completion.json"
    _write_json(output, summary)
    print(json.dumps(summary, indent=2))
    return 0 if not false_items else 4


def cmd_audit_verifier(args: argparse.Namespace) -> int:
    report = json.loads(Path(args.report).read_text(encoding="utf-8"))
    anomalies = detect_verifier_anomalies(report)
    output = Path(args.output) / "reports" / "verifier_anomalies.json"
    _write_json(output, {"anomaly_count": len(anomalies), "anomalies": anomalies})
    print(json.dumps({"anomaly_count": len(anomalies), "output": str(output)}, indent=2))
    return 0 if not anomalies else 5


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Nexus V1 Phase 0 baseline harness")
    sub = parser.add_subparsers(dest="command", required=True)

    validate_parser = sub.add_parser("validate-goldset")
    validate_parser.set_defaults(func=cmd_validate_goldset)

    capture = sub.add_parser("capture")
    capture.add_argument("--v1-root", required=True)
    capture.add_argument("--output", required=True)
    capture.set_defaults(func=cmd_capture)

    source = sub.add_parser("source-baseline")
    source.add_argument("--v1-root", required=True)
    source.add_argument("--output", required=True)
    source.set_defaults(func=cmd_source_baseline)

    evaluate = sub.add_parser("evaluate-results")
    evaluate.add_argument("--results", required=True)
    evaluate.add_argument("--output", required=True)
    evaluate.set_defaults(func=cmd_evaluate_results)

    verifier = sub.add_parser("audit-verifier")
    verifier.add_argument("--report", required=True)
    verifier.add_argument("--output", required=True)
    verifier.set_defaults(func=cmd_audit_verifier)

    return parser


def main() -> int:
    args = build_parser().parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
