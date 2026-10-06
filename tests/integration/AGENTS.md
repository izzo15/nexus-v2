# integration

## Purpose
Cross-component tests.

## Owns
Realistic integration among databases, queues, gateways, and services.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Use isolated test resources only.

## Required Tests
Relevant service-backed integration suite.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
