---
tags: ["agents", "agent-ops", "enterprise", "productivity", "process", "background-agents", "observability", "agent-harness", "ai-strategy", "verification"]
source: https://x.com/mardehaym/status/2087086419491647589
date: 2026-08-11
type: bookmark
description: "No Process, No Agent — Mark Ajzenstadt argues process maturity is ~95% of agent success; document → connect SoR → observability before agent code."
author: mardehaym
summary: "No Process, No Agent — Mark Ajzenstadt argues process maturity is ~95% of agent success; document → connect SoR → observability before agent code."
raw: "[[raw/mardehaym_2087086419491647589]]"
---

# No Process, No Agent

Second LimestoneHQ essay from @mardehaym. Thesis: **model choice ~5%; process maturity ~95%** of whether agent projects survive. AI scales what you already have — documented process becomes automation; dysfunction scales at machine speed.

## Core failure mode

Demos against **undocumented** workflows fill gaps with assumptions (handoffs, escalation, edge rules). Weeks later: wrong emails, bad routing, “AI doesn’t work for sales.”

Time-tracking variance case: looked like a 3-step weekend agent; forecast, threshold rules, and explanation templates were **tribal**. Doc took **3 weeks**, build **1 week** — cited **3:1 documentation:build** ratio as typical.

## Cited landscape numbers (2026 surveys — treat as directional)

- ~86% agent pilots never reach production scale  
- ~16% enterprises have streamlined cross-functional workflows  
- High adoption, low high-performer share; executives deploy agents but few see ROI  
- Salesforce Agentforce: structured-process orgs claim much higher sales growth  

## Sidekicks vs background agents

| Mode | Role | Claimed value |
|------|------|----------------|
| Sidekick / Copilot | Human-prompted | ~10–20% efficiency |
| Background agent | Autonomous, exceptions only | ~60–90% / ~10× enterprise value |

Almost no true background agents in production because they need **documented, reengineered** processes + continuous judgment codified.

Why coding agents “worked” first: software is continuous, digital, relatively observable; sales/finance/HR still run on tribal knowledge and human loops.

## Sequence that matters

1. **Document** top workflows as they actually run (workarounds, “ask Janet,” broken integrations)  
2. **Connect** to systems of record (Salesforce, NetSuite, SAP, Dynamics…)  
3. **Observability** — tracing, logs, eval suites, improvement loops  

## Metric shift

Stop: seats, logins, prompt volume, pilot count.  
Start: **automation readiness** — % of core workflows that are **documented + connected + observable**.

## Why it matters

Complements Velocity Pod piece (V.U.E., knowledge graph): enterprise agent value is mostly **legibility of work**, not model shopping. Aligns with silent-degradation / eval-gate / company-agent notes.

## Skeptical read

Vendor narrative (LimestoneHQ discovery call). Survey stats need primary sources. “95% process” is a rhetorical split, not a measured decomposition. Still a strong anti-demo checklist.

## Related

- [[ai-velocity-pod-senior-engineer-agents-mardehaym]]
- [[notes-on-fde-mardehaym]]
- [[how-to-run-perfect-ai-implementation-pierce]]
- [[agents-behave-like-employees-six-shifts]]
- [[sierra-pinecone-singular-company-agent]]
- [[ai-enterprise-finance-background-agents-varick-vasuman]]
- [[eval-engineering-merge-gate-hanakoxbt]]
- [[agent-workflows-silent-degradation-verification-vladic]]
- [[why-harness-engineering-is-so-hard-winterarc]]
- [[own-your-intelligence-harrison-chase]]
- [[ai-native-engineering-org]]
