# .github

## Purpose
Repository governance, ownership, PR policy, and CI configuration.

## Owns
GitHub Actions, CODEOWNERS, templates, and repository governance files.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Changes here are security-relevant because they control promotion.
- Never remove required checks merely to unblock a PR.

## Required Tests
Governance validation plus workflow syntax/behavior checks.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
