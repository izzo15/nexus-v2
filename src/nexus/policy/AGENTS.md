# policy

## Purpose
Deterministic authorization and policy enforcement.

## Owns
Permissions, capability evaluation, data classification, approval requirements, and redaction.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Default deny.
- Agent reasoning cannot override policy.

## Required Tests
100% pass for security/control policy tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
