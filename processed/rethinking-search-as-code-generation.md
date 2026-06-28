---
title: Rethinking Search as Code Generation
tags:
- search
- agents
- perplexity
- sac
- architecture
- code-generation
- agent-harness
source: https://research.perplexity.ai/articles/rethinking-search-as-code-generation
date: 2026-06-02
published: 2026-06-01
authors:
- Perplexity Research
type: article
raw: '[[raw/perplexity_rethinking-search-as-code-generation]]'
description: Rethinking Search as Code Generation
---

# Rethinking Search as Code Generation

Perplexity introduces **Search as Code (SaC)** — a new architecture where agents compose task-specific search pipelines from atomic primitives via generated Python code, rather than calling monolithic search endpoints.

## Key Takeaways

- Traditional search = monolithic pipeline with query params as the only control point. Three failure modes: coarse context, inability to leverage model domain knowledge, and inefficient serial control flow with context pollution.
- SaC has 3 layers: **Models** (control plane), **Compute Sandboxes** (deterministic execution), **Agentic Search SDK** (composable search primitives).
- Code is both orchestrator AND gap-filler — models write code for capabilities not natively in the SDK.
- CVE case study: 100% accuracy with 85.1% fewer tokens vs baseline. Non-Perplexity systems all below 25%.
- Benchmark results: SaC wins 4/5 benchmarks. On WANDR, 2.5x better than next-best system.
- Cost-performance: SaC low-reasoning is cheaper than all competitors while beating two of them. Medium reasoning beats all non-SaC systems at <$1/task.
- SaC vs Perplexity's own non-SaC pipeline: +29% on DSQA, +45% on WANDR.
- Architecture insight: hybrid compute (token-space reasoning + deterministic runtimes + universal I/O) is the future.

## Architecture

### Why Traditional Search Fails for Agents

1. **Coarse context** — Monolithic pipelines aren't optimal across all query types. Low-recall queries get flooded; high-recall queries get starved.
2. **Domain knowledge goes unused** — Models may know the right strategy but can't implement it through query params alone.
3. **Inefficient control flow** — Fan-out, parallelism, dedup require repeated model turns, adding latency and polluting context.

### SaC's Three Layers

**Models (Control Plane):** Reason about directives, decompose into subtasks, decide retrieval pipelines, generate code.

**Compute Sandboxes:** Secure code execution runtimes. Filesystem-based serde for cross-turn state management (chosen over REPL for better long-trajectory reliability).

**Agentic Search SDK:** Not a wrapped API — the search stack was rearchitected into composable primitives. Python-based. Continuously improved via autoresearch loop. Agent Skills (<2000 tokens) teach models to compose primitives.

### Code as Gap-Filler

Example: complex regex not supported by search syntax. Instead of approximating and filtering in token space, the model generates code that makes parallel SDK calls for a superset, deduplicates, then applies the exact regex deterministically.

## Case Study: CVE Vendor Advisories

Task: identify 200+ high-severity CVEs (2023-2025) with vendor advisory citations, product names, and fix versions.

**Results:** 100% accuracy, 42.9K tokens vs 288.7K baseline (85.1% reduction).

Three phases:
1. **Fan-out** — Encoded source-class rules (vendor-only, no NVD/MITRE) directly into query templates with site-scoped exact-phrase constraints.
2. **LLM as planner** — Summarized coverage gaps, asked model for targeted refinements, validated queries before execution.
3. **Schema verification** — Defined explicit CVE-to-version binding schema, deduped by CVE, rejected weak evidence.

## Benchmarks

| Benchmark | SaC | OpenAI | Anthropic | Exa | Parallel |
|-----------|-----|--------|-----------|-----|----------|
| DSQA | **0.871** | 0.733 | 0.815 | 0.530 | 0.810 |
| BrowseComp | **0.805** | 0.720 | 0.598 | 0.380 | 0.560 |
| HLE | 0.612 | **0.614** | 0.566 | 0.387 | 0.515 |
| WideSearch | **0.651** | 0.522 | 0.590 | 0.471 | 0.584 |
| WANDR | **0.386** | 0.130 | 0.152 | 0.057 | 0.126 |

**WANDR** (new benchmark, publishing soon) — "wide research" tasks requiring complex search orchestration. SaC leads by 2.5x. Still unsaturated at 0.386.

### Cost-Performance Frontier

On DSQA and WideSearch, all three SaC reasoning levels (low/medium/high) sit on the upper-right frontier. Low reasoning beats competitors on cost while matching or exceeding performance. Medium reasoning beats all non-SaC systems at under $1/task.

## Relevance to Hermes

SaC's architecture mirrors the agent-harness pattern used in Hermes — models as control plane, sandboxes for execution, and SDK-style tools as primitives. The insight that codegen + atomic primitives beats monolithic APIs is directly applicable to tool design. Key lesson: the SDK should expose the smallest useful building blocks, not pre-baked pipelines. The model is better at composing than we are at predicting compositions.

## Source

[Perplexity Research — Rethinking Search as Code Generation](https://research.perplexity.ai/articles/rethinking-search-as-code-generation)
