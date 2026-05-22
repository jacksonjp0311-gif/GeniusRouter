# GeniusRouter-SA v0.4 Validation Surface

## Valid v0.4 Claims

- RCC-N navigation surfaces exist.
- Folder-level mini READMEs exist for indexed folders.
- Route map exists.
- RCC-N checker exists.
- RCC-N checker passes.
- Existing unit tests pass.
- Existing smoke validation passes.

## Invalid v0.4 Claims

- code correctness proven,
- routing quality proven,
- production readiness proven,
- cost savings proven,
- provider reliability proven,
- patch safety proven,
- AI understanding proven.

## Validation Commands

```powershell
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
python scripts/release/run_smoke_validation_v0_3.py
```