---
tags: ["observability", "traces", "llm-ops", "clustering", "braintrust", "clio", "agents"]
source: https://x.com/ankrgyl/status/2062635408182427859
date: 2026-06-04
type: bookmark
author: "Ankur Goyal (Braintrust CEO)"
raw: "[[raw/ankrgyl_2062635408182427859]]"
related: []
---

# How Braintrust Made Continuous Trace Intelligence Possible at Scale

## Key Takeaways

- **Don't embed the trace — embed a facet of it.** The core insight (inspired by Anthropic's Clio paper): ask an LLM to summarize a trace along a single dimension in 1-2 sentences, then embed THAT. A million-token agent trace doesn't fit in an embedding model's context window and produces noisy clusters. A short, on-topic summary embeds cleanly.
- **Six-stage pipeline: preprocess → facet → embed → cluster → name → classify.** Key optimizations: facets batched into single LLM call (trace tokens paid once), HDBSCAN for clustering (no pre-specified cluster count, natural outlier detection), no LLM at classification time (nearest centroid lookup, ~100ms per trace).
- **Active observability runs continuously, not as batch.** Minimum 400 traces / 100 unique facet summaries before generating topic maps. Two views: persistent automated topic map for trend dashboards and alerting, and ad hoc clustering for exploration. Cluster identity stable across regenerations via predecessor matching.
- **Agent traces are fundamentally different from traditional NLP inputs.** They're millions of tokens, arrive at high volume, keep updating after completion, and interesting behavior lives in a few spans out of hundreds. Standard tools (topic modeling, sentiment analysis, embedding clustering) fail on this shape.

## Summary

Ankur Goyal describes Braintrust's Topics feature — a continuous intelligence layer that automatically discovers patterns in production LLM traces. The architecture is built on one key bet: instead of trying to embed/classify raw traces, use an LLM to produce a focused one-sentence summary per dimension (facet), then run traditional clustering on those clean short summaries. The pipeline handles millions of tokens by preprocessing to 128K, batching facets into one LLM call, and using HDBSCAN+UMAP+c-TF-IDF for unsupervised topic discovery — all without an LLM call at classification time.
