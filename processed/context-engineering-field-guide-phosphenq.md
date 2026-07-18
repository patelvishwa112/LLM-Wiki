---
tags:
  - context-engineering
  - prompt-engineering
  - agents
  - agent-harness
  - context-management
  - context-rot
  - compaction
  - subagents
  - token-economy
source: https://x.com/phosphenq/status/2078221723409830336
date: 2026-07-18
type: bookmark
description: "Phosphenq field guide: context engineering designs the whole window (not one prompt); bigger windows worsen via Lost-in-the-Middle and context rot; 12 moves for high-signal tokens."
author: phosphenq
summary: "Phosphenq field guide: context engineering designs the whole window (not one prompt); bigger windows worsen via Lost-in-the-Middle and context rot; 12 moves for high-signal tokens."
raw: "[[raw/phosphenq_2078221723409830336]]"
published: 2026-07-17
---

# Context engineering field guide (12 moves)

@phosphenq long-form (Jul 2026): context engineering replaced prompt engineering as the leverage skill. Karpathy: fill the window with the right information for the next step. Lütke: provide all context so the task is plausibly solvable.

## What changed

A modern answer comes from the full window (system, history, retrieval, tools, memory), not the typed sentence alone. Prompting was swallowed, not killed — still fine for one-shot chat; decisive when sessions are long or agentic.

## Why bigger is worse

- Lost in the Middle: U-shaped attention; middle of long context is weak.
- Chroma 2025: reliability falls as length grows, before "full."
- Coherent stuffed context can hurt more than messy text.
- Cost + accuracy tax; Anthropic attention budget / diminishing returns.

## 12 moves (condensed)

1. System prompt at right altitude  
2. Spend tokens like money (subtract)  
3. Just-in-time retrieve  
4. Compact before rot  
5. Examples over essays  
6. Label blocks  
7. Stable first; hinge fact on edges  
8. External memory file  
9. Sub-agent for heavy reading  
10. Tools as clean API + pinned schema  
(+ supporting framing moves in the original list numbering)

## Related

- [[harness-is-the-product-context-aware-agents]]
- [[how-to-use-rlms-in-deep-agents]]
- [[loop-engineering-clearly-explained]]
- [[hermes-agent-10x-faster-vault-index]]
- [[your-ais-memory-is-quietly-making-it-dumber]]
