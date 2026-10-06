# unit

## Purpose
Fast isolated unit tests.

## Owns
Pure and narrowly scoped behavior.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Avoid network/process dependencies.

## Required Tests
All affected unit tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
