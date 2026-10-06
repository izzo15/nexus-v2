# scripts

## Purpose
Deterministic repository, CI, migration, and developer automation.

## Owns
Small auditable scripts used by governance and engineering workflows.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Scripts used as release gates must fail closed.

## Required Tests
Unit tests for nontrivial scripts plus execution in CI.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
