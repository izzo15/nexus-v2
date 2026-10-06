# GitHub Actions Workflows

## Purpose
CI/CD gates for Nexus.

## Owns
Governance, fast CI, integration, security, Gold Set, chaos, and release workflows.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Workflow changes must not reduce required protection.
- A failing, skipped, or unavailable required check is not a pass.

## Required Tests
Workflow validation and representative dry-run/fixture checks.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
