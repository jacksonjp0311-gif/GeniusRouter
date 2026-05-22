# GeniusRouter-SA v0.4.2 Validation Surface

## Valid v0.4.2 Claims

- Root README has Human / RCC Nexus / AI Agent trisection.
- Mini READMEs are aligned to v0.4.2.
- RCC-N checker passes.
- Unit tests pass.
- Smoke validation passes.

## Invalid v0.4.2 Claims

- routing quality proven,
- production readiness proven,
- cost savings proven,
- provider reliability proven,
- security proven,
- patch safety proven,
- AI understanding proven.

## Validation Commands

```powershell
python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
python scripts/release/run_smoke_validation_v0_3.py
```