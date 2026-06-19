---
tags: [github-copilot, token-efficiency, prompt-caching, tool-search, agent-harness, vscode, anthropic, openai, cost-optimization, latency, mcp, prompt-engineering, agent-architecture]
source: https://code.visualstudio.com/blogs/2026/06/17/improving-token-efficiency-in-github-copilot
type: bookmark
ingested: 2026-06-19
---

# Improving Token Efficiency in GitHub Copilot Agentic Harness (VS Code)

**Source:** [VS Code Blog - June 17, 2026](https://code.visualstudio.com/blogs/2026/06/17/improving-token-efficiency-in-github-copilot) by Ryan Caldwell & Bhavya U

## Summary
Detailed engineering post on how the VS Code team reduced token usage and latency in GitHub Copilot's agentic workflows through prompt caching improvements, tool search (defer_loading), WebSocket transport for OpenAI, smarter cache breakpoint placement for Anthropic, and client-side embedding-guided tool search. Achieved 9-18% token reductions, significant latency wins, and higher cache hit rates (up to 94% for Anthropic) while maintaining or improving task success. Directly relevant to agent harness design, MCP tool management, and cost/latency optimization in local + cloud agent systems.

## Why It Matters
This is core material for the wiki's "Agent Architecture" and "Claude/AI Tools" domains. It provides concrete, production-validated techniques for the exact problems we face in hermes-agent, claude-code workflows, MCP servers, and any long-running agentic session (prompt prefix caching, tool definition bloat, repeated requests). The emphasis on A/B testing harness changes, subagents for narrow tasks, and transparency around token spend aligns perfectly with the vault's focus on reliable, efficient agent systems. High-signal for anyone building or tuning agent harnesses.

## Key Techniques
- **Prompt prefix caching** (OpenAI extended retention 24h, Anthropic deliberate breakpoints at tool defs + system prompt + rolling anchors)
- **Tool search / defer_loading**: Model sees only lightweight metadata; heavy schemas loaded on demand. Reduces context bloat dramatically.
- **WebSockets** for OpenAI Responses API: persistent connection + response state reuse for sequential tool calls.
- **Client-side tool search** with internal embedding model for intent matching (better than lexical, supports dynamic MCP tools).
- **Future direction**: Specialized subagents on smaller/cheaper models + better token usage UI.

## Related Notes
- [[agent-harness]]
- [[claude-code]]
- [[mcp]]
- [[prompt-engineering]]
- [[skills]]
- [[anthropic-harnessing-claudes-intelligence]]

---
*Raw source saved to: raw/vscode-copilot-token-efficiency.md*
*Ingested as part of LLM Wiki curation pipeline. Full original blog content preserved in raw.*
