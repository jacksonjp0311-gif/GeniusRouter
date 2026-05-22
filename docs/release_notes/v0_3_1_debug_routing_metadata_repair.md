# GeniusRouter-SA v0.3.1 — Debug Routing Metadata Repair

## Summary

v0.3.1 repairs the v0.3 smoke-validation layer so debug routing metadata is inserted into mocked local validation responses when `GENIUSROUTER_DEBUG_ROUTING=true`.

## Why

v0.3 correctly emitted a routing decision JSONL artifact, but the unit test also expected debug metadata in the response body. The smoke runner reported `debug_routing_metadata_present: false`, while still allowing status pass. This repair makes the validation stricter and aligns runtime behavior with the test contract.

## Boundary

This repair validates local debug metadata and routing-record emission. It does not prove routing quality, provider reliability, production readiness, cost savings, classifier accuracy, or benchmark validity.