# GeniusRouter: Evidence-Governed LLM Routing Runtime

## Repository Description

GeniusRouter is an OpenAI-compatible FastAPI LLM routing scaffold for sending requests to low, medium, or high model tiers instead of defaulting every prompt to the largest or most expensive model.

This repo currently combines three layers:

1. **GeniusRouter runtime**: FastAPI app, OpenAI-compatible `/v1/chat/completions` endpoint, config-first model routing, typed config validation, tier merge policy, stable SHA256 cache keys, provider abstraction, smoke validation, and routing-decision evidence.
2. **RCC-N navigation**: Human Director Box, README trisection, repository sphere, route maps, Echo Location records, Nexus context index, folder-level mini READMEs, and validation-bound AI operating protocol.
3. **Codex documentation shell**: software architecture, architecture-change records, validation surfaces, release notes, non-claim locks, and repo-governance traceability.

Boundary: this description improves discoverability and maintenance discipline. It does not prove routing correctness, benchmark validity, production readiness, security, patch safety, cost savings, provider reliability, classifier accuracy, or AI understanding.

> GeniusRouter is being evolved into an evidence-governed LLM router: cheap when possible, strong when necessary, observable always, bounded in claims.

Important attribution boundary: GeniusRouter began as Keith / keithofaptos' router vision. This repository enhancement preserves that origin while adding Codex/RCC-N architecture, tests, validation surfaces, and navigation structure.

---

## Human Director Box

### What is this?

GeniusRouter is a local-first LLM routing workbench. It tests whether an OpenAI-compatible proxy can inspect an incoming chat request, classify routing complexity, select a low / medium / high model tier, call a configured provider, and emit routing evidence without overclaiming production readiness.

### What changed?

This update performs the main README and mini README alignment after RCC-N injection.

The repo now has:

- PART I - Human README
- PART II - RCC Nexus README
- PART III - AI Agent README
- folder-level mini READMEs with RCC Nexus Echo Location blocks
- `docs/context/repository_context_index.json`
- `docs/context/rcc_nexus_index.json`
- `rcc/nexus/route_map.json`
- `scripts/rcc/check_rcc_nexus.py`

### Current health snapshot

| Surface | Current result |
|---|---:|
| Package / app | `geniusrouter` |
| Primary runtime entrypoint | `src/main.py` |
| Primary runtime package | `src/geniusrouter/` |
| Current software layer | GeniusRouter-SA v0.4.2 |
| Latest alignment patch | README / RCC-N root alignment and mini README refresh |
| Original vision attribution | Keith / keithofaptos preserved |
| Runtime scaffold | FastAPI OpenAI-compatible router |
| Routing tiers | low / medium / high |
| Config validation | present |
| Stable cache key | SHA256 utility present |
| Routing decision schema | present |
| Routing telemetry writer | present |
| Legacy runtime snapshot | `src/legacy_main_v0_1.py` |
| Compatibility entrypoint | preserved |
| RCC-N checker | passed in v0.4.1 |
| Mini README coverage | 21 / 21 indexed folders |
| NCI mode | self |
| NCI target | 1.0 |
| Unit tests | 21 OK in v0.4.1 |
| Smoke validation | passed in v0.4.1 |
| Routing records emitted | 1 in latest smoke validation |
| Debug routing metadata | present |
| Claim status | locally smoke-validated scaffold |
| Production readiness | not claimed |
| Cost savings | not benchmark-claimed |
| Provider reliability | not claimed |
| Current route map | `rcc/nexus/route_map.json` |
| Current RCC-N report | `reports/rcc_nexus/latest_rcc_nexus_check.json` |
| Current validation report | `reports/validation/geniusrouter_sa_v0_4_1_validation.json` |

### What this is not

- Not production ready.
- Not benchmark-validated.
- Not proof of cost savings.
- Not proof of routing quality.
- Not proof of classifier accuracy.
- Not proof of provider reliability.
- Not proof of security.
- Not proof of patch safety.
- Not proof that RCC-N validates code correctness.
- Not proof that AI understands the repository.
- Not a replacement for tests, smoke validation, benchmark evidence, or provider integration testing.

### Where do I start?

1. Read this README.
2. Open `README_5_MINUTES.md`.
3. Open `docs/context/repository_context_index.json`.
4. Open `docs/context/rcc_nexus_index.json`.
5. Open `rcc/nexus/route_map.json`.
6. Read the target folder README before editing.
7. Run `python scripts/rcc/check_rcc_nexus.py`.
8. Run `python -m unittest discover -s tests`.
9. Run `python scripts/release/run_smoke_validation_v0_3.py`.

