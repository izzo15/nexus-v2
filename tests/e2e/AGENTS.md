# e2e

## Purpose
End-to-end user-visible workflow verification.

## Owns
Full API-to-workflow-to-artifact/action paths.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- E2E success requires objective completion evidence.

## Required Tests
Required E2E scenarios for changed capabilities.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
