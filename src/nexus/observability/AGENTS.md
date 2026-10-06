# observability

## Purpose
OpenTelemetry instrumentation and privacy-safe operational visibility.

## Owns
Tracing, metrics, structured logs, correlation, and redaction.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not introduce hidden cross-layer dependencies.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Raw prompts, secrets, and sensitive content are excluded by default.

## Required Tests
Telemetry schema, propagation, redaction, and failure tests.

## Completion Criteria
All required checks pass and the change has objective evidence appropriate to its risk.