---

# PART I - Human README

## Current Identity

GeniusRouter is a local Python/FastAPI reference runtime for testing whether a routing proxy can:

- expose an OpenAI-compatible `/v1/chat/completions` endpoint,
- load a model-tier configuration,
- validate runtime config,
- extract prompt text from OpenAI-style messages,
- compute a semantic route,
- compute or mock a classifier route,
- merge low / medium / high tier decisions,
- select a configured model,
- compute stable SHA256 cache keys,
- write routing decision evidence,
- run endpoint smoke validation,
- expose repository navigation through RCC-N,
- preserve non-claim boundaries.

The current repo is a governed scaffold. It is not a production LLM gateway.

## Quick Start

Set the local package path:

```powershell
$env:PYTHONPATH = "$PWD\src"
```

Run tests:

```powershell
python -m unittest discover -s tests
```

Run RCC-N checker:

```powershell
python scripts/rcc/check_rcc_nexus.py
```

Run smoke validation:

```powershell
python scripts/release/run_smoke_validation_v0_3.py
```

Run locally with Uvicorn:

```powershell
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000
```

Health endpoint:

```text
GET /health
```

Chat endpoint:

```text
POST /v1/chat/completions
```

## What GeniusRouter Tests

| Surface | Purpose |
|---|---|
| config validation | Confirms `config.yaml` has required routing tiers. |
| tier routing | Tests low / medium / high routing primitives. |
| merge policy | Prevents obvious under-routing when one signal indicates higher complexity. |
| stable cache key | Replaces process-unstable Python `hash()` behavior with SHA256. |
| routing decision schema | Makes routing evidence explicit. |
| smoke validation | Confirms endpoint path can emit a routing record with mocked provider. |
| RCC-N checker | Confirms navigation surfaces and mini READMEs exist. |

GeniusRouter rewards bounded evidence emission, not confident overclaiming.

## Current Hardening Layer

The current hardening layer includes:

- source-preserving attribution,
- full software architecture document,
- typed config validation,
- structured runtime package,
- compatibility entrypoint,
- legacy runtime preservation,
- stable cache-key utility,
- routing decision schema,
- routing telemetry writer,
- smoke validation runner,
- RCC-N repository navigation,
- 21 mini READMEs with Echo Location blocks,
- route map,
- context indexes,
- validation compatibility repair.

## Project Structure

```text
GeniusRouter/
  README.md
  README_5_MINUTES.md
  pyproject.toml
  config.yaml
  Dockerfile
  docker-compose.yml
  requirements.txt
  CONTRIBUTORS.md
  LICENSE

  docs/
    DOCS_REGISTRY.md
    README.md
    software_architecture/
    architecture_changes/
    release_notes/
    protocols/
    context/
    roadmap/
    validation/

  rcc/
    README.md
    nexus/
      README.md
      rcc_nexus_protocol.md
      route_map.json

  scripts/
    README.md
    rcc/
      check_rcc_nexus.py
    release/
      run_smoke_validation_v0_3.py
      repair scripts and release scripts

  src/
    README.md
    main.py
    legacy_main_v0_1.py
    geniusrouter/
      config.py
      routing.py
      cache.py
      schemas.py
      telemetry.py
      providers.py
      main.py

  tests/
    README.md
    test_config.py
    test_routing.py
    test_cache_key.py
    test_routing_decision.py
    test_runtime_boundaries.py
    test_smoke_validation_v0_3.py
    test_docs_v0_3.py
    test_rcc_n_v0_4.py

  reports/
    README.md
    validation/
    smoke/
    rcc_nexus/

  artifacts/
    README.md
    routing_decisions/
```

## Project Structure Director

