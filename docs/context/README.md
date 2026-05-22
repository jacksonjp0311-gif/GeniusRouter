# GeniusRouter docs/context/

## Purpose

Machine-readable repository and RCC-N context indexes.

## RCC Nexus Echo Location

Sphere Position:
- Shell: center
- Meridian(s): documentation, agent, validation
- Sector: context
- Version / TTL: GeniusRouter-SA-v0.4 / 180 days
- Last Verified: 2026-05

Local Role:
- Machine-readable repository and RCC-N context indexes.

Inbound Hooks:
- README_5_MINUTES.md; docs/DOCS_REGISTRY.md

Outbound Hooks:
- repository_context_index.json; rcc_nexus_index.json; rcc/nexus/route_map.json

Evidence Surface:
- reports/rcc_nexus/

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