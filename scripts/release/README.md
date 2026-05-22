# GeniusRouter scripts/release/

## Purpose

Release and repair scripts for governed evolution.

## RCC Nexus Echo Location

Sphere Position:
- Shell: middle
- Meridian(s): release, validation, runtime
- Sector: release-scripts
- Version / TTL: GeniusRouter-SA-v0.4 / 180 days
- Last Verified: 2026-05

Local Role:
- Release and repair scripts for governed evolution.

Inbound Hooks:
- docs/DOCS_REGISTRY.md

Outbound Hooks:
- reports/validation/; reports/smoke/

Evidence Surface:
- reports/validation/

Validation Surface:
- python -m unittest discover -s tests

Claim Boundary:
- This folder improves navigation and traceability. It does not prove routing correctness, production readiness, cost savings, provider reliability, security, patch safety, or AI understanding.

Non-Claim Locks:
- navigation_is_not_validation
- context_is_not_truth
- rcc_n_is_not_code_correctness
- validation_remains_required

Agent Route:
- Read this README before editing files in this folder.
- Inspect relevant source, tests, docs, reports, or artifacts.
- Run declared validation before claiming completion.

Update Obligation:
- Update this README when folder role, outbound hooks, validation commands, evidence paths, or claim boundaries change.