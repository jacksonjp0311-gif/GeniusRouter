# GeniusRouter-SA v0.3.1 Architecture Change
## Debug Routing Metadata Repair

## Change Type

Smoke-validation repair.

## What Changed

- Runtime now inserts `_geniusrouter.routing_decision` into successful local/debug responses when `GENIUSROUTER_DEBUG_ROUTING=true`.
- Smoke runner now requires debug routing metadata when debug mode is enabled.
- v0.3.1 repair note added.

## Why

The v0.3 commit had one failing unit test before commit. Routing artifacts were emitted correctly, but the response body did not include debug metadata. This repair closes that gap.

## Boundary

This repair strengthens local validation. It does not prove routing optimality, provider reliability, production readiness, cost savings, or benchmark validity.