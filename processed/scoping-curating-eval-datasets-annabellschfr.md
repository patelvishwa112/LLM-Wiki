---
tags: ["evals", "llm-judges", "agents", "agent-harness", "verification", "observability", "trace-data", "production", "regression-testing"]
source: https://x.com/annabellschfr/status/2085381643687047434
date: 2026-08-06
type: bookmark
description: "Eval dataset design before row writing — goal, sources, distribution, reference vs free eval, schema, 15-30 MVP rows, then expand from runs."
author: annabellschfr
summary: "Eval dataset design before row writing — goal, sources, distribution, reference vs free eval, schema, 15-30 MVP rows, then expand from runs."
raw: "[[raw/annabellschfr_2085381643687047434]]"
---

# Scoping and curating eval datasets (@annabellschfr)

## Key takeaways

When vibe-checking stops working, you need a **repeatable eval dataset**: same inputs over time → metrics, compare changes, catch regressions before users.

Design work comes **before/while** creating items. Start **minimally complete**: **~15–30 rows**, important slices, evaluator or review rubric — run early, fix schema/evaluator, then expand.

Expect **multiple datasets** (subsystem or step-scoped). Split when jobs differ in inputs, evaluators, or release decisions.

### Seven design steps

1. **Goal** — smallest useful job (common E2E first; later step-level, adversarial, red-team). Boundary: E2E payload vs step state.
2. **Sources** — inspect samples of production traces (scores/tickets as signals), existing assets (FAQs/docs/CSVs/benchmarks), synthetic gap-fills.
3. **Input distribution** — deliberate mix of scenario type × difficulty/risk × dataset role (typical / regression / failure / synthetic). Need not mirror production frequency; make mix visible in metadata.
4. **Evaluation style first** — **reference-based** (known target: label, tool call, answer) for CI/regression; **reference-free** (rubric: JSON, grounding, safety, tone) when no single correct output. Prefer cheapest evaluator that works (code → LLM-judge → manual).
5. **Item schema** — stable contract: `input`, `expectedOutput` (omit if free), `metadata` (source, scenario, difficulty, role, review status). Keep behavior-shaping fields; no arbitrary per-row junk.
6. **Draft MVP** — common paths + few hard/risky + known failures + synthetic only for named gaps. Do not wait for “complete.”
7. **Run then expand** — validate shapes; add/edit/archive from failures and product drift.

### Evolution patterns

- Production-mirroring  
- Bad-trace expansion (every serious failure → reviewed item)  
- Purpose-specific sets (regression vs adversarial vs single-step)

### Practice

One release question → smallest E2E dataset that answers “can this ship?” → every row runnable and scorable → expand after first run.

## Why it matters

Operational counterpart to agent-as-a-judge and eval merge-gates: how to **scope and grow** the dataset itself so scores stay interpretable. Langfuse-adjacent practitioner framing (academy links in source).

## Related

- [[eval-engineering-merge-gate-hanakoxbt]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
- [[do-automated-evals-work-parlance-labs]]
- [[improving-agents-data-mining-traces]]
- [[continual-learning-replit-agent-vibench]]
- [[writing-good-skills-measured-rulebook-aparna]]
- [[dear-lord-no-wonder-evals-are-a-mess]]

## Source

https://x.com/annabellschfr/status/2085381643687047434