| Surface | What it does | Why it matters |
|---|---|---|
| `README.md` | Human / RCC Nexus / AI Agent root map. | Reduces orientation ambiguity. |
| `README_5_MINUTES.md` | Short adoption compression. | Gives quick start and current boundary. |
| `docs/context/` | Stores repository context and RCC Nexus indexes. | Main machine-readable self-description layer. |
| `docs/software_architecture/` | Stores GeniusRouter-SA architecture documents. | Keeps theory-to-software evolution explicit. |
| `docs/protocols/` | Stores AI contract, non-claim locks, and routing evidence contracts. | Prevents overclaiming and blind edits. |
| `rcc/nexus/` | Stores route map and Nexus protocol. | Makes the repo agent-navigable. |
| `scripts/rcc/` | Stores RCC-N checker. | Enforces navigation surface integrity. |
| `scripts/release/` | Stores release and repair automation. | Preserves executable continuity. |
| `src/geniusrouter/` | Stores the structured runtime implementation. | Contains config, routing, cache, schemas, telemetry, provider wrapper, and app. |
| `tests/` | Stores implementation-health and navigation tests. | Catches scaffold regressions. |
| `reports/` | Stores validation, smoke, and RCC-N reports. | Makes evidence visible. |
| `artifacts/routing_decisions/` | Stores runtime routing decision ledger output. | Makes routing behavior inspectable. |

## Structure Reading Route

For humans:

1. Read Human Director Box.
2. Read Project Structure Director.
3. Open `README_5_MINUTES.md`.
4. Open `docs/context/repository_context_index.json`.
5. Run validation commands.

For AI agents:

1. Read this README.
2. Read `README_5_MINUTES.md`.
3. Read `docs/context/repository_context_index.json`.
4. Read `docs/context/rcc_nexus_index.json`.
5. Read `rcc/nexus/route_map.json`.
6. Read the target folder README.
7. Inspect source/tests/evidence before patching.
8. Run declared validation.
9. Update RCC-N surfaces if geometry changed.

Structure boundary: project structure improves navigation. It does not prove correctness, security, patch safety, AI understanding, benchmark validity, production readiness, cost savings, or provider reliability.

## Evidence Artifacts

Routing decisions are written under:

```text
artifacts/routing_decisions/
```

Validation reports are written under:

```text
reports/validation/
```

Smoke reports are written under:

```text
reports/smoke/
```

RCC-N reports are written under:

```text
reports/rcc_nexus/
```

## Non-Claim Locks

GeniusRouter is:

- not production ready,
- not benchmark validated,
- not proof of routing optimality,
- not proof of cost savings,
- not proof of provider reliability,
- not proof of classifier accuracy,
- not proof of security,
- not proof of patch safety,
- not proof that documentation equals runtime truth,
- not proof that RCC-N navigation validates code correctness.

---

# PART II - RCC Nexus README

## RCC Nexus Identity

GeniusRouter includes a local RCC Nexus layer.

```text
RCC tells the agent what the repository means.
RCC-N tells the agent where it is.
Validation tells the agent whether reality agreed.
```

## Repository Sphere

| Shell | Name | Meaning |
|---|---|---|
| `center` | Invariant Core | Attribution, source boundary, non-claim locks, API-key secrecy, routing-evidence laws. |
| `inner` | Runtime Primitives | `src/geniusrouter/`, config validation, routing, cache, schema, telemetry, provider abstraction. |
| `middle` | Processes | tests, release scripts, smoke runner, RCC checker, validation commands. |
| `outer` | Evidence / Reflection | docs, reports, artifacts, route maps, validation reports, release notes. |

## Nexus Meridians

- source
- runtime
- validation
- evidence
- safety
- agent
- release
- documentation

## Nexus Sectors

- runtime-core
- config
- routing
- cache
- telemetry
- provider
- validation
- reports
- artifacts
- rcc
- docs
- release

## Primary Nexus Files

- `docs/context/repository_context_index.json`
- `docs/context/rcc_nexus_index.json`
- `rcc/nexus/route_map.json`
- `rcc/nexus/README.md`
- `rcc/nexus/rcc_nexus_protocol.md`
- `scripts/rcc/check_rcc_nexus.py`
- `reports/rcc_nexus/latest_rcc_nexus_check.json`
- `reports/rcc_nexus/latest_rcc_nexus_check.md`

## Nexus Context Integrity

Current NCI mode: `self`.

Current NCI target: `1.0`.

Current mini README coverage target: indexed folders.

Current checked mini READMEs: `21`.

NCI is not code quality proof.

## RCC Nexus Echo Location

Sphere Position:

- Shell: center
- Meridian(s): source, safety, agent, runtime, evidence
- Sector: rcc
- Version / TTL: GeniusRouter-SA-v0.4.2 / 180 days
- Last Verified: 2026-05

Local Role:

- Root orientation surface for humans, RCC Nexus navigation, and AI agents.

Inbound Hooks:

