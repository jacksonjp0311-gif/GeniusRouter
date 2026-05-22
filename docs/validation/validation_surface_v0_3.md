# GeniusRouter-SA v0.3 Validation Surface

## Valid v0.3 Claims

- Health endpoint smoke test exists.
- Chat endpoint smoke test exists.
- Provider call can be mocked for local validation.
- Routing decision record emission is tested.
- Smoke validation report is emitted.
- Runtime evidence layer exists.

## Invalid v0.3 Claims

- routing quality proven,
- cost savings proven,
- classifier accuracy proven,
- production ready,
- provider reliability proven,
- benchmark validated,
- RCC-N complete.

## Validation Commands

```powershell
python -m unittest discover -s tests
python scripts/release/run_smoke_validation_v0_3.py
```

## v0.3 Law

No router-health claim without endpoint smoke validation.
No routing-evidence claim without artifact validation.