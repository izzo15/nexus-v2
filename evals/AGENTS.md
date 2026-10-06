# evals

## Purpose
Versioned agent evaluation assets.

## Owns
Gold Sets, schemas, evaluators, baselines, and held-out governance.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Production agents must not receive held-out answers.

## Required Tests
Dataset/schema validation plus evaluator tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
