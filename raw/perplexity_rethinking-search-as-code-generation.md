# Rethinking Search as Code Generation

**Source:** https://research.perplexity.ai/articles/rethinking-search-as-code-generation
**Published:** June 1, 2026
**Authors:** Perplexity Research

---

Evolving search from monolithic services to programmable primitives for the era of agent harnesses.

## Introduction

Perplexity's search stack serves thousands of queries each second across their applications and API Platform. In September 2025, they published the first architectural overview of their search systems.

Traditionally, AI systems have treated search as a monolith: an AI model issues a query, the search engine runs its predefined pipeline, and the model consumes the results as context. This worked fine for early AI users, but today's agents complete tasks over hours or days with highly variable information needs.

The key bottleneck is control. Frontier models are good at reasoning over fixed context, but the most powerful AI systems need to steer how context is retrieved, processed, aggregated, and rendered.

## The Rigidity of Traditional Search

Traditional search pipelines are designed around a single point of control: the query parameters. Three recurring failure modes:

1. **Coarse context.** Models are sensitive to context quality and compactness, both query-dependent. Monolithic pipelines aren't optimal across all queries.
2. **Failure to leverage domain knowledge.** Models may know the right search strategy but can't act on it if it's not expressible through query parameters.
3. **Inefficient control flow and context pollution.** Many workflows need fan-out, parallel fetching, deduplication — nonlinear and async operations. Forcing these through repeated model turns adds latency and pollutes context.

## Search as Code (SaC) Architecture

Three tightly coupled layers:

1. **Models** serve as the control plane — reason about directives, decompose into tasks, decide retrieval pipelines, generate code.
2. **Compute sandboxes** provide deterministic compute through secure code execution runtimes — control flow, batching, retries, filtering, joining, aggregation.
3. **Agentic Search SDK** exposes Perplexity's search stack as composable primitives, from low-level retrieval to high-level semantic parsing.

### Agentic Search SDK

Not a preexisting API packaged as a library. The search stack was rearchitected into modular, composable primitives. High-level pipelines still available but as shorthand — models can use or bypass them.

- Runtime: Python
- Optimized via autoresearch loop running continuously over weeks

### Sandboxes

Secure environments for defining and running SaC pipelines. Key design consideration: managing intermediate states across turns.

- **Persistent filesystem + explicit serde:** Models serialize intermediate state across turns. More reliable on long trajectories. Adopted approach.
- **REPL:** Persist execution runtime across turns, reference variables by name. More token-efficient but namespace clutter degrades long-trajectory performance.

### Models

Frontier models are effective at general-purpose code generation. Challenge: inducing effective codegen for the custom SDK. Solution: highly-tuned Agent Skills (<2000 tokens in SKILL.md) with concise guidance and few-shot examples for composing building blocks into complex patterns.

## Case Study: CVE Vendor Advisories

Real-world task: identify and characterize 200+ high-severity CVEs from 2023-2025 with vendor advisory citations.

- SaC: 100% accuracy, 42.9K tokens
- Non-SaC baseline: 288.7K tokens (85.1% reduction)
- Non-Perplexity systems: all below 25% accuracy

Three-part code trajectory: (1) fan-out over official advisory formats with encoded source-class rules, (2) LLM as intermediate planning subroutine for sparse vendor-years, (3) result verifier with schema-defined CVE-to-version binding.

## Evaluation Results

Five benchmarks: DeepSearchQA (DSQA), BrowseComp, Humanity's Last Exam (HLE), WideSearch, and the new WANDR benchmark.

| Benchmark | Perplexity (SaC) | OpenAI | Anthropic | Exa | Parallel |
|-----------|-----------------|--------|-----------|-----|----------|
| DSQA | **0.871** | 0.733 | 0.815 | 0.530 | 0.810 |
| BrowseComp | **0.805** | 0.720 | 0.598 | 0.380 | 0.560 |
| HLE | 0.612 | **0.614** | 0.566 | 0.387 | 0.515 |
| WideSearch | **0.651** | 0.522 | 0.590 | 0.471 | 0.584 |
| WANDR | **0.386** | 0.130 | 0.152 | 0.057 | 0.126 |

SaC wins 4/5 benchmarks. On WANDR, 2.5x better than next-best system.

Cost-performance frontier: SaC's low reasoning setting is cheaper than all other systems while performing better than two of them. Medium reasoning outperforms all non-SaC systems at under $1/task.

## Key Insight

Search is a natural proving ground for hybrid architecture combining token-space reasoning (models) with deterministic compute (sandboxes) and universal I/O (search infrastructure). When these pieces are integrated and codesigned, the resulting system is dramatically more powerful and efficient.

SaC vs non-SaC on Perplexity's own infrastructure: +19.77 pp on DSQA (29% relative), +12 pp on WANDR (45% relative).
