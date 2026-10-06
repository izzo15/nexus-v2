# docs

## Purpose
Architecture, operating, and engineering documentation.

## Owns
ADRs, runbooks, specifications, and durable design rationale.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Documentation must match implemented behavior; do not document nonexistent guarantees.

## Required Tests
Link/reference validation where applicable.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
