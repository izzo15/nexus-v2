# nexus

## Purpose
Nexus V2 production package.

## Owns
Control-plane and runtime implementation.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- No imports from legacy Nexus V1 production code.

## Required Tests
Unit, contract, integration, and affected Gold Set cases.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
