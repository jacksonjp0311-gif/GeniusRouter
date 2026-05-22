# GeniusRouter-SA v0.3.2 — Runtime Debug Metadata Repair

## Summary

v0.3.2 repairs the actual runtime path so `_geniusrouter.routing_decision` is inserted into local/debug responses when `GENIUSROUTER_DEBUG_ROUTING=true`.

## Why

v0.3 emitted routing JSONL evidence but failed the unit test requiring debug metadata in the response body. v0.3.1 tightened docs and validation but did not modify the runtime file. v0.3.2 patches the runtime block directly and reruns validation before commit.

## Root Cause

The previous repair used relative paths with `[System.IO.File]::WriteAllText(...)`. PowerShell `Set-Location` changed the shell location, but the .NET current directory still resolved relative paths under `C:\Users\jacks`, so writes targeted the wrong path and failed.

## Boundary

This repair validates local debug metadata and routing-record emission. It does not prove routing quality, provider reliability, production readiness, cost savings, classifier accuracy, or benchmark validity.