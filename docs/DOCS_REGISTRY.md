# GeniusRouter Docs Registry

## Current Architecture Stack

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/geniusrouter_sa_v0_1_full_software_architecture.md` | active | Defines the v0.1 full structural runtime architecture. |
| Architecture Change | `docs/architecture_changes/geniusrouter_sa_v0_1_docs_architecture_injection.md` | active | Records the docs architecture injection. |
| Release Note | `docs/release_notes/v0_1_docs_architecture_injection.md` | active | Records v0.1 docs checkpoint. |
| Non-Claim Locks | `docs/protocols/non_claim_locks.md` | active | Defines what GeniusRouter does not yet prove. |
| AI Operating Contract | `docs/protocols/ai_operating_contract.md` | active | Defines safe AI/developer modification workflow. |
| Routing Decision Contract | `docs/protocols/routing_decision_contract.md` | active | Defines future routing evidence record. |
| Runtime Hardening Plan | `docs/protocols/runtime_hardening_plan.md` | active | Defines the v0.2 runtime hardening target. |
| Roadmap | `docs/roadmap/geniusrouter_sa_roadmap.md` | active | Defines the v0.1 -> v1.0 path. |
| Validation Surface | `docs/validation/validation_surface_v0_1.md` | active | Defines valid and invalid v0.1 claims. |
| Repository Context Index | `docs/context/repository_context_index.json` | active | Machine-readable repo orientation seed. |

## Current Status

GeniusRouter-SA v0.1 is a docs architecture checkpoint. Runtime behavior is intentionally unchanged.

## Boundary

The docs registry improves navigation and traceability. It does not prove code correctness, production readiness, routing quality, cost savings, provider reliability, or benchmark validity.
## GeniusRouter-SA v0.2 Runtime Hardening Scaffold

| Layer | File | Status | Purpose |
|---|---|---|---|
| Architecture Change | `docs/architecture_changes/geniusrouter_sa_v0_2_runtime_hardening.md` | active | Records runtime package hardening. |
| Release Note | `docs/release_notes/v0_2_runtime_hardening.md` | active | Records the v0.2 checkpoint. |
| Validation Surface | `docs/validation/validation_surface_v0_2.md` | active | Defines valid and invalid v0.2 claims. |
| Runtime Package | `src/geniusrouter/` | active | Structured router package. |
| Tests | `tests/` | active | First local validation tests. |

Boundary: v0.2 improves structure. It does not prove routing quality, production readiness, cost savings, or RCC-N completion.
## GeniusRouter-SA v0.3 Smoke Validation and Runtime Evidence

| Layer | File | Status | Purpose |
|---|---|---|---|
| Architecture Change | `docs/architecture_changes/geniusrouter_sa_v0_3_smoke_validation.md` | active | Records smoke validation layer. |
| Release Note | `docs/release_notes/v0_3_smoke_validation.md` | active | Records the v0.3 checkpoint. |
| Validation Surface | `docs/validation/validation_surface_v0_3.md` | active | Defines valid and invalid v0.3 claims. |
| Smoke Runner | `scripts/release/run_smoke_validation_v0_3.py` | active | Emits local smoke validation report. |
| Smoke Report | `reports/smoke/latest_smoke_validation_report.json` | active | Latest endpoint/routing evidence report. |

Boundary: v0.3 validates endpoint smoke behavior and routing-record emission only. It does not prove routing quality, cost savings, or production readiness.
## GeniusRouter-SA v0.3.1 Debug Routing Metadata Repair

| Layer | File | Status | Purpose |
|---|---|---|---|
| Architecture Change | `docs/architecture_changes/geniusrouter_sa_v0_3_1_debug_routing_metadata_repair.md` | active | Records debug metadata repair. |
| Release Note | `docs/release_notes/v0_3_1_debug_routing_metadata_repair.md` | active | Records v0.3.1 smoke repair. |
| Repair Script | `scripts/release/repair_geniusrouter_sa_v0_3_1_debug_metadata.ps1` | active | Applies the v0.3.1 repair. |

Boundary: v0.3.1 repairs local debug metadata validation. It does not prove routing quality, cost savings, or production readiness.
## GeniusRouter-SA v0.3.2 Runtime Debug Metadata Repair

| Layer | File | Status | Purpose |
|---|---|---|---|
| Architecture Change | `docs/architecture_changes/geniusrouter_sa_v0_3_2_runtime_debug_metadata_repair.md` | active | Records actual runtime debug metadata repair. |
| Release Note | `docs/release_notes/v0_3_2_runtime_debug_metadata_repair.md` | active | Records v0.3.2 repair. |
| Validation Report | `reports/validation/geniusrouter_sa_v0_3_2_validation.json` | active | Records passing v0.3.2 validation. |
| Repair Script | `scripts/release/repair_geniusrouter_sa_v0_3_2_runtime_debug_metadata.ps1` | active | Applies the v0.3.2 repair. |

Boundary: v0.3.2 repairs local debug metadata validation. It does not prove routing quality, cost savings, or production readiness.
## GeniusRouter-SA v0.4 RCC-N Repository Navigation Injection

| Layer | File | Status | Purpose |
|---|---|---|---|
| RCC-N Architecture | `docs/software_architecture/geniusrouter_sa_v0_4_rcc_n_injection.md` | active | Defines RCC-N injection architecture. |
| RCC Nexus Index | `docs/context/rcc_nexus_index.json` | active | Machine-readable Nexus index. |
| Route Map | `rcc/nexus/route_map.json` | active | Task-to-surface navigation map. |
| RCC Checker | `scripts/rcc/check_rcc_nexus.py` | active | Validates RCC-N surfaces and mini READMEs. |
| RCC Report | `reports/rcc_nexus/latest_rcc_nexus_check.json` | active | Latest RCC-N checker result. |

Boundary: v0.4 improves navigation and AI-agent orientation. It does not prove routing correctness, production readiness, cost savings, or AI understanding.
## GeniusRouter-SA v0.4.1 Validation Compatibility Repair

| Layer | File | Status | Purpose |
|---|---|---|---|
| Architecture Change | `docs/architecture_changes/geniusrouter_sa_v0_4_1_validation_compatibility_repair.md` | active | Records v0.4.1 historical-test compatibility repair. |
| Release Note | `docs/release_notes/v0_4_1_validation_compatibility_repair.md` | active | Records the v0.4.1 repair checkpoint. |
| Validation Report | `reports/validation/geniusrouter_sa_v0_4_1_validation.json` | active | Records passing v0.4.1 validation. |
| Repair Script | `scripts/release/repair_geniusrouter_sa_v0_4_1_validation_compatibility.ps1` | active | Applies v0.4.1 repair. |

Boundary: v0.4.1 repairs validation compatibility. It does not prove routing correctness, production readiness, cost savings, or AI understanding.
## GeniusRouter-SA v0.4.2 README / RCC-N Alignment

| Layer | File | Status | Purpose |
|---|---|---|---|
| Root README | `README.md` | active | Human / RCC Nexus / AI Agent trisection. |
| Quick README | `README_5_MINUTES.md` | active | Short adoption compression. |
| Repository Context | `docs/context/repository_context_index.json` | active | Current repository context index. |
| RCC Nexus Index | `docs/context/rcc_nexus_index.json` | active | Current RCC-N index. |
| Release Note | `docs/release_notes/v0_4_2_readme_rcc_n_alignment.md` | active | Records v0.4.2 README/RCC-N alignment. |
| Architecture Change | `docs/architecture_changes/geniusrouter_sa_v0_4_2_readme_rcc_n_alignment.md` | active | Records README/RCC-N alignment change. |
| Validation Surface | `docs/validation/validation_surface_v0_4_2.md` | active | Defines v0.4.2 validation boundaries. |

Boundary: v0.4.2 improves navigation and README completeness. It does not prove routing correctness, production readiness, cost savings, provider reliability, security, patch safety, or AI understanding.