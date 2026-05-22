# GeniusRouter Runtime Hardening Plan

## v0.2 Target

The next layer should modify runtime structure safely.

## Required Changes

1. Normalize package layout to `src/geniusrouter/`.
2. Add typed config validation with Pydantic.
3. Replace Python `hash()` cache key with SHA256.
4. Add graceful Redis fallback.
5. Define semantic/classifier merge policy.
6. Add routing decision records.
7. Add tests.
8. Preserve original FastAPI route compatibility.

## Boundary

Runtime hardening improves structure. It does not prove routing quality or cost savings without benchmarks.