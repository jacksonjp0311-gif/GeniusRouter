# GeniusRouter docs/software_architecture/

## Purpose

Software architecture documents and RCC-N injection architecture.

## RCC Nexus Echo Location

Sphere Position:
- Shell: center
- Meridian(s): source, documentation, safety
- Sector: architecture
- Version / TTL: GeniusRouter-SA-v0.4 / 180 days
- Last Verified: 2026-05

Local Role:
- Software architecture documents and RCC-N injection architecture.

Inbound Hooks:
- docs/DOCS_REGISTRY.md

Outbound Hooks:
- geniusrouter_sa_v0_1_full_software_architecture.md; geniusrouter_sa_v0_4_rcc_n_injection.md

Evidence Surface:
- docs/validation/

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