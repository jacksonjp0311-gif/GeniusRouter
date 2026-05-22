# GeniusRouter-SA v0.2 - Runtime Hardening Scaffold

## Summary

v0.2 starts the runtime hardening path after v0.1 established the full software architecture documentation layer.

## Added

- `src/geniusrouter/config.py`
- `src/geniusrouter/routing.py`
- `src/geniusrouter/cache.py`
- `src/geniusrouter/schemas.py`
- `src/geniusrouter/telemetry.py`
- `src/geniusrouter/providers.py`
- `src/geniusrouter/main.py`
- compatibility `src/main.py`
- first tests under `tests/`
- `pyproject.toml`

## Preserved

- Original runtime snapshot: `src/legacy_main_v0_1.py`
- Existing Docker command compatibility: `src.main:app`

## Boundary

This release does not prove production readiness or routing quality.