---
title: "The rise of the knowledge engineer"
type: bookmark
description: "Mintlify's Hahnbee Lee argues agents are now the primary audience for docs (66% of July 2026 traffic) and that a new 'knowledge engineer' role must own accuracy."
tags: [agents, documentation, enterprise, content-strategy, knowledge-work, context-engineering, rag]
source: https://x.com/hahnbeelee/status/2100619585561256277
date: 2026-09-17
author: Hahnbee Lee
summary: "Mintlify's Hahnbee Lee argues agents are now the primary audience for docs (66% of July 2026 traffic) and that a new 'knowledge engineer' role must own accuracy."
raw: "[[raw/hahnbeelee_2100619585561256277]]"
---

# The rise of the knowledge engineer

**Source:** Hahnbee Lee (Mintlify), 2026-09-17. An X article making the case that documentation now has two audiences — humans and agents — and needs a dedicated owner.

The triggering statistic: in July 2026, agents accounted for **66% of measured web traffic** across documentation powered by Mintlify. That reframes docs as an agent-facing API surface rather than a human-facing publication. Lee's failure modes are operational rather than dramatic — an agent that cannot find an answer recommends a competitor, retrieves an obsolete API parameter and ships broken code, or picks the wrong one of two conflicting policies. The Air Canada chatbot ruling (BC Civil Resolution Tribunal, 2024) is the legal edge case: the airline was held liable for information on its website, including from its chatbot.

The proposed role is the **knowledge engineer**: someone who establishes authoritative sources and owners, wires product releases, code changes, and support tickets to content updates, publishes knowledge as Markdown, `llms.txt` indexes, APIs and MCP tools, defines terminology, permissions, and freshness standards, and measures what agents search for and where retrieval fails. Lee quotes practitioners who frame the same shift as "context curator" (Fabrizio Ferri Benedetti) and warns that the layer needs org-wide buy-in or "a real source of truth never happens" (David Hou, Decagon).

A useful sub-thesis: agents and humans want different documentation. Agents want exhaustive, structured detail — parameters, constraints, schemas, procedures. Humans want mental models and trade-offs, per Drew Breunig: "Humans don't require exhaustive documentation, they require mental models. Agents can find the details."

## Why it matters

Every team shipping an agent that reads company knowledge is implicitly betting on the quality of that knowledge, usually without an owner for it. This article names the missing accountability and gives concrete numbers for what bad knowledge costs: an agent that codifies one stale parameter reproduces the error across thousands of downstream interactions. For anyone building retrieval or MCP-backed assistants, the actionable shift is treating docs as a product with freshness SLOs and agent-traffic measurement, not a writing task.

## Key points

- Agents were **66%** of measured traffic on Mintlify-powered docs in July 2026.
- Air Canada was found liable by BC's Civil Resolution Tribunal for a chatbot's incorrect refund advice (2024).
- Coinbase cut documentation update time from **over 20 minutes to under 60 seconds**.
- HubSpot cut engineering resources spent on documentation infrastructure by **50%**.
- Knowledge engineer responsibilities: authoritative sources and owners, change-to-content linking, publishing as Markdown/`llms.txt`/APIs/MCP, terminology and review standards, and measuring unanswered agent queries.
- Splits the audience: exhaustive structured detail for agents, mental models for humans.
- Start by assigning accountability, not by creating a title.

## Related

- [[knowledge-system-compounding-obsidian-vellum]]
- [[open-knowledge-format-okf-google]]
- [[voxyz-ai-10-lessons-agents-md]]
- [[cerebras-knowledge-base-hybrid-search-mcp]]
