# GeniusRouter RCC Nexus

## Identity

RCC-N is the repository navigation layer for GeniusRouter.

```text
RCC tells the agent what the repository means.
RCC-N tells the agent where it is.
Validation tells the agent whether reality agreed.
```

## Primary files

- `docs/context/repository_context_index.json`
- `docs/context/rcc_nexus_index.json`
- `rcc/nexus/route_map.json`
- `rcc/nexus/rcc_nexus_protocol.md`
- `scripts/rcc/check_rcc_nexus.py`

## Validation

```powershell
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
python scripts/release/run_smoke_validation_v0_3.py
```

## Boundary

RCC-N improves navigation and AI-agent orientation. It does not prove routing correctness, production readiness, security, patch safety, benchmark validity, cost savings, provider reliability, or AI understanding.

## RCC Nexus Echo Location

Sphere Position:
- Shell: outer
- Meridian(s): agent, documentation, validation, evidence
- Sector: rcc
- Version / TTL: GeniusRouter-SA-v0.4 / 180 days
- Last Verified: 2026-05

Local Role:
- Root RCC-N navigation surface.

Inbound Hooks:
- README.md
- README_5_MINUTES.md
- docs/context/repository_context_index.json

Outbound Hooks:
- rcc/nexus/route_map.json
- scripts/rcc/check_rcc_nexus.py
- docs/context/rcc_nexus_index.json

Evidence Surface:
- reports/rcc_nexus/latest_rcc_nexus_check.json
- reports/rcc_nexus/latest_rcc_nexus_check.md

Validation Surface:
- python scripts/rcc/check_rcc_nexus.py

Claim Boundary:
- Navigation is not validation.

Non-Claim Locks:
- rcc_n_is_not_code_correctness
- context_is_not_truth
- validation_remains_required

Agent Route:
- Read route map, target mini README, source/tests, then validate.

Update Obligation:
- Update this README when route maps, validation commands, indexed folders, or claim boundaries change.