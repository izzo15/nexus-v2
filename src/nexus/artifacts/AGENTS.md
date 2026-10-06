# artifacts

## Purpose
Immutable content-addressed artifact storage.

## Owns
CAS storage, hashes, metadata, lineage, and retention integration.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Existing blobs are immutable.

## Required Tests
Hash, immutability, corruption, lineage, and GC tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
