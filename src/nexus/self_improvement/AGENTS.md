# self_improvement

## Purpose
Controlled proposal and evaluation of Nexus changes.

## Owns
Observation, hypothesis, proposal, verification, PR/canary integration.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- May never modify root policy, approvals, audit controls, sandbox boundaries, or held-out eval answers.

## Required Tests
Full regression, held-out eval, security, and anti-gaming tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
