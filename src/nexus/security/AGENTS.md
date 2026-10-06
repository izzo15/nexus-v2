# security

## Purpose
Security-specific runtime controls and validation.

## Owns
Security primitives that do not belong in the general policy layer.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Security-control regressions are release blockers.

## Required Tests
Security Gold Set and adversarial tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
