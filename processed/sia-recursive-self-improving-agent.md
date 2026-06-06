---
title: "SIA — Open Source Recursive Self Improving AI Agent (hexo.ai)"
tags: ["agents", "self-improvement", "rsi", "training", "slm", "open-source"]
source: https://x.com/rohanpaul_ai/status/2060063592448446778
date: 2026-05-30
published: 2026-05-28
authors: ["Rohan Paul", "Kunal Bhatia (hexo.ai)"]
type: article
related: ["[[raw/rohanpaul_ai_2060063592448446778]]", "[[processed/autoscientists-decentralized-ai-research-agents]]"]
---

# SIA — Self Improving AI Framework (hexo.ai)

## Key Takeaways

- First open-source framework that updates BOTH the outer harness AND model weights through task feedback
- 56.6% gain on LawBench, 91.9% runtime reduction on GPU kernels, 502% improvement on single-cell RNA denoising
- The loop: task attempt → feedback → scaffold change → model update → better attempt
- Agents stop being "frozen workers" — feedback actually changes internal parameters
- Paper: arxiv.org/abs/2605.27276 | Code: github.com/hexo-ai/sia

## Why It Matters

Most AI agents today are frozen at deployment — you can give them better prompts or tools, but the model weights never change. SIA breaks this: task feedback feeds back into both the agent's strategy (harness) and its knowledge (model weights). This is recursive self-improvement in practice, not theory.
