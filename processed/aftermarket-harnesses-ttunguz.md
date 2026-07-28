---
tags:
- harness-engineering
- agent-harness
- cost-optimization
- prompt-caching
- venture-capital
- ai-economics
- ai-strategy
- cursor
- claude-code
- codex
- token-economy
- investing
source: https://x.com/ttunguz/status/2082158740107866459
date: 2026-07-28
type: bookmark
author: Tomasz Tunguz (@ttunguz)
raw: "[[raw/ttunguz_2082158740107866459]]"
description: "VC thesis — aftermarket harnesses move coding benchmarks more than model choice; Cursor vs native Codex/Claude Code deltas"
summary: "Tunguz argues AI harnesses (context, cache, retrieval, tools) now dominate quality and cost vs the underlying model, citing Endor Labs swings of +25.7 pts GPT-5.5 Codex→Cursor and Opus 4.7 Claude Code→Cursor."
---

# Aftermarket Harnesses

## Key takeaways

- **Harness > model on the same week’s evals:** Endor Labs Agent Security League — GPT-5.5 functional correctness 61.5% in native Codex vs 87.2% in Cursor (+25.7 pts). Opus 4.7: 87.2% Claude Code vs 91.1% Cursor. Both frontier models scored higher in a competitor’s harness than their maker’s.
- **Input is the bill:** OpenRouter traffic ~86–98% input tokens. Output ~5× per-token price but volume makes input dominate. Harness owns what context ships and what caches.
- **Cache discipline is the product surface:** Stable-prefix caching + dynamic content after the breakpoint (Lumer et al., arXiv:2601.06007) → ~41–80% cost cut and 13–31% faster TTFT across 500 long-horizon sessions; savings scale 500→50k token prompts.
- **Aftermarket can match first-party co-design:** Claude Code’s cache culture (~96% hit rate, shared system-prompt cache, forked sub-agents at ~99% byte-identity) is real — but Cursor mirrors dynamic tool fetching, priority-based prefix assembly, two-tier caching and posts the higher scores.
- **Metaphor:** harness is the jockey, not a “model wrapper.” Battleground shifts from breed (weights) to equipment (runtime).

## Summary

Short essay (X Article + tomtunguz.com, Jul 28 2026) extending Tunguz’s Hungry Hungry AI Model / harness-battleground line. Fulcrum claim: harnesses set cost, quality, and accuracy via context selection, retrieval precision, and caching — not the model alone. Notes OpenRouter confidence bands on the chart are pricing-derived proxies, not measured per-provider splits.

Citations: Endor Labs ASL (Open SusVibes / CMU), prior Tunguz posts, Lumer prompt-caching paper, Anthropic Claude Code caching blog, Digital Applied cache-first economics.

## Skeptical read

- One benchmark week (security/functional-correctness style league) is not universal SWE performance; harness×task interactions can reverse.
- Vendor and lab blog numbers on cache hit rates are self-reported; third-party replication varies by workload.
- “Aftermarket wins” can also mean Cursor optimized harder for that leaderboard’s agent loop shape.

## Related

- [[learn-harness-engineering]]
- [[why-harness-engineering-is-so-hard-winterarc]]
- [[harness-is-the-product-context-aware-agents]]
- [[harness-is-the-product-280k]]
- [[deep-agents-prompt-caching]]
- [[own-your-intelligence-harrison-chase]]
- [[how-to-build-custom-agent-harness-langchain]]
- [[glean-coding-harness-programmatic-tool-calling]]
- [[economy-of-tokens-vipulved-modular-ai]]
- [[the-untrainable]]
- [[how-to-build-company-os-kimi-k3]]
