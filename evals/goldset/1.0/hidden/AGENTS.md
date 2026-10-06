# hidden cases

## Purpose
The hidden Gold Set partition.

## Owns
Only case records assigned to this immutable partition.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Do not move cases between splits inside version 1.0.

## Required Tests
Gold Set validation and anti-leak tests.

## Completion Criteria
All required checks pass and objective evidence exists for the change.
