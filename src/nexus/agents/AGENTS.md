# agents

## Purpose
Agent runtime and specialist definitions.

## Owns
Orchestration, specialist configuration, context requests, and delegation.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Agents have no implicit authority; tools enforce capability boundaries.

## Required Tests
Agent behavior, routing, authority, and Gold Set trajectory tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
