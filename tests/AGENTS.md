# tests

## Purpose
Deterministic verification hierarchy.

## Owns
Unit, contract, integration, security, chaos, workflow, regression, and E2E tests.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Tests may not be weakened to make implementation pass.

## Required Tests
The tests themselves are the required verification layer.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
