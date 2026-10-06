# api

## Purpose
Typed HTTP/BFF API surface.

## Owns
FastAPI routes, auth/session boundaries, errors, streaming, and request dependencies.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Browser-facing code must not expose provider credentials.

## Required Tests
API contract, auth, RFC problem response, and integration tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
