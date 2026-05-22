# GeniusRouter-SA v0.4.1 — Validation Compatibility Repair

## Summary

v0.4.1 repairs the validation compatibility gap introduced by the RCC-N v0.4 injection.

## Root Cause

The RCC-N v0.4 injection correctly changed `docs/context/repository_context_index.json` to the current layer `GeniusRouter-SA v0.4`, but the older v0.3 docs test still required the current layer to remain exactly `GeniusRouter-SA v0.3`.

That is a historical-test freezing problem.

## What Changed

- `tests/test_docs_v0_3.py` now allows the current context index to report either the original v0.3 smoke layer or a newer v0.4 RCC-N layer.
- A v0.4.1 validation report is added only after validation passes.
- The repair preserves the v0.3 lineage while allowing active current-state progression.

## Boundary

This repair validates compatibility between historical tests and current RCC-N state. It does not prove routing quality, production readiness, cost savings, provider reliability, security, patch safety, or AI understanding.