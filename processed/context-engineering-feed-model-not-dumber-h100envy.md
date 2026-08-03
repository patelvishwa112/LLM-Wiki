---
tags: ["context-engineering", "context-rot", "agents", "agent-harness", "attention", "rag", "compaction", "loop-engineering", "kv-cache", "prompt-engineering"]
source: https://x.com/h100envy/status/2082064768844837357
date: 2026-07-28
type: bookmark
description: "Context is a biased attention budget — lost-in-the-middle, RoPE decay, softmax sinks, dilution; spend edges deliberately, measure MECW."
author: h100envy
summary: "Context is a biased attention budget — lost-in-the-middle, RoPE decay, softmax sinks, dilution; spend edges deliberately, measure MECW."
raw: "[[raw/h100envy_2082064768844837357]]"
---

# Context Engineering: feed a model so it does not get dumber (@h100envy)

## Key takeaways

- **More context is not better.** Quality falls (often non-linearly) long before the advertised window. Chroma 2025 multi-model study cited.
- **Lost in the middle** (Liu et al., TACL 2024): U-shaped accuracy; middle can drop 30%+ vs edges. Agent greps that land key files mid-pack hit the blind spot.
- Three architectural rot mechanisms: **RoPE long-term decay**, **softmax concentration + attention sink**, **attention dilution** (n² relations stretch signal).
- Inference workarounds fail at the root: temperature doesn’t retune attention; reordering fights KV cache; long-context fine-tunes shift the cliff, don’t remove the U-shape.
- Coherent long docs can **hurt more than shuffled** (diffuse attention).
- **MECW** (maximum effective context window) can be orders of magnitude below marketed length on hard tasks — measure per domain.

## Practice (budget, not vessel)

1. **Retrieve less** — 3–5 reranked chunks beat top-20 dilution.
2. **Position on purpose** — instructions start; critical near end before question; least important middle.
3. **Compact often** — agent loops accumulate junk; summarize and drop dead turns.
4. **Isolate per task** — fresh short contexts (same spirit as stateless loop iterations / swarm workers).
5. Hybrid 2026 default: retrieve to narrow, then long-context **reason over the filtered set**.

Closing line: *Whoever fills the window degrades the model. Whoever spends the budget keeps it sharp.*

## Why it matters

Same-author series after loop-engineering technical roadmap. Ties field-guide / delete-audit context notes to architecture-level why.

## Related

- [[loop-engineering-technical-roadmap-h100envy]]
- [[context-engineering-field-guide-phosphenq]]
- [[context-engineering-delete-audit-free-ai-guides]]
- [[context-engineering-os-loop-engineering-vartekxx]]
- [[new-rules-context-engineering-claude-5-trq212]]
- [[loop-is-the-moat-rsi-m0egpt]]

## Source

https://x.com/h100envy/status/2082064768844837357
