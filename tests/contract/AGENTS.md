# contract

## Purpose
Schema and interface compatibility tests.

## Owns
API, event, manifest, tool, policy, and persistence contracts.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Breaking changes require versioning and migration.

## Required Tests
All affected contract tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
