# sandbox

## Purpose
Isolation for generated/untrusted code execution.

## Owns
Sandbox broker, OCI runtime policy, resource limits, egress, and teardown.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Agents never receive direct Docker-daemon access.

## Required Tests
Escape, path, network, resource-limit, and teardown tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
