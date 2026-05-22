# CODEX DELTA-PHI - GENIUSROUTER SOFTWARE ARCHITECTURE
## GeniusRouter-SA v0.1 - Full Structural Runtime Architecture and Governance Genesis Layer

Status: Canonical v0.1 software architecture checkpoint
Date: May 2026
Runtime project: GeniusRouter
Runtime type: FastAPI OpenAI-compatible LLM routing proxy
Enhancement type: Source-preserving Codex/RCC-N aligned structural architecture
Runtime mutation in this release: none

---

## 1. Version

v0.1 - Full Structural Runtime Architecture and Governance Genesis Layer

This layer defines the complete software architecture, runtime contract, evidence contract, validation surface, non-claim locks, repository documentation spine, and future RCC-N preparation path for GeniusRouter.

This release is intentionally documentation-first. It does not mutate router behavior. It prepares the project for safe runtime hardening.

---

## 2. Source and Attribution

Primary project origin:

- Project: GeniusRouter
- Original owner / main developer credited by repository: Keith / keithofaptos
- Current repository used for this architecture pass: https://github.com/jacksonjp0311-gif/GeniusRouter
- Local working path: C:\Users\jacks\OneDrive\Desktop\GeniusRouter

Existing contributors file credits:

- keithofaptos as owner and main developer
- Grok by xAI as co-creator of the initial architecture, code, routing logic, and three-tier IQ system

Codex/RCC-N enhancement:

- James Paul Jackson
- Role: source-preserving architecture hardening, repository governance, evidence-gated evolution, future RCC-N preparation

Attribution lock:

This architecture must preserve Keith's original project vision. It must not erase project authorship, overtake project identity, or present the Codex/RCC-N enhancement as the original invention of GeniusRouter.

---

## 3. Current Repository State

The current repository is compact and early-stage.

Observed files:

```text
GeniusRouter/
  .env.example
  .gitignore
  config.yaml
  CONTRIBUTORS.md
  docker-compose.yml
  Dockerfile
  LICENSE
  README.md
  requirements.txt
  src/
    main.py
    src/
      __init__.py
```

Current git status at dump time:

```text
branch: main
latest commit: 37c7125 Remove duplicate Docker command
working tree: clean
```

Current runtime file:

```text
src/main.py
```

Current runtime endpoints:

```text
POST /v1/chat/completions
GET  /health
```

Current runtime dependencies:

```text
fastapi
uvicorn
litellm
semantic-router
redis
ollama
pydantic
python-dotenv
PyYAML
```

---

## 4. Current Runtime Intent

GeniusRouter currently intends to route OpenAI-compatible chat requests across low, medium, and high model tiers.

Current conceptual chain:

```text
OpenAI-compatible request
-> extract prompt text
-> semantic-router first-pass tier
-> Ollama classifier tier
-> choose configured model
-> optionally check Redis cache
-> send to LiteLLM
-> return OpenAI-compatible response
```

Current configuration file:

```text
config.yaml
```

Current tier configuration:

```yaml
routing:
  low_iq: "ollama/gemma4:e4b"
  medium_iq: "ollama/qwen3.6:35b-a3b"
  high_iq: "openrouter/anthropic/claude-opus-4.7"
```

Core project vision:

```text
Route prompts to the lightest sufficient model tier while preserving access to stronger models when required.
```

---

## 5. Purpose of GeniusRouter-SA

GeniusRouter-SA is the software architecture layer that turns GeniusRouter from an early routing prototype into a governed, testable, evidence-emitting LLM routing runtime.

It answers:

1. What is GeniusRouter as software?
2. What are the stable runtime contracts?
3. What claims are allowed now?
4. What claims require evidence later?
5. What should be tested first?
6. What should be logged as routing evidence?
7. What must be preserved from Keith's original vision?
8. What must be in place before RCC-N injection?
9. How should AI agents safely modify the repo?
10. How should the repo evolve toward a stable checkpoint?

---

## 6. What This Is

GeniusRouter-SA v0.1 is:

- a software architecture document,
- a repository governance layer,
- a source-preserving enhancement plan,
- a runtime hardening roadmap,
- a future RCC-N preparation surface,
- a claim-boundary document,
- a test-readiness plan,
- a routing evidence contract,
- a documentation registry seed,
- an AI operating contract seed.

---

## 7. What This Is Not

GeniusRouter-SA v0.1 is not:

