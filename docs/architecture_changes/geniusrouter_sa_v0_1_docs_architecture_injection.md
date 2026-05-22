# GeniusRouter-SA v0.1 Architecture Change
## Docs Architecture Injection

## Change Type

Documentation architecture, governance scaffold, and linear trace foundation.

## What Changed

This change adds the first Codex-style software architecture layer for GeniusRouter:

```text
docs/software_architecture/geniusrouter_sa_v0_1_full_software_architecture.md
```

It also adds the first documentation governance structure:

```text
docs/README.md
docs/DOCS_REGISTRY.md
docs/architecture_changes/
docs/release_notes/
docs/protocols/
docs/context/
docs/roadmap/
docs/validation/
```

## Why

The current GeniusRouter repository has a strong runtime idea but needs a traceable architecture and claim boundary before deeper runtime modification or RCC-N injection.

## Runtime Impact

None. This is a docs-only architecture checkpoint.

## Boundary

This change does not prove router correctness, production readiness, routing accuracy, cost savings, classifier accuracy, provider reliability, cache correctness, or RCC-N completion.

## Next Layer

GeniusRouter-SA v0.2 should harden runtime structure:

- package layout,
- typed config,
- stable SHA256 cache key,
- graceful Redis fallback,
- routing decision contract implementation,
- first tests.