---
source_url: https://x.com/quarqlabs/status/2061571757488972153
title: "98.2% on LongMemEval: How We Built an Open-Source Agent That Actually Remembers"
author: "@quarqlabs (Quarq)"
published: 2026-06-01
ingested: 2026-06-01
platform: X (Article)
tags: ["agents", "memory", "evals", "architecture"]
stats: "7.4K views, 122 bookmarks"
---

# 98.2% on LongMemEval: How We Built an Open-Source Agent That Actually Remembers

## Architecture

Quarq Agent uses three specialized LLMs instead of one:
- **Retrieval Planner (gpt-4o-mini):** HyDE query expansion, generates structured retrieval strategy
- **Generator (gpt-4.1):** Response generation only, receives retrieved memories + procedural rules + conversation history
- **Learning Model (gpt-4.1):** Targeted edits — adds new facts, updates outdated facts, deletes contradictions

Three memory layers:
- **Semantic:** events and interaction history (what happened, when, who involved)
- **Procedural:** behavioral and operational rules
- **Episodic:** conversational and contextual experiences

## Key Components

**Hybrid Retrieval:** vector similarity + keyword search + metadata filtering + temporal validation

**Temporal Truth Protocol:** Separates storage date, event date, narrative date, and relative dates. Hard-coded rules: never use bracketed timestamps as event dates, never infer dates from neighboring memories, never assume unrelated memories refer to same entity.

**Self-Correcting Two-Pass Retrieval:** If first pass doesn't provide enough evidence, generator requests additional retrieval with broader threshold (0.28), merges new memories, regenerates under stricter anti-hallucination constraints.

**Quantitative Fidelity:** For totals, durations, prices, quantities — explicitly identifies actor/entity, measured action, target event/object, required exactness. Excludes merely nearby numbers.

**Background Learning:** Async after every response, semaphore limit of 4 concurrent tasks, persistent retry with exponential backoff.

## Results

98.2% on LongMemEval-S (500 questions, ~57M tokens, ~50 sessions per question). Uses less capable generator (gpt-4.1) than competitors (gpt-5-mini, gemini-3-pro). Local-first with FAISS.

## Evolution

Started as raw flat .txt files. Each component emerged from a specific failure mode:
- HyDE from single-vector retrieval missing relevant memories
- Temporal Truth Protocol from temporal hallucinations
- Two-pass fallback from models fabricating answers instead of admitting insufficient context

Core insight: "A single LLM cannot simultaneously optimize for retrieval quality, generation quality, and cost efficiency."

Open source: github.com/quarqlabs/agent-oss (Apache 2.0)
