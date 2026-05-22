# GeniusRouter docs/architecture_changes/

## Purpose

Versioned architecture change records.

## RCC Nexus Echo Location

Sphere Position:
- Shell: outer
- Meridian(s): release, documentation
- Sector: change-records
- Version / TTL: GeniusRouter-SA-v0.4 / 180 days
- Last Verified: 2026-05

Local Role:
- Versioned architecture change records.

Inbound Hooks:
- docs/DOCS_REGISTRY.md

Outbound Hooks:
- docs/release_notes/; docs/validation/

Evidence Surface:
- docs/architecture_changes/

Validation Surface:
- python scripts/rcc/check_rcc_nexus.py

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