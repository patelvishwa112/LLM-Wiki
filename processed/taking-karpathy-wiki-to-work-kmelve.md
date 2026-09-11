---
tags: ["second-brain", "knowledge-graph", "agents", "content-ops"]
source: https://x.com/kmelve/status/2095601256987492516
date: 2026-09-03
type: bookmark
description: "knut (@kmelve): Karpathy LLM wiki at org scale is ContentOps not DevOps; six ownership questions; entropy/drift; Sanity Context pitch."
author: kmelve
summary: "knut (@kmelve): Karpathy LLM wiki at org scale is ContentOps not DevOps; six ownership questions; entropy/drift; Sanity Context pitch."
raw: "[[raw/kmelve_2095601256987492516]]"
---

# Taking Karpathy's Wiki to Work

knut (@kmelve), Sanity. Karpathy's personal LLM wiki (~100 articles / 400k words, LLM writes, human rarely touches, index-then-drill) does not survive org entropy.

## Shift

How agents get context is solved (RAG, markdown, MCP, CLI). Who **owns** what becomes context, consistency, audit — that's ContentOps. Non-engineers use agents too; they will not live in git.

Karpathy's miniature: ingestion, IDE, Q&A, output, linting, extra tools. At work: owners, processes, audits, BYOA, decisions that survive a rebuild.

## Six questions

Ingestion sources + audit trail. IDE config approval. Q&A / BYOA. Single source of truth + provenance. Linting: who decides when the model flags a contradiction, and does the decision persist? Plumbing ownership / on-call.

Git-as-CMS for legal policy fails: Legal reviews documents with effective dates, not line diffs. Forks of Karpathy's gist independently invent drafts, locking, pinned overrides, per-audience wikis — i.e. a CMS.

Stale page used to mislead one human; behind an agent it misleads at machine speed.

Vendor for Sanity Context. Extract the **ContentOps vs repo** questions.

## Related

- [[karpathy-three-folders-compiler-v1lrok]]
- [[context-drift-ontology-ar9av]]
