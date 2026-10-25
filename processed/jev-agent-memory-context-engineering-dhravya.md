---
title: How Jev Changes Agent Memory and Context Engineering
type: bookmark
description: "Dhravya Shah maps a decision model onto every stage of the memory pipeline: reranking, chunking, pre-observation filtering, harness hooks — with costs and failures."
tags: [agent-memory, memory, retrieval, chunking, cost-optimization, context-engineering, agent-harness]
source: https://x.com/DhravyaShah/status/2103314339239428201
date: 2026-09-25
author: Dhravya Shah
summary: "Dhravya Shah maps a decision model onto every stage of the memory pipeline: reranking, chunking, pre-observation filtering, harness hooks — with costs and failures."
raw: "[[raw/DhravyaShah_2103314339239428201]]"
---

# How Jev Changes Agent Memory and Context Engineering

**Source:** Dhravya Shah (@DhravyaShah), founder of supermemory, 2026-09-25. A long exploration of where a fast "system 1" decision model (Jev, by @typesafeAI) fits into a production memory pipeline — including where it does not.

Shah first flattens every memory system he has studied (ChatGPT, Claude, Instinct, Openclaw, Hermes, Muse, and supermemory's own) into four shared stages: finding relevant information (grep or cosine, not necessarily RAG), chunking data so a model can observe it, observation/learning that runs *outside* the main agent loop on a schedule or trigger, and harness-specific logic that puts the resulting context back in front of the model. The insight is that Jev's profile — extremely fast, outputs structured choices and probabilities, poor at text generation — is a near-exact match for the small decisions inside those four stages rather than for the generation steps.

He then works through each stage with numbers. As a reranker on BEIR sets (SciFact, NFCorpus, TREC-COVID, FiQA, SCIDOCS), Jev beats BM25 by **+0.05 to +0.17 nDCG@10** every time, and a "Score-10" protocol was the strongest Jev-only variant (SciFact 0.751). But quality is mid-pack against dedicated rerankers — it edges bge-reranker-base (mean 0.612 vs 0.564 on three overlapping sets) at ~20× the cost ($0.00037/query vs $0.00002), loses to jina-reranker-turbo (0.612 vs 0.633), and trails monoT5 (0.766) and RankGPT-4 (0.756) on SciFact. Pricing sits next to Voyage ($0.042/MTok vs rerank-3 at $0.05/MTok), not next to BGE. One usage mode failed outright: using the model as a delete gate kept almost nothing.

The chunking and filtering results are the more interesting section. Asking, sentence by sentence, whether the sentence continues the previous thought gives cleaner boundaries than embedding-based, markdown-heading, or sliding-window chunking — including on messy multilingual data — at the cost of being far more expensive than the near-free alternatives. Placed *before* the observation model as a yes/no gate, the same per-sentence classification cut **58% of content tokens**. That gate is where the approach breaks: removing sentences independently severs context, because an early line in a legal document or conversation can be referenced much later, and assistant turns lose meaning when trimmed. Shah's verdict is that this makes Jev a weak *compactor*, even though it is a strong filter.

The last application is harness-level: in the supermemory Claude Code plugin, a Jev decision in the `UserPromptSubmit` hook chooses whether memory should be injected at all (average injection is ~250 tokens, and injection is always disclosed). This exploits a failure mode Shah names directly — models are bad at deciding *when* memory helps but good at using long context — while giving users a natural escape hatch: say "without using memory" and the decision model simply skips the search without a tool call.

## Why it matters

It relocates memory engineering from "bigger context window" to a stack of cheap binary decisions, which is where cost and latency actually live. The concrete asymmetry — 58% token savings on the observation path versus broken semantics when the same filter is used as a compactor — is a design rule worth copying: gate what enters the extractor, never rewrite what the extractor sees. It is also an honest cost table for anyone assuming decision models are automatically cheaper than purpose-built rerankers; at these prices they are not.

## Key points

- Four-stage memory pipeline: search → chunk → observe/learn off the main loop → harness reinjection.
- Reranking: +0.05 to +0.17 nDCG@10 over BM25 on SciFact, NFCorpus, TREC-COVID, FiQA, SCIDOCS; best Jev-only method (Score-10) hit SciFact 0.751.
- Reranking economics: Jev ≈ $0.00037/query (~20× bge-reranker-base), $0.042/MTok ≈ Voyage rerank-3; loses to jina-reranker-turbo (0.612 vs 0.633) and to monoT5 (0.766) / RankGPT-4 (0.756) on SciFact.
- Delete-gate usage failed (kept nothing); sort and score variants worked.
- Sentence-level boundary decisions made Jev the best chunker tested on internal messy, markdown, and multilingual sets — at high cost.
- Pre-extraction yes/no filter saved **58% of content tokens**, but independent sentence removal breaks cross-references (legal docs, assistant turns) → not viable as a compactor.
- Claude Code plugin: Jev decides in `UserPromptSubmit` whether to inject memory; ~250 tokens injected on average, user can opt out conversationally with no tool call.

## Related

- [[agent-memory-landscape-2026]]
- [[how-to-be-a-memory-engineer-n01ennn]]
- [[memory-engineering-forgetting-policy-leanxbt]]
- [[cerebras-knowledge-base-hybrid-search-mcp]]
- [[production-rag-agents-technmak]]
