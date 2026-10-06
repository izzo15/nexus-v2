# Gold Set fixtures

## Purpose
Safe benchmark fixtures only.

## Owns
Synthetic repositories, fake secrets, captured web corpora, mock services, and failure scenarios.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Never place real credentials, production data, or destructive live targets here.

## Required Tests
Fixture integrity and safety checks.

## Completion Criteria
All required checks pass and objective evidence exists for the change.
