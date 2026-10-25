---
title: "Free the Models: Harness Design at the Frontier"
type: bookmark
description: "Replit's argument that harnesses should let the model choose delegation: four subagent primitives, GPT-6 Astra delegating on its own, and Pareto wins on DeepSWE and Terminal-Bench."
tags: [agent-harness, subagents, orchestration, cost-optimization, models, harness-engineering]
source: https://x.com/pirroh/status/2104976589180252218
date: 2026-09-29
author: Michele Catasta
summary: "Replit's argument that harnesses should let the model choose delegation: four subagent primitives, GPT-6 Astra delegating on its own, and Pareto wins on DeepSWE and Terminal-Bench."
raw: "[[raw/pirroh_2104976589180252218]]"
---

# Free the Models: Harness Design at the Frontier

**Source:** Michele Catasta (@pirroh), 2026-09-29. An X article by the Replit AI team (with Daniel Furman, Jacky Zhao, Vaibhav Kumar, Ed Sioufi) on why their agent stopped routing and started letting the model decide.

The central argument is that a router is structurally capped: whether it is a heuristic or a small model reading each turn, it is less capable than the models it selects among. Replit Agent inverts this — the core loop picks its subagents' tier and effort, and adjusts its own effort as the task unfolds. That requires harness primitives rather than a policy: domain-aware specialists (read-only explorers, browser testers, reviewers, a design subagent for slides and UI) alongside a general worker; small/standard/large tiers each with an effort level; reusable subagents that stay warm so the loop can return to one it already briefed; and dynamic effort tuning that changes effort mid-turn without breaking the prompt cache.

The empirical claim rests on two benchmark comparisons. Replit Agent in Max mode scores 72% on DeepSWE v1.1 at $2.11/task, versus Astra alone at 67%/$1.60 (low) or 74%/$4.43 (xhigh), and a "sidekick" harness with one long-lived worker at 61%/$1.34. On Terminal-Bench 4.0 it reaches 49% at $2.53 against 42%/$2.25 (low), 60%/$5.86 (xhigh), and 33%/$1.84 for the sidekick — an 11- and 16-point win over the sidekick, and the only configuration on the Pareto frontier against both baselines.

They read this as Sutton's bitter lesson applied to harnesses: baked-in human workflow helps short-term, plateaus, and loses to general methods that scale with compute. Astra, in their production traces, is the first model they have seen routinely hand implementation to general workers unprompted and then return to the same worker instead of restarting; they also report needing the code-review subagent less with Astra and Fable 5.1 at no eval-score cost. Notably, the harness still decides which specialists exist — the model decides when and whom to dispatch.

## Why it matters

If delegation quality is a property of the model rather than the prompt, then harness work shifts from encoding procedure to exposing good primitives and pricing them honestly. That inverts a lot of current practice (deterministic orchestrators, hand-written routing rules, fixed pipelines): those are the parts that get invalidated each model release. The cost framing also matters for buyers — the Pareto frontier moved left, meaning the same score got ~2x cheaper, and the win came from token allocation rather than a better model.

## Key points

- DeepSWE v1.1: Replit Agent 72% @ $2.11/task; Astra alone 67% @ $1.60 (low), 74% @ $4.43 (xhigh); sidekick 61% @ $1.34.
- Terminal-Bench 4.0: Replit Agent 49% @ $2.53; Astra 42% @ $2.25 (low), 60% @ $5.86 (xhigh); sidekick 33% @ $1.84.
- Beats the single-worker sidekick by 11 and 16 points; Astra alone beats it on score only by spending 2x+ per task.
- Four primitives: domain-aware specialists, subagent tiers + effort, reusable warm subagents, dynamic mid-turn effort escalation.
- GPT-6 is the first OpenAI family supporting mid-turn effort changes without breaking the cache; longer cache lifetime is what makes warm subagents cheap.
- In production at medium effort, Fable models rarely delegate implementation (they use explorers/reviewers and keep coding); Astra routinely delegates to general workers and returns to briefed ones, a return rate rising each generation.
- A production trace (2026-09-17) shows 3 of 5 worker dispatches were returns to an already-briefed worker.
- Reported side effect: less code-review subagent use with Astra/Fable 5.1 at unchanged eval scores.

## Related

- [[harness-is-the-product-context-aware-agents]]
- [[harness-engineering-2026-discipline]]
- [[claude-subagents-vs-agent-teams]]
- [[fable-manager-sol-worker-nateherk]]
- [[continual-learning-replit-agent-vibench]]
