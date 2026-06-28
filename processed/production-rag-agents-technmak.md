---
tags:
- agent-architecture
- agent-harness
- rag
- agents
- retrieval
- prompt-engineering
- agent-ops
source: https://x.com/technmak/status/2068683947899273295
type: bookmark
related:
- - 21-agent-building-mistakes
- - coding-agent-harness-eight-pillars
- - harness-engineering-2026-discipline
- - iii-agent-harness-workers
summary: '"@techNmak''s Part 2 post on production AI systems. Focuses on where real
  systems fail: retrieval (RAG pipeline stages from ingestion to evaluation) and agent
  design (tool design, observation, verification, memory, termination). Strong emphasis
  on ''Model proposes. System verifies. Tool executes.'' Includes practical interview
  scenarios that distinguish builders from readers."

  '
why_it_matters: '"One of the best single posts on practical RAG + agent engineering.
  Systems-thinking heavy, anti-hype, and laser-focused on production failure modes.
  Directly relevant to agent-harness design, verification loops, tool safety, memory
  architecture, and evaluation. Complements existing vault notes on agent building
  mistakes and harness engineering."

  '
description: '"@techNmak''s Part 2 post on production AI systems. Focuses on where
  real systems fail: retrieval (RAG pipeline stages from ingestion to evaluation)
  and agent design (tool design, observation, verification, memory, termination).
  Strong emphasis on ''Model proposes. System verifies. Tool executes.'' Includes
  practical interview scenarios that distinguish builders from readers."'
---

# Production AI Systems: RAG and Agents (Part 2)

**Source:** [X Post by techNmak](https://x.com/technmak/status/2068683947899273295)

This post is Part 2 of a series on building production AI systems. While Part 1 covered the model layer, this one addresses the two layers that actually cause most failures: **RAG** and **Agents**.

## Core Thesis
Production failures are rarely about the model lacking understanding of self-attention. They are about **retrieval** (right evidence never reaches the model) and **agent design** (tools, observation, planning, verification are fragile).

## RAG Pipeline Realities
RAG is a complex, multi-stage system where every layer can silently break downstream performance:

- Ingestion & Parsing (tables, headings, hierarchies, figures, PDFs)
- Chunking (structural and semantic > fixed-size; match document type and query patterns)
- Retrieval (hybrid dense + sparse + metadata filters wins in most real corpora)
- Re-ranking, metadata, freshness, versioning, access control (permissions enforced *before* model sees content)
- Evaluation (separate retrieval metrics from generation metrics; many "generation" failures are retrieval failures)
- Multimodal RAG (visual evidence often critical)
- Production concerns (embedding migration, prompt injection defense, grounding/citation)

## Agent Design Principles
An agent is a goal-pursuing, observing, replanning system — not just an LLM with tools.

- Prefer pipelines unless dynamic replanning is genuinely required
- Core principle: **Model proposes. System verifies. Tool executes.**
- Tool design: narrow, schema-validated, permission-checked, idempotent, clear success/failure signals
- Observation design is as critical as the tool itself
- Termination conditions, loop detection, step/budget limits, programmatic success checks required
- Memory must be deliberate (working/episodic/semantic/procedural) with attention to staleness, privacy, retrieval quality
- Multi-agent systems add coordination overhead — only use when clear justification exists

## Standout Value
The real-world interview scenarios at the end (50M vector migration, debugging confident-but-wrong RAG, fixing agent loops, multimodal failures, securing agents with sensitive actions) are excellent discriminators between people who have built systems and those who have only read blogs.

## Relevance to Vault
- Directly supports [[21-agent-building-mistakes]], [[coding-agent-harness-eight-pillars]], [[harness-engineering-2026-discipline]], and [[iii-agent-harness-workers]]
- Strong patterns around verification, tool safety, memory architecture, and evaluation
- Practical bridge between theory and production agent-harness implementation

**Related:** agent architecture, RAG pipelines, agent verification, tool design, memory systems, evaluation.