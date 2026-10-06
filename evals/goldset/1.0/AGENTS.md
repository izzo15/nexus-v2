# Gold Set 1.0

## Purpose
Frozen Nexus V2 benchmark definition.

## Owns
The immutable 1.0 case inventory, splits, schemas, evaluator contracts, and safe fixtures.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Development/hidden/held-out membership may not change without a new Gold Set version.

## Required Tests
Gold Set structural validation and anti-leak tests.

## Completion Criteria
All required checks pass and objective evidence exists for the change.
