# GeniusRouter-SA v0.3.2 Architecture Change
## Runtime Debug Metadata Repair

## Change Type

Runtime repair and validation integrity repair.

## What Changed

- Patched `src/geniusrouter/main.py` with explicit debug metadata insertion.
- Added v0.3.2 validation report.
- Added v0.3.2 repair release note.
- Anchored this repair script into `scripts/release/`.

## Why

The v0.3.1 attempt changed docs and scripts but did not successfully write the runtime patch due to relative path resolution. v0.3.2 uses absolute paths and synchronizes the .NET current directory.

## Boundary

This validates local mocked-provider debug metadata only. It does not prove routing quality, provider reliability, production readiness, cost savings, classifier accuracy, or benchmark validity.