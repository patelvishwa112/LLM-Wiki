---
tags:
- claude-code
- architecture
- agent-engineering
- harness-engineering
- paper
- hermes
- openclaw
source: https://github.com/VILA-Lab/Dive-into-Claude-Code
date: 2026-06-05
type: resource
author: VILA-Lab
paper: https://arxiv.org/abs/2604.14228
description: Dive into Claude Code (VILA-Lab)
---

# Dive into Claude Code (VILA-Lab)

**What it is:** A comprehensive source-level architectural analysis of Claude Code v2.1.88 (~1,900 TypeScript files, ~512K lines) by VILA-Lab, combined with a design-space guide for agent builders and cross-system comparisons. Published as an academic paper (arXiv: 2604.14228).

## Key Findings

- **1.6% AI, 98.4% infrastructure.** The agent loop is a simple while-loop. The real complexity is permission gates, context management, tool routing, recovery logic, and 5-layer compaction. As models converge in capability, the harness becomes the differentiator.
- **5 values → 13 design principles → implementation.** Every design choice traces back to: Human Decision Authority, Safety/Security/Privacy, Reliable Execution, Capability Amplification, Contextual Adaptability.
- **7 independent safety layers** with shared failure modes. 50+ subcommands bypass security analysis. 4 CVEs reveal a pre-trust execution window.
- **9-step turn pipeline:** Settings → State init → Context assembly → 5 pre-model shapers → Model call → Tool dispatch → Permission gate → Tool execution → Stop condition.

## Architecture Deep Dives Covered

- **Agentic Query Loop:** ReAct-pattern while-loop as AsyncGenerator. 5 compaction stages before every model call. Max output token escalation (3 retries).
- **Safety & Permissions:** 7 permission modes on graduated trust spectrum. Deny-first evaluation. Auto-mode classifier (yoloClassifier). Permissions never restored on resume.
- **Extensibility:** 4 mechanisms at graduated context costs (Hooks → Skills → Plugins → MCP). 27 hook events, 10 plugin component types. 3 injection points: assemble(), model(), execute().
- **Context & Memory:** 9 ordered context sources. 4-level CLAUDE.md hierarchy. File-based memory (no vector DB). LLM-based file-header scan selects up to 5 relevant files.
- **Subagent Delegation:** 6 built-in types. Sidechain transcripts — only summaries return to parent. SkillTool (injects into context) vs AgentTool (isolated context).
- **Session Persistence:** Append-only JSONL transcripts. Chain patching for non-destructive compaction boundaries. Permissions never restored on resume.

## Cross-System Comparison: Claude Code vs OpenClaw vs Hermes-Agent

The repo includes a detailed comparison across 6 design dimensions: system scope, trust model, agent runtime, extension architecture, memory & context, multi-agent architecture. Three conclusions:

1. **Deployment context drives design** — per-user coding CLI → per-action approval; multi-channel gateway → perimeter trust; multi-deployment agent → opt-in isolation + swappable backends.
2. **Extension layer is where differentiation lives** — Claude Code stratifies by context cost, OpenClaw uses registry-managed capabilities, Hermes-Agent ships bundled plugins + dual MCP/ACP server surfaces.
3. **Memory sits on a spectrum** — file-based Markdown (Claude Code), file-based + optional vector + dreaming (OpenClaw), FTS5 + 8 swappable plugin backends (Hermes-Agent).

## Build Your Own Agent: Design Guide

Not a coding tutorial — a guide to 6 design decisions every agent builder must make: reasoning placement, safety posture, context management, extensibility, subagent architecture, session persistence.

## Related

- [[learn-harness-engineering]]
- [[feedback-loops-claude-code-less-babysitting]]
