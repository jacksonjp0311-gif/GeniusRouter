# GeniusRouter Routing Decision Contract

Future GeniusRouter runtime hardening should emit a routing decision record for each request.

Target schema:

```json
{
  "schema": "GeniusRouter-SA-v0.1-routing-decision",
  "request_id": "",
  "timestamp": "",
  "semantic_tier": "low|medium|high|unknown",
  "classifier_tier": "low|medium|high|unknown",
  "final_tier": "low|medium|high",
  "selected_model": "",
  "provider": "",
  "cache_enabled": true,
  "cache_hit": false,
  "cache_key": "",
  "fallback_used": false,
  "fallback_reason": null,
  "latency_ms": null,
  "claim_boundary": "routing decision evidence, not proof of optimal routing"
}
```

Boundary:

A routing decision record is evidence of what the router did. It is not proof that the selected model was optimal.