---
tags: ["evals", "llm-judges", "error-analysis", "observability", "braintrust", "arize", "langsmith", "traces", "criteria-drift", "agents"]
source: https://parlance-labs.com/blog/posts/auto-evals/
date: 2026-07-11
type: article
description: "Parlance Labs (Saha, Husain): auto error-analysis on 100 leasing-agent traces — best system 87% recall of human labels, misses UX/product goals invisible in traces alone; keep human-in-the-loop."
author: Antaripa Saha, Hamel Husain
summary: "Parlance Labs (Saha, Husain): auto error-analysis on 100 leasing-agent traces — best system 87% recall of human labels, misses UX/product goals invisible in traces alone; keep human-in-the-loop."
raw: "[[raw/parlance_labs_auto_evals]]"
---

# Do Automated Evals Work? — Parlance Labs

Empirical head-to-head: human error analysis vs automated agents on **100 production apartment-leasing traces** (Nurture Boss), 39 hand-labeled failures. Same light prompt; labels masked.

## Headline results

| System | Recall | Precision | Discoveries | FPs |
|--------|--------|-----------|-------------|-----|
| Braintrust Loop | 87.2% | 79.1% | 20 | 9 |
| Codex / Factory Droid | ~84.6% | ~83% | 17–20 | 10–11 |
| LangSmith chat / Claude Code | ~79.5% | ~77% | 17–20 | 9–14 |
| Arize Alyx | 74.4% | **91.0%** | 19 | 3 |

- Strong on **obvious** failures: bad tool claims, broken follow-ups, contradictions with tool output.
- Every system found ~17–20 real issues humans missed.
- **Not a vendor ranking** (small failure set; one product domain).

## Systematic misses (all tools)

Failures that look fine in the transcript without product context:

- Giving up on sales objections
- Markdown in SMS
- Voice interruptions
- Missed human handoffs

Root issue: **criteria drift** — good/bad criteria emerge from reading data; tools don’t interview for business rules they weren’t given.

## Recommended workflow

Not one-shot “traces in → report out.” Instead:

1. Human annotates traces.
2. Agent watches annotations, builds taxonomy, proposes new instances.
3. Human accept/dismiss → product context compounds into evaluators.

Platforms beat coding agents on **ops** (trace-linked findings, re-run on new traffic); coding agents competitive on **finding quality**.

## Why it matters

Gives numbers behind “look at your data” vs fully automated Loop/Alyx/Engine hype. Auto-eval is high-recall assist, not a substitute for domain judgment on UX and business goals.

## Related

- [[agent-as-a-judge-trajectory-evals-aparna]]
- [[improving-agents-data-mining-traces]]
- [[langchain-fireworks-trace-judge-100x-cheaper]]
- [[continual-learning-replit-agent-vibench]]
- [[dear-lord-no-wonder-evals-are-a-mess]]
- [[how-to-become-applied-ai-engineer-eyad-khrais]]
- [[four-loops-ai-engineering-taxonomy-aparna]]
