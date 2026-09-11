---
tags: ["finance", "agents", "ontology", "knowledge-graph", "accounting"]
source: https://x.com/eya0/status/2097801524579864803
date: 2026-09-09
type: bookmark
description: "Erik (@eya0): AI accountants fail because the GL stores conclusions not stories; T:0 treats Pacioli double-entry as a proven ontology (objects, links, actions)."
author: eya0
summary: "Erik (@eya0): AI accountants fail because the GL stores conclusions not stories; T:0 treats Pacioli double-entry as a proven ontology (objects, links, actions)."
raw: "[[raw/eya0_2097801524579864803]]"
---

# Why Every AI Accountant Fails (and Why Palantir Knew First)

Erik (@eya0), T:0, 2026-09-09. X Article: Palantir made *ontology* famous; accounting already had one in 1494.

## Claim

Frontier models on a flat general ledger produce fluent, incompatible answers to "why did X move?" The GL stores **conclusions** (date, account, debit, credit, memo) and throws away the **story** (invoice → payment → payout → bank, fees, mods). Agents-on-the-old-ledger are faster bookkeepers. The ceiling is the substrate, not the model.

## Palantir parallel

Three primitives: **objects** (typed nouns), **links** (relations), **actions** (governed verbs). Palantir builds this per customer because operations ontologies are bespoke. Accounting's ontology is **standard** (same ~30 objects across ERPs) and **provable** (debits = credits; a payment settles a specific invoice). ERPs store objects then flatten links at posting. The journal entry is where the story dies.

## T:0 connected accounting map (production)

Objects normalized at ingestion (e.g. "deposit" means three different events in QBO / NetSuite / bank). Links exist only when proven; gaps are recorded, not guessed. Actions are deterministic posting rules. **Read/write split:** AI proposes rules and explains via path traversal; a deterministic engine writes numbers. Never probabilistic posting.

On the map: "why" is a graph walk with evidence; rec is confirmation against predicted bank lines; audit is continuous traversal not sampling; close is a checkpoint; future work is forking the map and replaying what-ifs.

## Hard lessons

1. Normalization is the moat, not the model.
2. A 95% link is worse than no link in finance.
3. Trust comes from showing the path, not eloquent reasoning.

Vendor piece for T:0. Extract the **substrate-before-agents** thesis, not the customer list.

## Related

- [[graph-engineering-vs-rag-graphrag-sprytixl]]
- [[graphiti-knowledge-graph-agent-memory]]
- [[unified-memory-layers-entity-resolution]]
- [[thinking-database-infinite-context-polygres-daleverett]]
