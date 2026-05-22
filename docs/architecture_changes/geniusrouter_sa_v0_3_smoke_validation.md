# GeniusRouter-SA v0.3 Architecture Change
## Smoke Validation and Runtime Evidence Layer

## Change Type

Endpoint smoke validation and routing evidence verification.

## What Changed

- Added FastAPI TestClient smoke tests.
- Added mocked `/v1/chat/completions` provider test.
- Added verification that routing decisions are emitted to JSONL.
- Added optional debug routing metadata for local validation.
- Added smoke validation runner.
- Added latest smoke validation report outputs.
- Updated docs registry and context index.

## Runtime Impact

The router can now be tested locally without a real provider call by mocking provider execution. The route still exercises request parsing, tier selection, model selection, cache-key generation, routing decision construction, telemetry writing, and response return.

## Boundary

This layer proves local smoke validation and routing-record emission. It does not prove routing quality, cost savings, production readiness, provider reliability, classifier accuracy, or benchmark validity.