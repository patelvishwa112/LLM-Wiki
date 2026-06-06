---
tags: ["agents", "hermes", "openclaw", "agent-architecture", "research-agents", "local-llms", "multi-agent", "agent-ops"]
source: https://x.com/gkisokay/status/2059986597391823286
date: 2026-05-28
type: bookmark
author: gkisokay
---

# 21 Agent Building Mistakes

By Graeme (@gkisokay) | 3 months of Hermes + OpenClaw agents

## Key Takeaways

- **Crew over monolith:** Specialized agents with clear ownership. One bloated agent is impossible to debug.
- **Research-first architecture:** Build a research agent before output agents. It becomes the input intelligence layer.
- **Hermes as supervisor:** Don't run OpenClaw solo. Hermes has persistent memory, better UX, ClawHub skills.
- **Auto-think before auto-build:** A self-building system needs a self-thinking layer first.
- **Cost tracking is critical:** Log exact cost per run once things run 24/7.
- **Model diversity:** GPT-5.5 + Minimax for tool calling + local Qwen. Never depend on one provider.
- **Local LLMs:** Always-on layer for 24/7 background cognition. RAM tier decides what work runs cheaply.
- **Boring infrastructure first:** Clean inputs, clear handoffs, monitoring, recovery, evals before chasing AGI.

## Summary

Graeme distills 3 months of daily agent building into 21 rules. The core philosophy: specialized agents over monoliths, research layer before output layer, Hermes as supervisor over OpenClaw, local models for background work, cost tracking from day one, and building in public. Each rule is paired with a linked guide or setup tutorial.

## Source

https://x.com/gkisokay/status/2059986597391823286

## Related

- [[iii-agent-harness-workers]] — Composable agent architectures
- [[autobrowse-browser-agent-memory]] — Skills as durable memory
