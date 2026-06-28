---
tags:
- agents
- agent-harness
- context-engineering
- vertical-agents
- systems
source: https://x.com/brainsandtennis/status/2065190286519906657
date: 2026-06-11
type: bookmark
author: brainsandtennis
summary: 'Peter Wang on building production-grade vertical agents: treat context as
  a CPU-style L1/L2/L3 memory hierarchy, invest heavily in compressing the common
  case (L1), defer occasional capabilities to on-demand curated specs (L2), and provide
  a bounded escape hatch to the raw API via a mining skill (L3). One execute_code
  tool beats many narrow tools.'
raw: '[[raw/brainsandtennis_2065190286519906657]]'
description: 'Peter Wang on building production-grade vertical agents: treat context
  as a CPU-style L1/L2/L3 memory hierarchy, invest heavily in compressing the common
  case (L1), defer occasional capabilities to on-demand curated specs (L2), and provide
  a bounded escape hatch to the raw API via a mining skill (L3). One execute_code
  tool beats many narrow tools.'
---

# Building a Good Vertical Agent

Peter Wang (@BrainsAndTennis) shares hard-won principles from building Shortcut, the spreadsheet agent used inside major hedge funds where accuracy is non-negotiable.

## Core Thesis
A good agent is a **faithful compression of its task distribution**.

Users bring a long-tailed distribution of tasks. The agent cannot hold everything in context without bloating the prompt. The goal is to minimize context spent per task, averaged over the distribution — exactly like a CPU cache hierarchy.

## The L1 / L2 / L3 Context Hierarchy

**L1 — Always Resident (the 80%)**
- Lives in the system prompt.
- Bread-and-butter operations that dominate every session.
- Must be brutally token-efficient, consequence-reporting, and feature-engineered.
- Example: highly compressed cell-range reading/writing with formula aliasing, free row/column context, style grouping, and structured diff reporting after writes.

**L2 — On Demand (the ~15%)**
- Curated English specs fetched via a single discovery call (e.g., `getPivotTableInfo()`).
- Important but occasional capabilities (pivot tables, charts, conditional formatting, etc.).
- Written as hand-crafted prose that includes gotchas and canonical recipes, not just API signatures.
- Costs zero tokens until needed.

**L3 — Escape Hatch (the long tail)**
- The complete raw API reference (70k lines) lives on disk.
- A short `skill.md` teaches the agent how to mine it with a bounded number of grep calls.
- The system prompt explicitly tells the model when to descend: "If the wrapped API can't do it, use the raw API — don't compromise."

## Key Design Choices

- **One tool, not thirty**: A single `execute_code` tool that lets the model compose capabilities in a real programming language. Adding more narrow tools degrades model accuracy.
- **Compression is everything** in L1: formula normalization, header inference, style grouping, sampled diffs with "Cells that need review" triage.
- **The hierarchy drifts** as models get stronger — yesterday's L3 becomes tomorrow's L2.

## The Recipe (Portable to Any Domain)

1. Identify the steep part of your task frequency curve → wrap it ruthlessly into L1.
2. Write curated, gotcha-aware English specs for the important-but-occasional stuff → L2.
3. Provide a complete raw substrate + a short mining skill → L3.
4. Make the escape path explicit in the prompt.

This is directly relevant to Hermes agent design, skill authoring, and context management in multi-step agent workflows.