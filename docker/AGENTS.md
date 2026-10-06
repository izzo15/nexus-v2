# docker

## Purpose
Container build/runtime definitions.

## Owns
API, worker, sandbox, and supporting image definitions.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Production images must be minimal, non-root, and pinned/traceable.

## Required Tests
Build, vulnerability, non-root, and runtime-policy checks.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
