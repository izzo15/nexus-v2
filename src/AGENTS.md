# src

## Purpose
Production source-code root.

## Owns
Installable application packages only.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Generated/runtime artifacts do not belong here.

## Required Tests
Relevant unit, contract, integration, typing, lint, and security tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
