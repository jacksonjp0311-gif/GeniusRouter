# GeniusRouter in 5 Minutes

## What this repo is

GeniusRouter is a FastAPI/OpenAI-compatible LLM router scaffold. Its core idea is to route prompts to low, medium, or high model tiers instead of sending every request to the strongest or most expensive model.

## Current state

Current governed layer:

```text
GeniusRouter-SA v0.4 — RCC-N Repository Navigation Injection
```

Runtime state before RCC-N:

```text
GeniusRouter-SA v0.3.2
18 tests OK
health smoke validation passed
chat endpoint smoke validation passed
routing decision record emitted
debug routing metadata present
```

## What this repo is not

- Not production ready.
- Not benchmark-validated.
- Not proof of cost savings.
- Not proof of routing quality.
- Not proof of classifier accuracy.
- Not proof of provider reliability.
- Not proof that RCC-N validates code correctness.

## Where to start

1. Read `README.md`.
2. Read `docs/context/repository_context_index.json`.
3. Read `docs/context/rcc_nexus_index.json`.
4. Read `rcc/nexus/route_map.json`.
5. Read the target folder README.
6. Run validation.

## Current validation

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