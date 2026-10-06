# chaos tests

## Purpose
Failure-injection and recovery verification.

## Owns
Provider outages, process crashes, retries, storage corruption, and dependency loss.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Destructive scenarios use fixtures only.

## Required Tests
Relevant chaos scenarios plus duplicate-side-effect assertions.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
