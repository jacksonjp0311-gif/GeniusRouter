# GeniusRouter-SA v0.3 - Smoke Validation and Runtime Evidence

## Summary

v0.3 adds endpoint smoke validation and routing evidence verification.

## Added

- `tests/test_smoke_validation_v0_3.py`
- `tests/test_docs_v0_3.py`
- `scripts/release/run_smoke_validation_v0_3.py`
- `reports/smoke/latest_smoke_validation_report.json`
- `reports/smoke/latest_smoke_validation_report.md`
- `docs/architecture_changes/geniusrouter_sa_v0_3_smoke_validation.md`
- `docs/release_notes/v0_3_smoke_validation.md`
- `docs/validation/validation_surface_v0_3.md`

## Boundary

v0.3 validates endpoint behavior and routing-decision artifact emission with mocked provider calls. It does not prove routing quality or provider reliability.