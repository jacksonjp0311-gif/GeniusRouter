# GeniusRouter in 5 Minutes

## What this repo is

GeniusRouter is a FastAPI/OpenAI-compatible LLM router scaffold. Its core idea is to route prompts to low, medium, or high model tiers instead of sending every request to the strongest or most expensive model.

## Current layer

```text
GeniusRouter-SA v0.4.2 — README / RCC-N Alignment
```

## Current validated state

```text
RCC-N checker: passed in v0.4.1
Mini READMEs: 21 / 21 indexed folders
Unit tests: 21 OK in v0.4.1
Smoke validation: passed in v0.4.1
Routing records emitted: 1
Debug routing metadata: present
```

## Start here

1. `README.md`
2. `docs/context/repository_context_index.json`
3. `docs/context/rcc_nexus_index.json`
4. `rcc/nexus/route_map.json`
5. target folder `README.md`

## Validate

```powershell
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
python scripts/release/run_smoke_validation_v0_3.py
```

## Short law

```text
Cheap when possible.
Strong when necessary.
Observable always.
Bounded in claims.
```

## Boundary

This repo is a governed scaffold. It is not production ready, not benchmark-validated, and not proof of routing quality or cost savings.