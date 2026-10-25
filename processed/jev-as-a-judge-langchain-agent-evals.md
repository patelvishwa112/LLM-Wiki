---
title: Jev-as-a-Judge for Agent Evals
type: bookmark
description: "LangChain benchmarks TypeSafe's Jev as an agent judge: 500/500 agreement with a human oracle on binary pass/fail, 92-913x lower score variance than GPT-5.6 Luna/Terra and Claude Sonnet 4.6, at $0.00035 per call."
tags: [evals, llm-judges, cost-optimization, benchmarks, langchain, inference]
source: https://x.com/LangChain/status/2101454284927959080
date: 2026-09-19
author: LangChain
summary: "LangChain benchmarks TypeSafe's Jev as an agent judge: 500/500 agreement with a human oracle on binary pass/fail, 92-913x lower score variance than GPT-5.6 Luna/Terra and Claude Sonnet 4.6, at $0.00035 per call."
raw: "[[raw/LangChain_2101454284927959080]]"
---

# Jev-as-a-Judge for Agent Evals

**Source:** LangChain, 2026-09-19. A LangChain engineering post by Daniel Shea and Seán Roche testing TypeSafe AI's Jev as a third category of agent evaluator alongside code-based checks and LLM-as-a-judge.

The argument is that agent evaluation is fundamentally a decision task — given a state, return a score — while autoregressive judges reach that decision by generating text and then parsing it back into a score. Jev, which TypeSafe calls a "System One" model, skips generation entirely: it evaluates typed questions against structured state and returns typed answers with probabilities and confidence. It supports three question types (a Choice returning a probability from 0.0 to 1.0, a Score against an ordered rubric, and a "Noul" yes/no probability), and several atomic questions can be evaluated in parallel against the same state. LangChain's hypothesis is that matching the model shape to the task shape — decide, don't narrate — should show up as lower latency, lower cost, and lower variance.

The experiment is deliberately controlled. A weather agent built on Deep Agents produced five responses, which were frozen as a LangSmith dataset so every judge saw identical agent behaviour; a human labelled those same responses against the rubric as an oracle. Each judge then scored them 100 times on two signals: `quality` (continuous) and `does_pass` (binary). Accuracy means agreement with the oracle; precision/variance means reaching the same verdict on unchanged behaviour. Splitting the two matters because a judge can be perfectly stable and consistently wrong — variance alone is not quality.

The numbers favour Jev on every axis measured. On `does_pass` it matched the oracle on all 500 repeated decisions, against 99.8% for GPT-5.6 Terra, 96.4% for GPT-5.6 Luna and 80.0% for Claude Sonnet 4.6. Its mean per-case quality-score variance was 0.0000149, with Luna 433x, Terra 913x and Claude 92x higher. It also averaged 0.44s and $0.00035 per call, for $0.34 total against $28.17 on Claude. The authors are explicit that this is observational: five weather requests, one harness, one run, no Jev service version recorded and no temperature/top-p/seed set for the LLM judges, and the low variance cannot be causally attributed to Jev's training objective.

## Why it matters

Eval coverage has always been rationed by cost — when a judge call is expensive, teams choose between scoring more traces and staying inside budget, and the same tradeoff blocks online evaluation on production traffic. At roughly three hundredths of a cent per judgment, running several focused judges across a large share of traces becomes affordable, which turns evaluation from an offline gate into a continuous feedback signal. The variance result matters just as much for automation: an evaluator whose verdict flips between identical runs cannot gate a merge, no matter how accurate its average. The sober reading is that the direction is validated and the scale is not — LangChain itself frames the result as promising but early, and a cheap judge only amplifies feedback if it is aligned with human labels.

## Key points

- Jev matched the human oracle on 500/500 binary pass/fail decisions; GPT-5.6 Terra 99.8%, GPT-5.6 Luna 96.4%, Claude Sonnet 4.6 80.0%.
- Mean per-case quality-score variance: Jev 0.0000149, Claude 92x, Luna 433x, Terra 913x higher.
- Cost and latency: 0.44s and $0.00035 per call, $0.34 for the whole run vs $28.17 on Claude.
- TypeSafe's own claim: up to 200x faster inference and 400x lower cost than comparable LLMs on classification tasks.
- Jev is not an LLM — it returns typed answers and probabilities rather than generating text, so no output parsing step exists between judgment and score.
- Question types: Choice (0.0-1.0 probability), Score (rubric, e.g. 1-5), Noul (yes/no probability); multiple atomic questions run in parallel on one state.
- Method: fixed captured runs replayed from a LangSmith dataset plus a human oracle, so accuracy and repeatability are measured separately.
- "Signal value" is defined as oracle agreement times repeatability, which penalises consistently wrong judges that a raw variance number would flatter.
- Stated caveats: five weather requests, one harness, observational result, and low cost amplifies a misaligned judge across thousands of traces.

## Related

- [[jev-as-judge-probability-uncertainty-signal]]
- [[jev-reward-model-rl-anti-slop-fireworks-sophiamyang]]
- [[llm-as-judge-architectures-runtime-joshrosen]]
- [[agent-as-a-judge-trajectory-evals-aparna]]
- [[langchain-fireworks-trace-judge-100x-cheaper]]
