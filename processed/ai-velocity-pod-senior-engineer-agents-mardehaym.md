---
tags: ["agentic-engineering", "agents", "software-factory", "human-in-the-loop", "verification", "productivity", "agent-ops", "coding-tools", "career", "cost-optimization"]
source: https://x.com/mardehaym/status/2085025462481223755
date: 2026-08
type: bookmark
description: "Mark Ajzenstadt / LimestoneHQ AI Velocity Pod — one senior + agents vs five-person squad; V.U.E. gate, knowledge graph week-one, six-step ticket loop."
author: mardehaym
summary: "Mark Ajzenstadt / LimestoneHQ AI Velocity Pod — one senior + agents vs five-person squad; V.U.E. gate, knowledge graph week-one, six-step ticket loop."
raw: "[[raw/mardehaym_2085025462481223755]]"
---

# AI Velocity Pod — one senior + agents vs five-person team

@mardehaym (Mark Ajzenstadt / LimestoneHQ) argues the post-agent bottleneck is **review, direction, and judgment**, not keystrokes. Structure: **AI Velocity Pod**.

## Claimed case

PE-backed healthcare, same codebase/scope, 90 days:

- Pod: **122 merged PRs**
- Traditional squad: **40–60** PR average
- Also: ~50% faster cycles, 85% PRs &lt;5 reviewer comments, deploy weeks→days, ~$200/dev/mo AI compute
- Cost: pod **$15–20K/mo** vs traditional loaded ~**$50–73K/mo** (annual squad $610–880K loaded in writeup)

## Why composition changed

DX Q2 2026 (cited): 4–6 hrs/week saved, PR volume ~doubled. Writing collapsed; waiting on review/deps/PM/QA dominates. Five-person squads pay coordination tax for a bottleneck agents removed.

## Pod composition

**Core**

- 1.0 FTE senior full-stack + agents across SDLC  
- 0.5 FTE AI delivery architect (shared across pods)

**Shared / fractional**

- Pooled BA/PM, customer success, Dev Intelligence governance, automated QA  
- Optional vertical tech partner (billing, claims, compliance)

## Non-negotiable: V.U.E.

On every PR, engineer must (agent off):

1. **V**erify it works without the agent  
2. **U**nderstand why it works  
3. **E**xplain to someone who didn’t use the agent  

Without independent judgment, volume multiplies polished wrong code (Duolingo ~20% defect anecdote cited). Domain knowledge is the verification tool.

## Velocity Framework OS

**Week 1:** knowledge graph (modules, deps, data flows, domain terms) live before any agent codegen.

**Every ticket — six human-owned gates**

1. Define — business outcome  
2. Spec — agent draft, engineer validates architecture/domain  
3. Plan — agent decompose, engineer sequencing  
4. Implement — agent ~90% lines, engineer V.U.E. every PR  
5. Test — auto + engineer edges (+ compliance if regulated)  
6. Document — agent docs, engineer checks vs Define outcome  

## Fit questions

1. Idle wait &gt;30% of eng hours? → coordination overhead case  
2. Can you hire/afford senior who passes V.U.E. in **your** domain?  
3. Output-limited vs **judgment**-limited? Fix review before adding volume  

## Why it matters

Concrete staffing/ops model for agentic delivery: concentrate seniority, fractional services, gated loop + codebase graph. Aligns with software-factory and 100x agentic-engineer notes; stresses verification over “more agents.”

## Skeptical read

Vendor narrative (LimestoneHQ / discovery-call CTA). Metrics are self-reported case study; PE/healthcare scope may not generalize. Still useful as a checklist (V.U.E., graph-first, judgment-limited trap) even if numbers are marketing.

## Related

- [[hundred-x-agentic-engineer-preferences-systematicls]]
- [[the-agentic-engineer-workflow-aashatwt]]
- [[every-agentic-engineering-hack-june-2026]]
- [[software-factory-linear-claude-cloud-routines]]
- [[software-factories-light-and-dark-addy-osmani]]
- [[fable-orchestrate-huge-project-40-subagents-ryancarson]]
- [[the-great-flattening-tokenmaxx-vorflux-myprasanna]]
- [[ai-native-engineering-org]]
- [[eval-engineering-merge-gate-hanakoxbt]]
- [[why-harness-engineering-is-so-hard-winterarc]]
