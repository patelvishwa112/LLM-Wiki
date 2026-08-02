---
tags: ["evals", "llm-judges", "agents", "agent-harness", "harness-engineering", "verification", "trajectories", "observability", "production", "trace-data"]
source: https://x.com/hanakoxbt/status/2083540339147567268
date: 2026-08-01
type: bookmark
description: "Six-step course on eval infrastructure so an automated gate can merge agent changes without human review — blast radius over confidence."
author: hanakoxbt
summary: "Six-step course on eval infrastructure so an automated gate can merge agent changes without human review — blast radius over confidence."
raw: "[[raw/hanakoxbt_2083540339147567268]]"
---

# Eval Engineering: the merge gate (Hanako)

## Key takeaways

- End state is not "trust the model" — it is a **gate that reads evidence and applies rules** so agent diffs can merge without a human reading them.
- Most orgs lack the gate because the **evidence infrastructure does not exist yet**, not because of courage.
- Six prerequisites before opening auto-merge lanes.

### 1. The score is partly about your judge

- LLM-as-judge has **own-family bias** (e.g. GPT-5.2 / Gemini handing 75–84% wins to own family; Claude sometimes under-rates its own). ArenaHard bias span roughly **-38% to +90%**. Same outputs can score 93% under one judge and 39% under another.
- **Verbosity bias** rewards length independent of substance.
- Rules: judge from a **different family** than the generator; high-stakes → **panel across vendors**; anything objectively checkable → **code**, not a judge.
- A biased judge is worse than no gate — it launders a guess into a number.

### 2. A verdict that does not change the run is a report

- Dashboard-only evals are thermometers. Promote evals **into the agent runtime** (thermostat): low grounding rejects handoffs, schema failure blocks edges, suspected fabrication quarantines branches, verified completion is the only end state.
- A system already steered by verdicts produces signals worth reading at merge time.

### 3. Grade the path, not just the answer

Three levels:

1. **End-to-end** — did the task succeed?
2. **Trajectory** — loops, redundant calls, thrashing?
3. **Component** — which retriever/tool/sub-agent failed?

Starter metrics: **faithfulness** (grounded in real tool returns), **tool parameter accuracy**, **task completion** against external signals (not self-report). For the gate, a clean trajectory often matters more than an identical-looking final diff reached after thrashing.

### 4. Best tests are already in the logs

Mine production traces: clean successes, user corrections (free labels), empty tool returns, duplicate identical calls, external timeouts. Write each up in four lines (what happened, what worked/didn't, agent vs dependency, which capability is protected). Test the **verifier** on known-good and plausible-bad examples first. Convert every failure into a permanent test.

### 5. Pin the judge or lose the month

- Judges are versioned software — **pin and log versions** with every score.
- Rubrics as **independently observable outcomes**, not proxies (length, keywords, citation count, reference similarity) — Goodhart + model in the loop.
- Intrinsic self-correction without external grounding often fails or hurts (Huang et al., DeepMind, ICLR 2024).
- Suite sizing: working guidance ~**500+ cases**, run short enough to finish in a coffee break.

### 6. Open the gate on blast radius, not confidence

Sort work by **cost of undo**:

| Lane | Examples | Gate posture |
|------|----------|--------------|
| Reversible & contained | copy, isolated function with coverage | open earliest |
| Reversible but wide | shared utility, schema addition | deterministic checks + clean trajectory |
| Hard to reverse | migrations, deletions, prod data, money | stay human-gated |

Evidence priority inside open lanes: **deterministic** (tests/types/schema/sandbox) → **trajectory for this agent version** → **history/rollback rate** → model self-assessment **last**. Shadow-mode first; track gate–human disagreement until near zero. Green suites can still guard a falling product (tests converge on tests, not the spec).

## Discipline (closing)

1. Measure the path, not only the answer.
2. A verdict that does not change what runs next is a report.
3. Any failure not turned into a permanent test will return.

> The model on your card statement is a rental. The examiner around it is the only part you keep.

## Why it matters

Practical production recipe for **auto-merge gates** on agent work: treat evals as control surfaces and blast-radius policy, not confidence thresholds. Complements trajectory judges, trace-mining loops, and harness verification essays already in the vault.

## Related

- [[agent-as-a-judge-trajectory-evals-aparna]]
- [[do-automated-evals-work-parlance-labs]]
- [[improving-agents-data-mining-traces]]
- [[continual-learning-replit-agent-vibench]]
- [[why-harness-engineering-is-so-hard-winterarc]]
- [[agent-workflows-silent-degradation-verification-vladic]]
- [[own-your-intelligence-harrison-chase]]
- [[learn-harness-engineering]]
- [[langchain-fireworks-trace-judge-100x-cheaper]]

## Source

https://x.com/hanakoxbt/status/2083540339147567268
