# workflows

## Purpose
Durable Temporal orchestration.

## Owns
Deterministic workflows, signals, queries, cancellation, compensation, and orchestration state.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- External/nondeterministic work belongs in Activities, not workflow logic.

## Required Tests
Temporal replay, crash recovery, idempotency, and workflow tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
