# GeniusRouter-SA v0.2 Validation Surface

## Valid v0.2 Claims

- Runtime package structure exists.
- Config validation exists.
- Stable SHA256 cache key exists.
- Semantic/classifier merge policy exists.
- Routing decision schema exists.
- First unit tests exist.
- Legacy runtime was preserved.

## Invalid v0.2 Claims

- production ready,
- routing quality proven,
- cost savings proven,
- classifier accuracy proven,
- cache correctness proven for all request classes,
- provider reliability proven,
- RCC-N complete.

## Validation Command

```powershell
python -m unittest discover -s tests
```