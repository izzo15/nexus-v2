# tools

## Purpose
Typed tool registry and execution boundary.

## Owns
Tool manifests, gateways, validation, MCP adapters, and executors.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- No privileged action bypasses the policy gateway.

## Required Tests
Permission, schema, idempotency, timeout, and adversarial tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