- not a runtime behavior change,
- not proof that the router works correctly,
- not proof of production readiness,
- not proof of routing accuracy,
- not proof that the classifier selects the optimal tier,
- not proof of cost savings,
- not proof that quality is preserved,
- not proof that caching is safe for every request,
- not proof of security,
- not proof of provider reliability,
- not RCC-N completion,
- not a benchmark result,
- not a replacement for tests,
- not a replacement for runtime logs,
- not permission to overclaim SOTA status without evidence.

---

## 8. Core Extraction

The GeniusRouter invariant is:

```text
Route requests to the lightest sufficient model tier while preserving high-tier access, provider flexibility, OpenAI-compatible request shape, and configurable deployment.
```

The Codex/RCC-N invariant is:

```text
No claim should be stronger than the evidence emitted by the repo.
```

The combined GeniusRouter-SA invariant is:

```text
GeniusRouter should become an evidence-governed LLM routing runtime:
cheap when possible,
strong when necessary,
observable always,
bounded in claims.
```

---

## 9. Canonical Locks

Future GeniusRouter evolution must preserve:

1. Keith's original project attribution.
2. The low / medium / high tier routing concept unless explicitly replaced by a documented architecture change.
3. Config-first model selection.
4. OpenAI-compatible proxy behavior.
5. Docker-first deployment path.
6. Local and hosted provider compatibility.
7. API key secrecy.
8. Non-claim boundaries around routing quality, cost savings, and production readiness.
9. Tests before stronger implementation-health claims.
10. Benchmarks before cost-savings claims.
11. Routing decision logs before routing-quality claims.
12. Context documentation before AI-agent-driven refactors.
13. RCC-N as a later injection layer after runtime structure is stable.

---

## 10. Current Runtime Risks

| Risk | Current State | Required Hardening |
|---|---|---|
| No tests | No tests folder observed | Add unit and smoke tests |
| No CI | No workflow observed | Add CI after tests exist |
| Config validation | YAML loaded directly | Add typed config schema |
| Semantic route unused | semantic_tier computed but final model uses classifier tier | Define merge policy |
| Cache key instability | Python hash() used | Replace with SHA256 |
| Redis hard dependency | Cache lookup can fail runtime | Add graceful fallback |
| Broad exceptions | Exceptions swallowed in classifier | Add structured error records |
| No decision ledger | Routing choice not emitted | Add routing decision record |
| README issues | Duplicate content and encoding artifacts | Rewrite after architecture pass |
| Source layout | src/main.py plus nested src/src artifact | Normalize package layout |
| Cost claim | README claims 70-92% savings | Move behind benchmark gate |
| SOTA claim | README uses SOTA phrasing | Bound as project aspiration until benchmarked |

---

## 11. Target Runtime Loop

The target GeniusRouter runtime loop is:

```text
Request
-> validate request shape
-> extract prompt
-> load typed config
-> compute semantic tier
-> compute classifier tier
-> merge tier decisions
-> select provider/model
-> compute stable cache key
-> check cache if eligible
-> call provider through LiteLLM
-> emit routing decision record
-> update cache if eligible
-> return OpenAI-compatible response
```

The target loop must separate:

```text
routing decision
provider execution
cache behavior
fallback behavior
response return
evidence emission
```

---

## 12. Tier Decision Model

Target tier values:

```text
low
medium
high
unknown
```

Target semantic route:

```text
semantic_tier = semantic_router(prompt)
```

Target classifier route:

```text
classifier_tier = classifier(prompt)
```

Target merge policy for v0.2:

```text
if semantic_tier == classifier_tier:
    final_tier = semantic_tier

if classifier_tier is high:
    final_tier = high

if semantic_tier is high and classifier_tier is medium:
    final_tier = high

if semantic_tier is low and classifier_tier is medium:
    final_tier = medium

if either tier is unknown:
    final_tier = safest available non-low tier, default medium
```

This is conservative and prevents obvious under-routing while avoiding automatic high-tier overuse.

---

## 13. Routing Decision Evidence Contract

Future runtime hardening should emit one routing decision record per request.

Target JSON:

```json
{
  "schema": "GeniusRouter-SA-v0.1-routing-decision",
  "request_id": "",
  "timestamp": "",
  "semantic_tier": "low|medium|high|unknown",
  "classifier_tier": "low|medium|high|unknown",
  "final_tier": "low|medium|high",
  "selected_model": "",
  "provider": "ollama|openrouter|openai|anthropic|custom|unknown",
  "cache_enabled": true,
  "cache_hit": false,
  "cache_key": "",
  "fallback_used": false,
  "fallback_reason": null,
  "latency_ms": null,
  "claim_boundary": "routing decision evidence, not proof of optimal routing"
}
```

