---
title: "The Research Agent — Building an Evidence Operator That Compounds"
tags: ["research-agent", "agents", "hermes", "evidence", "vault", "knowledge-management", "compounding", "operator-surfaces"]
source: https://x.com/gkisokay/status/2051275483996909982
date: 2026-06-02
published: 2026-05-04
authors: ["Graeme (@gkisokay)"]
type: bookmark
raw: "[[raw/gkisokay_2051275483996909982]]"
related: ["[[knowledge-system-compounding-obsidian-vellum]]"]
---

# The Research Agent — Evidence Operator

Graeme's blueprint for an always-on research agent that runs inside Hermes. 8,000+ pieces of evidence across 16 topics in 3 months. The core insight: the research agent is not a scraper or summarizer — it's an evidence operator that separates observation from claim from verified knowledge.

## Key Takeaways

- **The chain is everything.** Raw input → finding → claim → verified knowledge → task → approved work. Each stage is a separate file type. Flattening them is how research bots become "hallucination laundries."
- **The SOUL.md is the identity file.** Defines role, boundary, and operating loop: observe → infer priorities → gather → deepen → update vault → route. Not "read news" — run a research loop.
- **Give it a vault, not a chat transcript.** Chat is continuous. A vault accumulates. Minimum: raw/, knowledge/ (claims, findings, sources), dossiers/, verification/, summaries/, handoffs/, decisions/, runs/, ops/, health/, context/, wiki/.
- **Interest profile rebuilt from behavior.** Not "what is trending" — "what does the user care about now?" Built from Hermes state, durable notes, thesis files, recent posts, shipped builds, repeated questions.
- **Verification queue is where the system stays honest.** Uncertainty needs a place to live. Without it, weak claims get ignored or over-promoted. With it, the agent can say "this might matter, but don't build on it yet."
- **Operator surfaces > notes.** Outputs include operator brief, cockpit, action ledger, focus message, dispatch JSON. "A research system should make the next decision easier."
- **Guardrails keep it safe.** Can influence, cannot steer. No trading, no publishing, no purchases, no stale data as fresh. Allowed: collect, score, write, route, surface degradation.
- **Model separation matters.** Cheap models for routine refresh, strong models for synthesis and judgment. "Research is many jobs wearing one coat."

## The Vault Schema

```
research-vault/
├── raw/              — Unprocessed capture. Keep separate from knowledge/.
├── knowledge/
│   ├── claims/       — Candidate beliefs, clustered, tracked over time
│   ├── findings/     — Individual observed signals with source trail
│   └── sources/      — Citation trail: URLs, types, excerpts, timestamps
├── dossiers/         — Living topic files (why it matters, signal, contradictions)
├── verification/     — Under-evidenced claims. "Interesting but not safe to build on."
├── summaries/        — Daily/weekly digests
├── handoffs/         — Routing lanes to other agents
├── decisions/        — What was decided, by whom, on what evidence
├── runs/             — Each refresh leaves a receipt. No receipt = can't trust.
├── ops/              — Source balance, collector health, cockpit
├── health/           — Broken links, missing front matter, gaps, orphans
├── context/          — interest-profile.json, source-plan.md
└── wiki/             — Obsidian-compatible compiled pages
```

## The Source Plan

Rule: prefer sources that change decisions. 

Wider collection ≠ better. Easy collection ≠ useful. The source plan is where the agent learns taste. Tracks source balance: is the run over-dependent on social media? Did primary sources show up? Which collectors failed?

## The Evidence Chain

```
Raw input → Finding (observed signal)
Finding → Claim (candidate belief)  
Claim → Verified knowledge (strong evidence)
Knowledge → Task (what to do about it)
Task → Approved work (operator signs off)
```

Each arrow is a deliberate transformation. Each stage has its own file type. If you collapse this chain, you get confident prose with no audit trail.

## Research Agent vs Other Agents

Research agent = evidence collector. Main = conscious operator. Subconscious = pattern-noticer. Coder = builder. QA = auditor. Content = publisher.

Everything is downstream from research. But research does not own the machine — it contributes evidence and implications. When research, judgment, building, and publishing collapse into one agent, every interesting signal becomes an action item.
