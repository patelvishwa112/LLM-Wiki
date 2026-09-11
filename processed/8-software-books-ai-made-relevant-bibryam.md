---
tags: ["coding-agents", "architecture", "engineering", "agents"]
source: https://x.com/bibryam/status/2096524948365775313
date: 2026-09-06
type: bookmark
description: "Bilgin Ibryam: eight pre-agent SE books become more relevant as you delegate implementation — decide, specify, DDD, architecture, data, threat model, production, Accelerate."
author: bibryam
summary: "Bilgin Ibryam: eight pre-agent SE books become more relevant as you delegate implementation — decide, specify, DDD, architecture, data, threat model, production, Accelerate."
raw: "[[raw/bibryam_2096524948365775313]]"
---

# 8 Software Books AI Has Made More Relevant

Bilgin Ibryam (@bibryam). Companion: https://generativeprogrammer.com/p/8-software-books-ai-has-made-more

Thesis: agents write the code; humans must still recognize which decisions are sound. Knowing what good software looks like gets *more* valuable as generation gets cheap.

| Area | Book | Agent-specific sting |
|---|---|---|
| Worth building | *Escaping the Build Trap* (Perri) | Convincing prototype before anyone knows if it's needed |
| What correct means | *Specification by Example* | Agent writes impl *and* tests that share the same wrong assumption |
| Business meaning | *Learning Domain-Driven Design* | Copies rules across bounded contexts |
| Architectural trade-offs | *Software Architecture: The Hard Parts* | Another service looks cheap; later deletes a boundary that was load-bearing |
| Data guarantees | *DDIA* 2e | Schema change looks consistent in-repo while events/clients diverge |
| Threats | *Threat Modeling* | README/tool prompt injection + shell/credentials; book predates this — keep newer guidance |
| Production failures | *Release It!* 2e | Retry-on-retry multiplies load |
| Delivery flow | *Accelerate* | Parallel agents vs one review queue; judge by lead time/stability, not generated LoC |

Start where the team has least clarity.

## Related

- [[software-factory-uber-scale]]
- [[70-ideas-ai-product-process-nurijanian]]
