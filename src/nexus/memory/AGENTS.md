# memory

## Purpose
Provenance-aware memory and context retrieval.

## Owns
Memory ingestion, retrieval, deduplication, supersession, and embeddings.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Redis is never canonical memory.

## Required Tests
Chronology, provenance, isolation, retrieval, and injection-resistance tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