- GitHub repository page
- local PowerShell evolution scripts
- GeniusRouter-SA software architecture

Outbound Hooks:

- README_5_MINUTES.md
- docs/context/repository_context_index.json
- docs/context/rcc_nexus_index.json
- rcc/nexus/route_map.json
- src/geniusrouter/
- tests/
- reports/
- artifacts/routing_decisions/

Evidence Surface:

- reports/validation/
- reports/smoke/
- reports/rcc_nexus/
- artifacts/routing_decisions/

Validation Surface:

- python scripts/rcc/check_rcc_nexus.py
- python -m unittest discover -s tests
- python scripts/release/run_smoke_validation_v0_3.py

Claim Boundary:

- README quality, RCC-N geometry, route maps, reports, and NCI do not prove code correctness, security, patch safety, AI understanding, benchmark validity, production readiness, routing quality, or provider reliability.

Non-Claim Locks:

- geometry_is_not_ai_internal_proof
- nci_is_not_code_quality_proof
- navigation_is_not_validation
- context_reconstruction_is_not_correctness_proof
- validation_remains_required
- routing_decision_is_not_optimality_proof
- smoke_validation_is_not_production_readiness

Agent Route:

- Read README.md, README_5_MINUTES.md, docs/context/repository_context_index.json, docs/context/rcc_nexus_index.json, rcc/nexus/route_map.json, then the target folder README before editing.

Update Obligation:

- Update README, RCC context, Nexus index, route maps, reports, and Echo Location records when project identity, validation commands, evidence paths, claim boundaries, or repository geometry changes.

## RCC Nexus Reports

| Artifact | Purpose |
|---|---|
| `reports/rcc_nexus/latest_rcc_nexus_check.json` | Machine-readable RCC-N checker snapshot. |
| `reports/rcc_nexus/latest_rcc_nexus_check.md` | Human-readable RCC-N checker report. |

## RCC Nexus Non-Claim Lock

RCC-N improves navigation, traceability, maintenance discipline, and agent self-location. It does not prove code correctness, security, AI understanding, patch safety, production readiness, benchmark validity, cost savings, provider reliability, or runtime truth.

Geometry is not correctness.

Navigation is not validation.

Context is not truth.

---

# PART III - AI Agent README

## AI Version Tracking Contract

Current repository context:

- Repository: GeniusRouter
- Purpose: evidence-governed LLM routing scaffold and OpenAI-compatible model-tier proxy.
- Current runtime layer: GeniusRouter-SA v0.3.2 smoke-validated runtime scaffold.
- Current software architecture layer: GeniusRouter-SA v0.4.2 README / RCC-N alignment.
- Primary package: `geniusrouter`.
- Current classification: locally smoke-validated scaffold only.
- Current non-claim boundary: local scaffold evidence only, not production readiness.
- RCC mode: Repository Context Canon style docs plus mini READMEs.
- RCC-N mode: local geometric repository navigation shell with route maps and Echo Location blocks.
- Runtime behavior changed by v0.4.2: no.
- Documentation/navigation changed by v0.4.2: yes.

## AI Operating Contract

Any AI agent reading or modifying this repository must follow this order:

1. Read the Human Director Box.
2. Read PART I - Human README.
3. Read PART II - RCC Nexus README.
4. Read PART III - AI Agent README.
5. Read `README_5_MINUTES.md`.
6. Read `docs/context/repository_context_index.json`.
7. Read `docs/context/rcc_nexus_index.json`.
8. Read `rcc/nexus/route_map.json`.
9. Read the mini README in the target folder.
10. Inspect only relevant source, tests, docs, scripts, reports, or artifacts.
11. Patch the smallest necessary surface.
12. Run relevant validation commands before claiming behavior changed.
13. Update README, RCC, RCC-N, reports, and Echo Location records if geometry or evidence changed.

## AI README Update Policy

When the repository versions, the AI agent must update the root README in all required zones. Do not update only the top dashboard.

Required root README update zones:

