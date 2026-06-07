---
tags:
  - agents
  - agent-harness
  - claude
  - skills
  - mcp
  - prompt-engineering
source: https://claude.com/blog/harnessing-claudes-intelligence
date: 2026-06-07
author: Anthropic (Lance Martin)
type: bookmark
summary: "Design patterns for building applications that keep pace with Claude's evolving intelligence — use what it already knows, ask what you can stop doing, and set boundaries carefully."
related:
  - "[[agent-harness-engineering-agentforge]]"
  - "[[claude-code-changed-what-agents-look-like]]"
  - "[[anthropic-claude-code-skills-lessons]]"
  - "[[harness-engineering-2026-discipline]]"
---

# Harnessing Claude's Intelligence

Three design patterns for building agent applications that adapt to Claude's improving capabilities while balancing intelligence, latency, and cost.

## Key Points

| Pattern | Principle | Implementation |
|---------|-----------|----------------|
| Use what Claude knows | Prefer tools Claude already understands deeply | Bash tool, text editor tool — Claude composes them into skills, programmatic tool calling, memory |
| Ask what you can stop doing | Re-test assumptions as Claude improves | Let Claude orchestrate its own actions via code execution, manage its own context via skills/compaction/subagents, persist context via memory folders |
| Set boundaries carefully | Harness provides structure for UX, cost, security | Maximize prompt cache hits; use declarative tools for security boundaries (gated actions, typed arguments, audit trails) |

## Core Patterns

**1. Let Claude orchestrate its own actions.** Instead of every tool result flowing through the context window, give Claude a code execution tool so it can filter, pipe, and chain tool calls programmatically. Only relevant output reaches context. On BrowseComp, this pattern lifted Opus 4.6 accuracy from 45.3% to 61.6%.

**2. Let Claude manage its own context.** Use skills with progressive disclosure (short YAML description pre-loaded, full content loaded on demand). Use context editing to remove stale content. Use subagents to fork into fresh context windows for isolated tasks.

**3. Let Claude persist its own context.** Compaction lets Claude summarize past context for long-horizon tasks. Memory folders let Claude write files and read them later. Opus 4.6 reached 84% on BrowseComp using compaction, vs. Sonnet 4.5's flat 43%.

**4. Maximize prompt cache hits.** Static content first, dynamic last. Append system reminders in messages rather than editing prompts. Don't switch models mid-session. Use tool search for dynamic tool discovery.

**5. Use declarative tools for security boundaries.** Promote actions to dedicated tools when they need UX gating, audit logging, or security checks. Reversibility is a good criterion — hard-to-reverse actions (external API calls) should be gated.

## Model Evolution Example

In Pokémon (a long-horizon game), Sonnet 3.5 treated memory as a transcript — 31 files of raw NPC dialogue after 14,000 steps, still in the second town. Opus 4.6 at the same step count had 10 organized files, three gym badges, and a learnings file distilled from its own failures.
