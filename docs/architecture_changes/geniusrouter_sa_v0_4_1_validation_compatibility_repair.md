# GeniusRouter-SA v0.4.1 Architecture Change
## Validation Compatibility Repair

## Change Type

Historical test compatibility repair.

## What Changed

- Repaired `tests/test_docs_v0_3.py`.
- Allowed `repository_context_index.json` to advance from v0.3 to v0.4 without breaking the historical docs test.
- Added a v0.4.1 validation report.
- Anchored this repair script.

## Why

v0.4 RCC-N checker passed and smoke validation passed, but unit tests failed because a v0.3 test froze the current layer string. Current-state fields must be allowed to advance while lineage tests preserve historical files.

## Boundary

This repair improves validation compatibility. It does not prove code correctness, routing quality, production readiness, cost savings, provider reliability, patch safety, or AI understanding.