Routing record law:

```text
No routing-quality claim without routing-decision evidence.
```

---

## 14. Cache Contract

Current code uses Python hash() to form cache keys.

Problem:

```text
Python hash() is intentionally not stable across processes by default.
```

Target cache key:

```text
sha256(normalized_messages + selected_model + routing_config_version)
```

Cache eligibility must be explicit.

Cache should be disabled or bypassed for:

- streaming requests unless supported,
- tool-call requests unless schema-stable,
- user requests marked no-cache,
- provider responses with error state,
- requests containing volatile context.

Cache law:

```text
No cache claim without stable key and cache-hit evidence.
```

---

## 15. Config Contract

Current config is useful but untyped.

Target config schema:

```yaml
routing:
  low_iq: string
  medium_iq: string
  high_iq: string

local_rigs:
  low_url: string | empty
  medium_url: string | empty
  high_url: string | empty

classifier:
  model: string
  enabled: boolean

cache:
  enabled: boolean
  ttl_seconds: integer
```

Future typed model:

```python
class RoutingConfig(BaseModel):
    low_iq: str
    medium_iq: str
    high_iq: str

class LocalRigsConfig(BaseModel):
    low_url: str = ""
    medium_url: str = ""
    high_url: str = ""

class ClassifierConfig(BaseModel):
    model: str
    enabled: bool = True

class CacheConfig(BaseModel):
    enabled: bool = True
    ttl_seconds: int = 3600
```

Config law:

```text
No runtime start without validated config.
```

---

## 16. Provider Contract

Target provider resolution:

```text
ollama model -> OLLAMA_BASE_URL
openrouter model -> OPENROUTER_API_KEY
openai model -> OPENAI_API_KEY
anthropic model -> ANTHROPIC_API_KEY
custom local rig -> configured base URL
```

Provider errors should return structured failure responses or fallback attempts, not hidden exceptions.

Provider law:

```text
No provider fallback without a logged fallback reason.
```

---

## 17. OpenAI-Compatible Proxy Contract

The route:

```text
POST /v1/chat/completions
```

should preserve OpenAI-compatible fields where possible.

Required input fields:

```json
{
  "model": "geniusrouter/auto",
  "messages": []
}
```

Required output behavior:

- return provider response shape when successful,
- return structured error on failure,
- preserve relevant OpenAI-compatible fields,
- never expose API keys,
- optionally include GeniusRouter routing metadata only when debug mode is enabled.

Compatibility law:

```text
No proxy claim without compatibility tests.
```

---

## 18. Health Contract

Current health returns:

```json
{
  "status": "healthy",
  "router": "GeniusRouter 3-Tier IQ (2026)",
  "config": {}
}
```

Target health should separate:

```json
{
  "status": "healthy|degraded|unhealthy",
  "router": "GeniusRouter",
  "version": "GeniusRouter-SA v0.2",
  "config_loaded": true,
  "cache": "enabled|disabled|degraded",
  "classifier": "enabled|disabled|degraded",
  "providers_configured": {
    "low": true,
    "medium": true,
    "high": true
  }
}
```

Health law:

```text
Healthy means dependencies are checked or explicitly marked optional.
```

---

## 19. Proposed Repository Architecture

Target structure:

```text
GeniusRouter/
  README.md
  README_5_MINUTES.md
  pyproject.toml
  requirements.txt
  Dockerfile
  docker-compose.yml
  config.yaml
  .env.example
  LICENSE
  CONTRIBUTORS.md

  docs/
    README.md
    DOCS_REGISTRY.md
    software_architecture/
      geniusrouter_sa_v0_1_full_software_architecture.md
    architecture_changes/
      geniusrouter_sa_v0_1_docs_architecture_injection.md
    release_notes/
      v0_1_docs_architecture_injection.md
    protocols/
      non_claim_locks.md
      ai_operating_contract.md
      routing_decision_contract.md
      runtime_hardening_plan.md
    context/
      repository_context_index.json
    roadmap/
      geniusrouter_sa_roadmap.md
    validation/
      validation_surface_v0_1.md

  src/
    geniusrouter/
      __init__.py
      __main__.py
      main.py
      config.py
      routing.py
      cache.py
      providers.py
      schemas.py
      telemetry.py

  tests/
    test_health.py
    test_config.py
    test_routing_decision.py
    test_cache_key.py
    test_openai_compat.py

  reports/
    routing/
    validation/

  artifacts/
    routing_decisions/
    evidence/
```

