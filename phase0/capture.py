"""Read-only capture of Nexus V1 repository and execution environment."""

from __future__ import annotations

import hashlib
import json
import platform
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BASELINE_COMMIT = "268e29b99cbf09f1ebfab8bf5f1e74fac8a0f175"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _run(command: list[str], cwd: Path | None = None, timeout: int = 30) -> dict[str, Any]:
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        return {
            "available": True,
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        }
    except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
        return {"available": False, "error": type(exc).__name__, "detail": str(exc)}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def capture_repository(v1_root: Path) -> dict[str, Any]:
    root = v1_root.resolve()
    head = _run(["git", "rev-parse", "HEAD"], root)
    branch = _run(["git", "branch", "--show-current"], root)
    status = _run(["git", "status", "--porcelain"], root)
    listed = _run(["git", "ls-files"], root)

    tracked: list[dict[str, Any]] = []
    if listed.get("returncode") == 0:
        for relative in listed.get("stdout", "").splitlines():
            path = root / relative
            if path.is_file():
                tracked.append({
                    "path": relative,
                    "size": path.stat().st_size,
                    "sha256": sha256_file(path),
                })

    tree_hash = hashlib.sha256()
    for item in sorted(tracked, key=lambda x: x["path"]):
        tree_hash.update(item["path"].encode())
        tree_hash.update(b"\0")
        tree_hash.update(item["sha256"].encode())
        tree_hash.update(b"\n")

    return {
        "captured_at": _now(),
        "root": str(root),
        "expected_baseline_commit": BASELINE_COMMIT,
        "head": head.get("stdout"),
        "baseline_commit_matches": head.get("stdout") == BASELINE_COMMIT,
        "branch": branch.get("stdout"),
        "working_tree_clean": status.get("stdout", "") == "",
        "status_porcelain": status.get("stdout", ""),
        "tracked_file_count": len(tracked),
        "tracked_tree_sha256": tree_hash.hexdigest(),
        "tracked_files": tracked,
    }


def capture_environment(v1_root: Path) -> dict[str, Any]:
    commands = {
        "git": ["git", "--version"],
        "pip": [sys.executable, "-m", "pip", "--version"],
        "redis_server": ["redis-server", "--version"],
        "ollama": ["ollama", "--version"],
        "node": ["node", "--version"],
        "npm": ["npm", "--version"],
    }
    versions = {name: _run(command, v1_root) for name, command in commands.items()}
    freeze = _run([sys.executable, "-m", "pip", "freeze"], v1_root, timeout=60)
    ollama_list = _run(["ollama", "list"], v1_root, timeout=30)

    requirements = v1_root / "requirements.txt"
    return {
        "captured_at": _now(),
        "platform": platform.platform(),
        "system": platform.system(),
        "machine": platform.machine(),
        "python_version": sys.version,
        "python_executable": sys.executable,
        "versions": versions,
        "pip_freeze": freeze.get("stdout", "").splitlines() if freeze.get("available") else [],
        "requirements_sha256": sha256_file(requirements) if requirements.is_file() else None,
        "ollama_models_raw": ollama_list.get("stdout") if ollama_list.get("available") else None,
    }


def capture_services() -> dict[str, Any]:
    return {
        "captured_at": _now(),
        "expected_v1_services": [
            {"name": "api", "command": "uvicorn app.main:app --reload"},
            {"name": "task_runner", "command": "python -m app.workers.task_runner"},
            {"name": "scheduler", "command": "python -m app.self_improvement.scheduler"},
            {"name": "redis", "role": "queue and memory"},
            {"name": "ollama", "role": "model provider"},
            {"name": "dashboard", "command": "npm run dev", "optional": True},
        ],
    }


def write_capture(v1_root: Path, output: Path) -> dict[str, str]:
    manifests = output / "manifests"
    manifests.mkdir(parents=True, exist_ok=True)
    payloads = {
        "repository.json": capture_repository(v1_root),
        "environment.json": capture_environment(v1_root),
        "services.json": capture_services(),
    }
    hashes: dict[str, str] = {}
    for name, payload in payloads.items():
        path = manifests / name
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        hashes[name] = sha256_file(path)
    (manifests / "checksums.json").write_text(
        json.dumps(hashes, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return hashes
