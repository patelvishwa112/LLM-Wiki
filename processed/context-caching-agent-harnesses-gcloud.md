---
tags: ["agents", "cost", "agent-harness", "caching"]
source: https://x.com/GoogleCloudTech/status/2095201318348722507
date: 2026-09-02
type: bookmark
description: "Google Cloud: Gemini context caching in agent harnesses — prefix invariance, 0.25x cached reads, ~75% transmitted reduction; skip if <32k or <3 turns."
author: GoogleCloudTech
summary: "Google Cloud: Gemini context caching in agent harnesses — prefix invariance, 0.25x cached reads, ~75% transmitted reduction; skip if <32k or <3 turns."
raw: "[[raw/GoogleCloudTech_2095201318348722507]]"
---

# Slash Token Costs with Context Caching in Agent Harnesses

Google Cloud Tech / Balaji Subramaniam. Gemini Enterprise Agent Platform + ADK 2.0.

Naive harness re-sends 37.5k static code + growing traceback every turn → 5-turn run bills ~189k prompt tokens. Cache requires **byte-identical prefix from token 0**. Mutable metadata in the header → miss. Dynamic suffix only.

Cached reads billed 0.25x. Measured: 5-file modernization 79% transmitted reduction; SQLi debate 75%; dependency-graph 75%.

Decision tree: do **not** cache if context <32,768 tokens, turns <3, or headers change every cycle. Do cache iterative test-and-repair against large repos. CachePayloadBuilder + ContextCacheManager (hash, TTL, dispatch).

Vendor numbers; pair with Uber's 1-hour TTL lesson.

## Related

- [[software-factory-uber-scale]]
- [[kv-prefix-prompt-semantic-caching-llms-avichawla]]