This structure is a target, not completed by v0.1.

---

## 20. Testing Contract

Minimum future tests:

1. config loads valid YAML,
2. missing config fields fail clearly,
3. health endpoint returns expected shape,
4. prompt extraction preserves message content,
5. semantic route returns valid tier or unknown,
6. classifier route returns valid tier or fallback medium,
7. merge policy prevents unsafe under-routing,
8. cache key is stable SHA256,
9. cache miss proceeds to provider call,
10. Redis failure degrades gracefully,
11. provider failure returns structured error,
12. routing decision record validates schema,
13. OpenAI-compatible input accepted,
14. API keys are not exposed,
15. README claims remain bounded.

Test law:

```text
No implementation-health claim without passing tests.
```

---

## 21. Validation Surface

A valid GeniusRouter-SA v0.1 repository state must show:

- docs architecture present,
- docs registry present,
- non-claim locks present,
- AI operating contract present,
- routing decision contract present,
- repository context index present,
- architecture change record present,
- release note present,
- source attribution preserved,
- no runtime behavior modified by docs-only release.

A valid future runtime state must show:

- package layout normalized,
- typed config validation,
- stable cache key,
- graceful Redis fallback,
- routing decision records,
- tests passing,
- benchmark claims gated by benchmark output.

---

## 22. Falsification Surface

GeniusRouter-SA claims are weakened if:

- production readiness is claimed before tests,
- cost savings are claimed before benchmark evidence,
- routing quality is claimed without decision logs,
- classifier accuracy is claimed without labeled evaluation,
- semantic route is computed but not used or explained,
- Redis failure crashes the router when cache is optional,
- provider failure is hidden,
- cache keys are unstable,
- API keys leak in logs,
- README claims exceed repo evidence,
- attribution to Keith is removed,
- RCC-N is injected as decoration before structure is stable.

---

## 23. RCC-N Preparation

RCC-N should be injected after v0.2 or v0.3, not before runtime hardening.

Reason:

```text
RCC-N should orient around real structure.
It should not decorate unstable structure.
```

Future RCC-N surfaces:

```text
README trisection
README_5_MINUTES.md
docs/context/repository_context_index.json
docs/context/rcc_nexus_index.json
rcc/nexus/route_map.json
folder mini READMEs
AI Agent README section
validation commands
claim boundary blocks
```

RCC-N law:

```text
Meaning + location + evidence + boundary before agent modification.
```

---

## 24. Roadmap

| Version | Goal |
|---|---|
| v0.1 | Full docs architecture, governance, claim locks, context seed |
| v0.2 | Runtime hardening: package layout, typed config, stable cache, graceful fallback |
| v0.3 | Unit tests and smoke validation |
| v0.4 | Routing decision ledger and evidence files |
| v0.5 | Benchmark harness for cost, latency, cache hit rate, tier distribution |
| v0.6 | README rewrite and public metrics dashboard |
| v0.7 | RCC-N injection and mini READMEs |
| v0.8 | Release manifest and readiness gate |
| v1.0 | Stable evidence-governed router checkpoint |

---

## 25. Practitioner Compression

```text
Preserve Keith's vision.
Make routing observable.
Make config typed.
Make cache stable.
Make failures visible.
Make claims bounded.
Make tests mandatory.
Make benchmarks earn cost claims.
Make RCC-N follow structure.
```

---

## 26. v0.1 Laws

```text
No routing claim without routing evidence.
No cost claim without benchmark evidence.
No production claim without tests.
No cache claim without stable keys.
No provider fallback without logged reason.
No AI-agent modification without repository context.
No RCC-N injection before structural orientation.
```

---

## 27. Conclusion

GeniusRouter has a strong seed: a practical low / medium / high model routing proxy that can connect local rigs, hosted providers, OpenRouter, Ollama, Redis caching, and OpenAI-compatible clients.

GeniusRouter-SA v0.1 does not pretend the repo is finished. It makes the next steps honest.

The immediate goal is to preserve Keith's vision while building the missing engineering spine:

```text
architecture
tests
typed config
stable cache
routing evidence
bounded claims
RCC-N-ready context
```

The destination is an evidence-governed LLM router:

```text
cheap when possible,
strong when necessary,
observable always,
bounded in claims.
```