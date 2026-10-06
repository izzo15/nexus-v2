# Phase 0 tests

## Purpose
Tests for the baseline harness, Gold Set structure, false-completion logic, and source checks.

## Owns
Phase 0 harness verification only.

## Inherits
All rules from parent `AGENTS.md` files apply here.

## Invariants
- Keep responsibilities inside this directory's boundary.
- Do not weaken parent security, testing, audit, or approval requirements.
- New subdirectories must include their own `AGENTS.md` in the same change.
- Tests must use temporary/synthetic fixtures and never mutate the real V1 repository.

## Required Tests
All tests in this directory plus governance and Gold Set validation.

## Completion Criteria
All required checks pass and objective evidence exists for the change.
