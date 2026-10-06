# Phase 0 Baseline Harness

Phase 0 measures Nexus V1; it does not modify or repair V1.

## Baseline
- Repository: `izzo15/nexus`
- Commit: `268e29b99cbf09f1ebfab8bf5f1e74fac8a0f175`
- Gold Set: `1.0.0`

## Commands

Validate the Gold Set:

```bash
python -m phase0.runner validate-goldset
```

Capture an immutable local V1 checkout:

```bash
python -m phase0.runner capture --v1-root ../nexus --output ./phase0-output
```

Run deterministic source-baseline checks:

```bash
python -m phase0.runner source-baseline --v1-root ../nexus --output ./phase0-output
```

Evaluate result records for false completion:

```bash
python -m phase0.runner evaluate-results --results results.jsonl --output ./phase0-output
```

Audit a legacy verifier report:

```bash
python -m phase0.runner audit-verifier --report verification_report.json --output ./phase0-output
```

Generated baseline output is evidence and should not be committed blindly. Each output directory contains hashes/manifests suitable for archival as a release artifact.
