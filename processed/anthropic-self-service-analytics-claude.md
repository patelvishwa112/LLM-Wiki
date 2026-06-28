---
tags:
- anthropic
- claude-code
- data-analytics
- skills
- enterprise
- evals
- agent-ops
- semantic-layer
- data-engineering
source: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
raw: '[[raw/anthropic-self-service-analytics-claude]]'
date: 2026-06-03
author: Chen Chang, Clement Peng, Justin Leder, Johanne Jiao, Josh Cherry (Anthropic)
type: bookmark
summary: 'Anthropic''s internal self-service analytics system: 95% of business queries
  automated via Claude at ~95% accuracy. Four-layer stack: data foundations (canonical
  datasets, colocated artifacts, metadata as product), sources of truth (semantic
  layer, lineage, business context), skills (pairwise routing + domain docs, 21% →
  95%+ accuracy), and validation (offline evals, ablations, adversarial review, provenance
  footers, active correction harvesting). Three failure modes: entity ambiguity, staleness,
  retrieval failure.'
related:
- '[[harness-engineering-2026-discipline]]'
- '[[claude-code-slash-command-library]]'
- '[[15-claude-skills-that-stuck-vaibhav-sisinty]]'
description: 'Anthropic''s internal self-service analytics system: 95% of business
  queries automated via Claude at ~95% accuracy. Four-layer stack: data foundations
  (canonical datasets, colocated artifacts, metadata as product), sources of truth
  (semantic layer, lineage, business context), skills (pairwise routing + domain docs,
  21% → 95%+ accuracy), and validation (offline evals, ablations, adversarial review,
  provenance footers, active correction harvesting). Three failure modes: entity ambiguity,
  staleness, retrieval failure.'
---

# Anthropic Self-Service Analytics with Claude

**Source:** Anthropic Data Science & Data Engineering team. 95% of business analytics queries automated via Claude at ~95% accuracy.

## Why Analytics ≠ Coding

Coding is open-ended with natural guardrails (docs, tests). Analytics has a single correct answer from a single correct source with no deterministic correctness proof. The complexity is in mapping a question to the right entities — SQL is trivial once that's done.

## Three Failure Modes

| Failure | Description |
|---------|-------------|
| **Entity ambiguity** | "Active users" has dozens of valid interpretations — agent picks wrong one |
| **Data staleness** | Schemas change, docs rot, answers go subtly wrong |
| **Retrieval failure** | Right info exists but agent can't find it in the search space |

## Four-Layer Stack

### 1. Data Foundations
- Canonical datasets: one governed answer per concept, aggressively deprecate duplicates
- CI-enforced standards: changes bypassing governed layer fail review
- Colocated artifacts: models, semantic layer, docs, dashboards in single repo
- Metadata as product: column descriptions, metric definitions, lineage, ownership

### 2. Sources of Truth (descending trust)
- **Semantic layer** → structurally required first path. LLM-auto-generated metrics were net-negative.
- **Lineage/transformation graph** → reason about upstream models, deprecation, grain
- **Query corpus** → raw retrieval added <1pt accuracy. Distill into reference docs instead.
- **Business context** → knowledge graph (roadmaps, org structure, decision logs)

### 3. Skills
- **Without skills:** 21% accuracy on evals
- **With skills:** 95%+ aggregate, ~99% in certain domains
- Pairwise pattern: knowledge skill (router) + unbook skill (process + reusable analysis patterns)
- Reference docs written for LLM retrieval with gotchas and routing triggers
- Maintenance: colocated in data repo, PR changing model must touch skill file (~90% compliance)
- Synced to plugin marketplace, cloud storage, MCP — same answer across Slack, IDE, dashboards

### 4. Validation
- **Offline evals:** dashboard-based + long-tail + harvested from stakeholder corrections
- **Ablations:** vary one component against fixed eval set. Key finding: raw SQL corpus access <1pt gain — bottleneck is structure, not access
- **Adversarial review:** +6% accuracy, +32% tokens, +72% latency
- **Provenance footer:** source tier, freshness, owner on every response
- **Active correction harvesting:** scheduled agent scans channels, drafts PR to fix reference doc

## Key Insight

> Collapse ambiguity into a single governed answer → make it discoverable → flag when either goes stale. That's the whole game.
