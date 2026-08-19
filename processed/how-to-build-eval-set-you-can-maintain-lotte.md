---
tags: ["evals", "observability", "agents", "llm-judges", "error-analysis", "production", "agent-ops", "langfuse", "verification"]
source: https://x.com/lotte_verheyden/status/2089838277729890437
date: 2026-08-18
type: bookmark
description: "Langfuse Academy — maintainable eval sets: goals vs guardrails vs ops; error analysis; filter one-time fixes; tie metrics to decisions; Goodhart."
author: lotte_verheyden
summary: "Langfuse Academy — maintainable eval sets: goals vs guardrails vs ops; error analysis; filter one-time fixes; tie metrics to decisions; Goodhart."
raw: "[[raw/lotte_verheyden_2089838277729890437]]"
---

# How to build an eval set you can maintain

@lotte_verheyden (Langfuse Academy): answer to “I have traces — how do I set up evals?” Focus = **choosing metrics you can keep**, not catalog shopping.

## Three metric roles

| Role | Question | Typical source |
|------|----------|----------------|
| **Goal metrics** | Is quality improving on what we’re building for? | Error analysis, product goals |
| **Guardrails** | Did we regress on something that must never break? | Requirements, compliance, incidents |
| **Operational** | Cost, latency, volume? | Tracing (often free) |

Use a mix. Push goals up; guardrails catch zero-tolerance fails; ops = visibility. **Fewer is better** — every metric is an evaluator + dataset to maintain; when everything is important, nothing is.

## Living artifact

North star drifts. Recurring **manual sample of traces** finds uncovered failures and stale metrics after prompt/model/feature changes.

## Where candidates come from

1. **Observed failures** (default) — structured **error analysis** on real traces; write evals for errors you see, not imaginary ones.  
2. **Goals & hard constraints** — compliance, safety, format contracts → guardrails from day one even if never broken.

Metric catalogs (hallucination, toxicity, helpfulness) = exploration only; **tailor to product failure modes**.

## Filters: what deserves a metric?

### One-time fix vs generalization

Prompt-only fixes → fix and drop (invalid JSON, date format, markdown vs plain text, “disclose you’re AI”).

Keep tracking when simple prompts don’t solve:

- Answer supported by retrieved context?  
- Right context fetched?  
- User request actually answered?  
- Right tool + args?

### Tie to a decision

If the score moves, what changes — block deploy, roll back prompt, open investigation? No action → noise.

Bad: conversation length (engagement and stuck look the same). OpenAI receipt walkthrough: merchant-name wrong 85% but uncorrelated with audit decision → stopped tracking.

### Budget

Code evaluators ≈ free. LLM-as-judge costs money + maintenance. Drop expensive nice-to-haves.

## Bootstrap from zero

1. Two generic scores: free-text note (“what happened + what’s wrong”) + pass/fail  
2. Label **30–50** traces  
3. Cluster notes → named failure categories  
4. One **boolean** metric per major category  

= error analysis.

## Keep alive

- Re-run error analysis after big changes  
- Retire non-guardrail metrics stuck at 100% for months  
- **Goodhart** — re-validate optimized metrics against fresh human labels  

## Start

Error analysis → goals/constraints as observable signals → apply filters → implement evaluators (Langfuse Academy deep dive on writing them).

## Why it matters

Practical anti-catalog discipline for agent eval stacks. Complements eval-engineering merge gates, trajectory judges, and small MVP datasets.

## Skeptical read

Langfuse Academy CTA. Framework is vendor-neutral and strong even without Langfuse.

## Related

- [[eval-engineering-merge-gate-hanakoxbt]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
- [[do-automated-evals-work-parlance-labs]]
- [[scoping-curating-eval-datasets-annabellschfr]]
- [[generative-verifiers-genrm-deepmind]]
- [[agent-workflows-silent-degradation-verification-vladic]]
- [[how-to-become-applied-ai-engineer-eyad-khrais]]
