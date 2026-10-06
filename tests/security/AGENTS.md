# security tests

## Purpose
Adversarial and security invariant verification.

## Owns
Prompt injection, secret leakage, path/SSRF, privilege, approval, and policy tests.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- A security test failure cannot be waived by quality scoring.

## Required Tests
100% of critical security cases.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
