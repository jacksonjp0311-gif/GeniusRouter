# GeniusRouter-SA v0.2 Architecture Change
## Runtime Hardening Scaffold

## Change Type

Runtime structure hardening.

## What Changed

- Added Python package layout under `src/geniusrouter/`.
- Preserved the original runtime as `src/legacy_main_v0_1.py`.
- Kept `src/main.py` as compatibility entrypoint for existing Docker/uvicorn usage.
- Added typed config validation.
- Added deterministic SHA256 cache key utility.
- Added semantic/classifier tier merge policy.
- Added routing decision schema.
- Added routing decision JSONL writer.
- Added first unit tests.
- Added `pyproject.toml`.

## Runtime Impact

The router now has a structured internal package and evidence-ready routing decision contract.

## Boundary

This layer improves runtime structure. It does not prove routing quality, cost savings, production readiness, provider reliability, or benchmark validity.