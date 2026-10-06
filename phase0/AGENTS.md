# phase0

## Purpose
Nexus V1 freeze, evidence capture, baseline runner, and comparison artifacts.

## Owns
Baseline manifests, historical evidence references, case results, and scorecards.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Phase 0 measures V1; it does not fix V1.

## Required Tests
Baseline harness tests and reproducibility checks.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
