# Architecture Decision Records

## Purpose
Immutable records of material architecture decisions.

## Owns
Context, decision, alternatives, consequences, migration impact, and rollback.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Supersede prior ADRs; do not silently rewrite architectural history.

## Required Tests
ADR structure validation.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