| Zone | Section | Required update |
|---|---|---|
| 1 | Human Director Box / Current health snapshot | Current software layer, latest patch, tests, validation status. |
| 2 | PART I - Human README | Current identity, quick start, project structure, evidence artifacts. |
| 3 | PART II - RCC Nexus README | Current RCC-N layer, route map, NCI, Echo Location, Nexus reports. |
| 4 | PART III - AI Agent README | Current software architecture layer, runtime status, read order, validation commands. |
| 5 | Theory / Software Architecture / Injections Registry | Current file rows and documentation lanes. |
| 6 | Current Versioned Documentation Stack | Active architecture, prior architecture, release notes, reports. |
| 7 | Current Architecture Chain | Append the new version in sequence. |
| 8 | Bottom historical lineage | Add a section for the completed version, not only a one-line extension. |
| 9 | Validation commands | Update commands if validation surface changed. |
| 10 | Boundary / non-claim locks | Preserve or strengthen boundaries; never weaken them. |

AI update rule:

```text
Top dashboard without bottom lineage is incomplete.
Bottom lineage without current health is stale.
Current version without documentation-stack update is drift.
README completion requires current state, registry state, and historical lineage.
```

Before claiming README completion, run:

```powershell
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
python scripts/release/run_smoke_validation_v0_3.py
```

Boundary: this policy improves AI repository navigation and README maintenance. It does not prove code correctness, routing quality, production readiness, AI understanding, provider reliability, cost savings, or benchmark validity.

## AI File Routing Guide

- `src/geniusrouter/`: executable runtime package.
- `src/geniusrouter/config.py`: typed config validation.
- `src/geniusrouter/routing.py`: prompt extraction, semantic routing, tier merge, model selection.
- `src/geniusrouter/cache.py`: SHA256 cache key helper.
- `src/geniusrouter/schemas.py`: routing decision schema.
- `src/geniusrouter/telemetry.py`: routing decision JSONL writer.
- `src/geniusrouter/providers.py`: provider call wrapper.
- `src/geniusrouter/main.py`: FastAPI runtime app.
- `src/main.py`: compatibility entrypoint.
- `tests/`: implementation-health validation.
- `scripts/rcc/`: RCC-N checker.
- `scripts/release/`: release, smoke, and repair scripts.
- `docs/context/`: repository context and RCC Nexus indexes.
- `docs/software_architecture/`: software architecture shell.
- `docs/protocols/`: AI and non-claim protocols.
- `rcc/nexus/`: RCC-N protocol and route map.
- `reports/`: validation, smoke, and RCC-N reports.
- `artifacts/routing_decisions/`: routing decision ledger output.

## AI Non-Claim Lock

Never claim or imply:

- GeniusRouter is production ready.
- GeniusRouter routing is optimal.
- GeniusRouter cost savings are proven.
- GeniusRouter classifier accuracy is proven.
- GeniusRouter provider reliability is proven.
- Smoke validation proves production readiness.
- Routing decisions prove optimality.
- RCC-N navigation proves code correctness.
- NCI proves code quality.
- Documentation proves runtime truth.
- LLM fluency should be confused with source-grounded implementation accuracy.

## Required Local Verification

After README, RCC, or RCC-N changes, run:

```powershell
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
python scripts/release/run_smoke_validation_v0_3.py
```

After source/runtime changes, also inspect:

```text
src/geniusrouter/
tests/
reports/validation/
reports/smoke/
artifacts/routing_decisions/
```

## Done Criteria

A change is not complete until:

- source attribution is preserved,
- non-claim locks are preserved,
- target folder README remains accurate,
- RCC/Nexus index remains accurate,
- validation commands ran,
- evidence paths are updated if outputs changed,
- claims remain inside evidence boundaries.

## Exact RCC-N Checker Non-Claim Markers

These markers are intentionally preserved:

- Navigation is not validation
- Context is not truth
- RCC-N is not code correctness
- Smoke validation is not production readiness
- Routing decision is not optimality proof

---

## Theory / Software Architecture / Injections Registry

### Documentation Separation Rule

The documentation shell is intentionally separated into distinct lanes:

| Lane | Path | Purpose |
|---|---|---|
| Software Architecture | `docs/software_architecture/` | Current executable software architecture. |
| Architecture Changes | `docs/architecture_changes/` | Versioned architecture and repository-structure changes. |
| Release Notes | `docs/release_notes/` | Version continuity and release records. |
| Protocols | `docs/protocols/` | AI operating contract, non-claim locks, routing evidence contracts. |
| Context | `docs/context/` | Repository context index and RCC Nexus index. |
| Validation | `docs/validation/` | Versioned validation surfaces. |
| RCC Nexus | `rcc/nexus/` | Route map, RCC-N protocol, and Nexus README. |
| Reports | `reports/` | Validation, smoke, and RCC-N reports. |
| Artifacts | `artifacts/` | Runtime evidence outputs. |

