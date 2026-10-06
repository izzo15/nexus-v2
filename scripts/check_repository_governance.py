from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_NAMES = {
    ".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache",
    ".mypy_cache", ".ruff_cache", "dist", "build", ".idea", ".vscode",
}
ALLOWED_BRANCH_PREFIXES = (
    "feat/", "fix/", "security/", "test/", "refactor/", "docs/", "chore/",
    "release/", "hotfix/",
)
PERMANENT_BRANCHES = {"main", "develop"}


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def tracked_directories(files: list[str]) -> set[Path]:
    dirs: set[Path] = {Path(".")}
    for item in files:
        path = Path(item)
        parent = path.parent
        while str(parent) not in ("", "."):
            if not any(part in EXCLUDED_NAMES for part in parent.parts):
                dirs.add(parent)
            parent = parent.parent
    return dirs


def check_agents(files: list[str]) -> list[str]:
    tracked = set(files)
    missing: list[str] = []
    for directory in sorted(tracked_directories(files), key=str):
        expected = "AGENTS.md" if directory == Path(".") else f"{directory.as_posix()}/AGENTS.md"
        if expected not in tracked:
            missing.append(expected)
    return missing


def current_branch() -> str | None:
    branch = os.getenv("GITHUB_HEAD_REF") or os.getenv("GITHUB_REF_NAME")
    if branch:
        return branch
    result = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() or None


def check_branch(branch: str | None) -> str | None:
    if not branch or branch in PERMANENT_BRANCHES:
        return None
    if branch.startswith(ALLOWED_BRANCH_PREFIXES):
        return None
    return f"Branch '{branch}' does not use an approved prefix."


def main() -> int:
    files = tracked_files()
    failures: list[str] = []

    missing = check_agents(files)
    if missing:
        failures.append(
            "Missing AGENTS.md files:\n  - " + "\n  - ".join(missing)
        )

    branch_failure = check_branch(current_branch())
    if branch_failure:
        failures.append(branch_failure)

    if failures:
        print("REPOSITORY GOVERNANCE: FAIL")
        for failure in failures:
            print(f"\n{failure}")
        return 1

    print("REPOSITORY GOVERNANCE: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
