---
tags: ["agent-harness", "claude-code", "mcp", "tools", "cost-optimization", "agent-memory", "sub-agents", "code-review", "prompt-engineering", "agents"]
source: https://x.com/dunik_7/status/2064342854051209338
date: 2026-06-09
type: article
authors: ["dunik"]
title: "6 MCP servers, 0 calls, $280K wasted — the harness is the product"
summary: "A 5-dev team burns ~$280K/year running Claude Code with no harness: dead MCP tools taxing every request, no map re-explaining context, no memory re-litigating decisions, no sub-agent team or review gate. The fix is four layers: THE MAP (CLAUDE.md, DESIGN.md), THE MEMORY (decision logs, ADRs), THE HANDS (tool audit — cut everything unused), and THE TEAM (sub-agents with independent review gate). Same model. Different harness. Different outcome."
raw: "[[dunik_7_2064342854051209338]]"
related: ["[[agent-first-vs-prompt-first-design]]", "[[claude-code-dynamic-workflows-intro]]", "[[harness-is-the-product-context-aware-agents]]", "[[claude-managed-agents]]"]
---

# The Harness Is the Product

## The Numbers

**~$1,083/week per developer wasted without a harness:**
- $108/week: dead tools injecting schema into every request
- $375/week: no map, re-explaining stack every session
- $150/week: no memory, redoing ruled-out approaches
- $450/week: no team/gate, reverting and debugging by hand
- **Team of 5: ~$280,000/year**

## Four Harness Layers

### 1. THE MAP (files read before touch)
- CLAUDE.md: stack, hard rules, file placement. Layered: personal → project → path. **Every time the agent is wrong, add one line.** His had 30+ rules by launch
- PRODUCT.md, DESIGN.md, CONTEXT.md, docs/agent-docs/
- Mistake: writing it once and forgetting it

### 2. THE MEMORY (two circuits)
- Circuit 1: task dependency graph (beads: 1,006 tasks, 48 ready)
- Circuit 2: written paper trail (162 plans, 157 specs, 48 reviews, 15 ADRs)
- Files: MEMORY.md (decision log), ERRORS.md (failure log for 2+ attempts), docs/adr/
- "The documentation IS the memory. The memory IS the moat."
- Mistake: keeping decisions in head or Slack

### 3. THE HANDS (tool audit)
- 13 plugins + custom MCP servers. 6 servers: ZERO calls across 98 sessions
- 80K-star "memory" plugin: 700MB, 5 CPU cores pinned
- Every connected tool injects schema into EVERY request. 36M wasted tokens/month
- Audit prompt: sort into KEEP/WATCH/CUT, default to cutting
- Mistake: adding tools "to be safe"

### 4. THE TEAM (sub-agents + review gate)
- Sub-agent breakdown: code-review (36), backend (31), explore (31), frontend (20), architect/security (6)
- Builder and reviewer MUST be different agents — self-grading is theater
- Hooks enforce discipline: session start, pre-compaction, post-edit lint, locked folder blocks, task completion quality gates
- Flow: context → brainstorm → plan → delegate → TDD → review → close

## The Key Insight

Same model. Same subscription. Same prompts. The agent that shipped 5 production services across 98 sessions runs the exact same model as the one that breaks in someone else's demo. It just had a map, a memory, hands it actually used, and a team.
