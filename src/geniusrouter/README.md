# GeniusRouter src/geniusrouter/

## Purpose

Structured GeniusRouter runtime package.

## RCC Nexus Echo Location

Sphere Position:
- Shell: inner
- Meridian(s): runtime, evidence, validation
- Sector: runtime-core
- Version / TTL: GeniusRouter-SA-v0.4 / 180 days
- Last Verified: 2026-05

Local Role:
- Structured GeniusRouter runtime package.

Inbound Hooks:
- src/main.py; config.yaml

Outbound Hooks:
- tests/; artifacts/routing_decisions/; reports/smoke/

Evidence Surface:
- artifacts/routing_decisions/; reports/smoke/

Validation Surface:
- python -m unittest discover -s tests; python scripts/release/run_smoke_validation_v0_3.py

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