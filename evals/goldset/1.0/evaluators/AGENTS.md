# Gold Set evaluators

## Purpose
Versioned evaluator contracts; implementation lives in audited Phase 0/runtime modules.

## Owns
Evaluator definitions, hard-gate rules, and scoring metadata.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Semantic scoring may never override a deterministic hard failure.

## Required Tests
Evaluator unit tests and anti-gaming checks.

## Completion Criteria
All required checks pass and objective evidence exists for the change.
