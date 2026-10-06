# config

## Purpose
Versioned non-secret Nexus configuration.

## Owns
Model aliases, agent specs, policies, tools, evaluation settings, and safe defaults.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Secrets never belong here.
- Policy changes require explicit review and versioning.

## Required Tests
Schema/contract validation plus policy tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
