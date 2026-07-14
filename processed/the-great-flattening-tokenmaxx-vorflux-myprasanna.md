---
type: bookmark
description: "Prasanna S (ex-Rippling CTO) argues frontier coding models are already superhuman: the scarce resource is harnessed judgment (tokenmaxx, not peoplemaxx), cloud full-stack sandboxes, and six lifecycle bottlenecks ending in while-you-sleep merges — positioned as Vorflux."
tags: ["agents", "harness-engineering", "agent-harness", "tokenmaxxing", "cloud-agents", "multi-agent", "orchestration", "verification", "review", "cost-optimization", "vorflux", "agent-ops", "enterprise"]
source: https://x.com/myprasanna/status/2077065557204222238
date: 2026-07-14
author: myprasanna
summary: "Prasanna S (ex-Rippling CTO) argues frontier coding models are already superhuman: the scarce resource is harnessed judgment (tokenmaxx, not peoplemaxx), cloud full-stack sandboxes, and six lifecycle bottlenecks ending in while-you-sleep merges — positioned as Vorflux."
raw: "[[raw/myprasanna_2077065557204222238]]"
---

# The Great Flattening

Long-form X Article by **Prasanna S** (@myprasanna), former Rippling co-founder/CTO, arguing that coding models crossed into genuine superhuman territory and that the org chart — and the unit of compute — must flatten around a **neutral harness** rather than more headcount.

## Key takeaways

### Thesis
- Frontier models no longer "fit inside your laptop": long autonomous runs, self-planning, self-compaction, self-check. Localhost is the wrong home.
- Humans remain in the loop, but the babysitting **moved up a level**: trust of unread merges, multi-session concurrency, real-stack verification.
- **Tokenmaxx, not peoplemaxx.** Profile every remaining human bottleneck and drown it in tokens. The seat is the wrong unit of compute; the token is the right one.

### The great flattening
- Code stopped being the scarce skill. Idea → production in hours collapses middle hops (PM/manager/engineer handoffs).
- Human "cell boundary" stays at customer-facing edges (sales, relationships); inside the boundary, work collapses into the **harness**.
- Meta-job: externalize judgment (triage, architecture bar, contrarian calls) into the harness so it compounds without the person in the room.

### Why the harness must be yours (and neutral)
- Labs absorb hand-built mechanics each release (context management, sub-agent patterns) — betting on mechanics loses.
- Two things labs cannot ship well: **your** judgment, and **cross-family neutrality** (they will not route to a competitor's model for review or dispatch).
- Vorflux pitch: train no models; route across labs; keep harness current as frontier models churn (Opus 4.8, Fable 5 called out as rapid resets).

### Six bottlenecks (profile → drown in tokens)
1. **Machine** — Real cloud sandbox of the *whole* stack (multi-repo, services, DB, auth, seed data, browser cookies, mobile), not a blind VM; snapshot ready machines.
2. **Planning** — Heavy tokens before code: explore stack, ask questions, adversarial plan-of-plans with sub-tasks and tests; human reviews dependency graph and architecture, not 8k-line diffs.
3. **Orchestration** — Controller fans dependency graph; best-model-per-task (cross-lab table for GPT/Claude/Gemini/open Chinese models — dated June 2026); fresh context windows per sub-agent.
4. **Testing** — E2E on the live stack + visual/browser recordings (and mobile); live branch URLs; "seen working" not "unit green."
5. **Review** — Adversarial review from a **different model family** than the author; story-ordered walkthrough for phone/async approval.
6. **Merge** — Auto conflict/rebase against moving master, feature flags, even deploy while the asker sleeps.

### Destination
- Parallel overnight sessions replace backlogs-as-queues. Software becomes cheap experiments; bottleneck shifts to **what to build and sell**.
- "While you sleep" development as the product of clearing all six bottlenecks.
- Business model angle: Vorflux runs *with* customers (profiling their stack); Codex partnership for BYO subscription ~10x rate claims. Monetization under token+EC2 burn is the open execution question (thread-level).

## Why it matters

Clearest 2026 articulation of the **harness as competitive advantage** and the lifecycle map (machine → plan → orchestrate → test → cross-lab review → merge) that many agent-coding threads name only partially. Useful checklist for evaluating cloud agent products (Devin, managed agents, enterprise harnesses) against full-stack fidelity and adversarial review, not just codegen demos.

## Skeptical read

- Strong product narrative for Vorflux; treat cost claims and "10x off" as marketing until validated.
- Benchmark table and model-strength table will age quickly (author acknowledges).
- "Backlogs shouldn't exist" assumes verification and product judgment scale with tokens — still the hard part.

## Related

- [[learn-harness-engineering]]
- [[harness-engineering-2026-discipline]]
- [[glean-coding-harness-programmatic-tool-calling]]
- [[how-to-build-custom-agent-harness-langchain]]
- [[fable-manager-sol-worker-nateherk]]
- [[fable-orchestrate-huge-project-40-subagents-ryancarson]]
- [[how-to-build-conductor-multi-agent-leanxbt]]
- [[economy-of-tokens-vipulved-modular-ai]]
- [[token-capital-scaffolding-process-governance]]
- [[addy-osmani-agent-autonomy-ladder-six-levels]]
- [[agent-workflows-silent-degradation-verification-vladic]]
- [[sierra-pinecone-singular-company-agent]]