Rule: do not mix runtime changes with documentation-only injections unless the architecture change says so.

### Current Versioned Documentation Stack

| Layer | Current file | Status | Notes |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/geniusrouter_sa_v0_4_rcc_n_injection.md` | active | RCC-N repository navigation injection. |
| Prior Software Architecture | `docs/software_architecture/geniusrouter_sa_v0_1_full_software_architecture.md` | active | Full structural runtime architecture and governance genesis layer. |
| Docs Registry | `docs/DOCS_REGISTRY.md` | active | Canonical map of architecture, releases, validation, and RCC-N surfaces. |
| RCC Nexus Index | `docs/context/rcc_nexus_index.json` | active | Machine-readable RCC-N index. |
| Repository Context Index | `docs/context/repository_context_index.json` | active | Machine-readable repository context. |
| Route Map | `rcc/nexus/route_map.json` | active | Task-to-surface navigation map. |
| RCC Checker | `scripts/rcc/check_rcc_nexus.py` | active | Validates RCC-N required files and mini READMEs. |
| v0.4.1 Repair | `docs/release_notes/v0_4_1_validation_compatibility_repair.md` | active | Repairs historical test/current-layer compatibility. |
| v0.4.2 README Alignment | `docs/release_notes/v0_4_2_readme_rcc_n_alignment.md` | active | Main README and mini README alignment. |
| Current RCC-N Report | `reports/rcc_nexus/latest_rcc_nexus_check.json` | active | Latest RCC-N checker report. |
| Current Validation Report | `reports/validation/geniusrouter_sa_v0_4_1_validation.json` | active | Latest passing validation report before v0.4.2. |

### Current Architecture Chain

Original GeniusRouter router seed -> GeniusRouter-SA v0.1 full software architecture docs -> GeniusRouter-SA v0.2 runtime hardening scaffold -> GeniusRouter-SA v0.3 smoke validation evidence layer -> GeniusRouter-SA v0.3.1 debug metadata repair attempt -> GeniusRouter-SA v0.3.2 runtime debug metadata path repair -> GeniusRouter-SA v0.4 RCC-N navigation injection -> GeniusRouter-SA v0.4.1 validation compatibility repair -> GeniusRouter-SA v0.4.2 README / RCC-N alignment.

### Version Update Obligation

Every future version must update this registry section when any of the following changes:

- software architecture layer,
- runtime behavior,
- evidence schema,
- validation commands,
- RCC-N route maps,
- mini README coverage,
- docs registry,
- claim boundaries,
- source attribution,
- release status,
- smoke validation behavior,
- routing decision behavior,
- old tests that freeze current-state assumptions.

### Boundary

This registry improves documentation continuity and agent navigation.

It does not prove code correctness, routing correctness, cost savings, provider reliability, production readiness, security, patch safety, or AI understanding.

---

## GeniusRouter-SA v0.1 Full Software Architecture Docs

v0.1 created the first governed software architecture and traceability layer.

Added:

| Layer | Path | Purpose |
|---|---|---|
| v0.1 architecture | `docs/software_architecture/geniusrouter_sa_v0_1_full_software_architecture.md` | Defines structural runtime architecture and governance genesis layer. |
| Architecture change | `docs/architecture_changes/geniusrouter_sa_v0_1_docs_architecture_injection.md` | Records docs architecture injection. |
| Release note | `docs/release_notes/v0_1_docs_architecture_injection.md` | Records v0.1 checkpoint. |
| Docs registry | `docs/DOCS_REGISTRY.md` | Records documentation surfaces. |

v0.1 law:

```text
No routing claim without routing evidence.
No cost claim without benchmark evidence.
No production claim without tests.
```

Boundary: v0.1 created architecture docs only. It did not prove runtime correctness.

---

## GeniusRouter-SA v0.2 Runtime Hardening Scaffold

v0.2 moved the repo from a single-file prototype toward a structured runtime package.

Added:

| Layer | Path | Purpose |
|---|---|---|
| Runtime package | `src/geniusrouter/` | Structured runtime modules. |
| Config validation | `src/geniusrouter/config.py` | Validates routing config. |
| Routing module | `src/geniusrouter/routing.py` | Extracts prompt, routes tier, merges decisions. |
| Cache module | `src/geniusrouter/cache.py` | Stable SHA256 cache key. |
| Schemas | `src/geniusrouter/schemas.py` | Routing decision schema. |
| Telemetry | `src/geniusrouter/telemetry.py` | JSONL routing decision writer. |
| Provider wrapper | `src/geniusrouter/providers.py` | Provider call abstraction. |
| Tests | `tests/` | First validation suite. |

v0.2 law:

```text
No cache claim without stable keys.
No implementation-health claim without passing tests.
```

Boundary: v0.2 improved structure. It did not prove routing quality or production readiness.

---

## GeniusRouter-SA v0.3 Smoke Validation Evidence Layer

v0.3 added endpoint smoke validation and routing evidence verification.

Added:

| Layer | Path | Purpose |
|---|---|---|
| Smoke test | `tests/test_smoke_validation_v0_3.py` | Tests health and chat endpoint with mocked provider. |
| Smoke runner | `scripts/release/run_smoke_validation_v0_3.py` | Emits latest smoke validation report. |
| Smoke report | `reports/smoke/latest_smoke_validation_report.json` | Machine-readable smoke result. |
| Docs test | `tests/test_docs_v0_3.py` | Checks v0.3 documentation surface. |

v0.3 law:

```text
No router-health claim without endpoint smoke validation.
No routing-evidence claim without artifact validation.
```

Boundary: v0.3 proved local smoke behavior only.

---

## GeniusRouter-SA v0.3.2 Runtime Debug Metadata Repair

v0.3.2 repaired the actual runtime path so `_geniusrouter.routing_decision` appears in local/debug responses when `GENIUSROUTER_DEBUG_ROUTING=true`.

Root lesson:

```text
PowerShell Set-Location is not always enough when using .NET file APIs.
Use absolute paths or synchronize .NET current directory.
```

Boundary: v0.3.2 repaired local debug metadata. It did not prove routing quality.

---

## GeniusRouter-SA v0.4 RCC-N Navigation Injection

v0.4 injected RCC-N repository navigation.

Added:

| Layer | Path | Purpose |
|---|---|---|
| RCC-N architecture | `docs/software_architecture/geniusrouter_sa_v0_4_rcc_n_injection.md` | Defines RCC-N injection. |
| RCC Nexus index | `docs/context/rcc_nexus_index.json` | Machine-readable Nexus index. |
| Route map | `rcc/nexus/route_map.json` | Task-to-surface navigation. |
| RCC checker | `scripts/rcc/check_rcc_nexus.py` | Validates RCC-N files and mini READMEs. |
| Mini READMEs | indexed folders | Folder-level Echo Location blocks. |

v0.4 law:

```text
No AI-agent navigation claim without mini READMEs, route maps, context index, checker, and validation.
```

Boundary: v0.4 improves navigation. It does not prove code correctness.

---

## GeniusRouter-SA v0.4.1 Validation Compatibility Repair

v0.4.1 repaired a historical test freeze after v0.4.

The older v0.3 docs test expected the active context layer to remain exactly `GeniusRouter-SA v0.3`. v0.4.1 updated that historical test so it can preserve lineage while allowing the active context index to advance.

v0.4.1 law:

```text
Historical tests validate lineage.
Current indexes validate active state.
Do not freeze current-state fields inside historical tests.
```

Boundary: v0.4.1 repairs validation compatibility. It does not prove routing quality or production readiness.

---

## GeniusRouter-SA v0.4.2 README / RCC-N Alignment

v0.4.2 overhauls the root README into the full RCC-N trisection pattern and refreshes folder-level mini READMEs.

Added / updated:

| Surface | Purpose |
|---|---|
| Human Director Box | Shows current state and start path. |
| PART I - Human README | Human-facing usage, structure, and evidence surfaces. |
| PART II - RCC Nexus README | Repository sphere, meridians, route map, NCI, Echo Location. |
| PART III - AI Agent README | Agent operating contract, file routing, update policy, done criteria. |
| Current Versioned Documentation Stack | Keeps architecture and validation trace visible. |
| Historical lineage sections | Prevents top-only README drift. |
| Mini README refresh | Aligns folder-level Echo Location blocks with v0.4.2. |

v0.4.2 law:

```text
Root README without trisection is incomplete after RCC-N injection.
Mini READMEs without current layer alignment create local context drift.
README completion requires current state, registry state, and historical lineage.
```

Boundary: v0.4.2 improves navigation and public comprehension. It does not prove routing quality, production readiness, cost savings, provider reliability, security, patch safety, or AI understanding.