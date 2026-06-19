---
source_url: https://code.visualstudio.com/blogs/2026/06/17/improving-token-efficiency-in-github-copilot
ingested: 2026-06-19
sha256: 8f3c2a1b9e4d7f6c5a8b2e1d9f3c4a5b6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3
author: Ryan Caldwell, Bhavya U (VS Code team)
---

# Improving token efficiency for GitHub Copilot in VS Code

June 17, 2026 by Ryan Caldwell and Bhavya U

With the recent move to usage-based billing for GitHub Copilot, every token in an agentic session matters. They affect your credits, latency, and the context window an agent has left to finish the task. Each new model generation tends to consume more tokens per task than the last. This means that harness-level efficiencies are increasingly important to counter this trend. As agents take on longer, more autonomous work, an inefficient harness adds up fast.

[Full article content continues with sections on prompt prefix and caching, tool-definition overhead, tool search, extended prompt caching for OpenAI, WebSockets, smarter prompt caching for Anthropic, client-side tool search with embeddings, what's next on subagents, etc. See processed note for synthesis.]
