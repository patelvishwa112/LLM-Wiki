---
tags: ["context-engineering", "loop-engineering", "prompt-engineering", "agents", "agent-harness", "claude-code", "subagents", "verification", "context-rot", "skills"]
source: https://x.com/vartekxx/status/2074864291568664646
date: 2026-07-08
type: bookmark
description: "Prompt→context→loop stack: Karpathy Software 3.0 (write/select/compress/isolate) + Cherny loops/verifiers on Claude Code."
author: vartekxx
summary: "Prompt→context→loop stack: Karpathy Software 3.0 (write/select/compress/isolate) + Cherny loops/verifiers on Claude Code."
raw: "[[raw/vartekxx_2074864291568664646]]"
---

# Context engineering as OS; loops as the kitchen (vartekxx)

Long-form synthesis: **prompt engineering is one instruction; context engineering is the OS; loop engineering automates context ops**. Same weights + question can yield large benchmark gaps (e.g. 0.637 vs 0.488) when only context structure changes. Shippers care more about context than model brand.

## Key takeaways

### Three stacked layers
1. **Prompt engineering** — craft one instruction.
2. **Context engineering** — design files, history, tools, rules the model sees.
3. **Loop engineering** — systems that run context ops repeatedly with verification.

Layers stack; a bad prompt in a good loop just produces bad work faster.

### Karpathy (Software 3.0)
- Model = CPU; context window = RAM; context is the programming surface.
- Four ops: **Write** (persist outside window: CLAUDE.md, skills, state), **Select** (relevant only), **Compress** (summarize stale; prioritize fresh tool results), **Isolate** (subagent "context firewall").
- Skip ops → **context rot** (cluttered window, worse decisions).

### Cherny (Claude Code)
- "I don't prompt Claude anymore. I have loops running that prompt Claude."
- Loop without context discipline = autopilot garbage.
- Five loop blocks: **Automation** (/loop, /goal), **Skill**, **Sub-agents** (maker/checker), **Connectors**, **Verifier** (tests/hooks). Verifiers claimed ~2–3× quality lift; without verifier it's self-agreement.

### Claude Code build path (high level)
- Curated CLAUDE.md (prefer short; ~150 instructions attended reliably).
- Specs over wishes; subagent isolation; hooks for non-negotiable gates.
- Self-improving context (write learnings → next run reads).
- /loop + /goal → Routines (24/7) → Dynamic Workflows (orchestration in code, not context).

### Limits
- More context ≠ better; noise drowns signal.
- Hallucinations remain; verifier mandatory.
- Skill is "what the model needs to see," not "what you want to say."

## Why it matters

Clean map of the vault's loop + context + Claude Code cluster in one place. Aligns with field guides, "loop ate prompt engineering," and vault/index patterns (write/select/compress outside the window). Practical ladder from CLAUDE.md → hooks → scheduled loops.

## Skeptical read
- Benchmark gap figures and "2–3× from verification" are author-asserted without methodology in-post.
- Part 4 promises copy-paste prompts; capture is somewhat condensed on the how-to section — use raw for full text if expanding implementations.
- Heavy Claude Code product surface (Routines, Dynamic Workflows) may date faster than the four ops.

## Source
https://x.com/vartekxx/status/2074864291568664646

## Related
- [[context-engineering-field-guide-phosphenq]]
- [[loop-engineering-quietly-ate-prompt-engineering]]
- [[loop-engineering-clearly-explained]]
- [[wtf-is-a-loop]]
- [[new-rules-context-engineering-claude-5-trq212]]
- [[harness-is-the-product-context-aware-agents]]
- [[how-to-create-loops-claude-code-sairahul1]]
- [[claude-code-four-loop-types-datasciencedojo]]
- [[own-your-intelligence-harrison-chase]]
