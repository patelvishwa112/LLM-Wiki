---
tags:
- github-copilot
- data-analytics
- internal-agent
- qubot
- agent-architecture
- trino
- kusto
- analytics-agent
- github-blog
source: https://github.blog/ai-and-ml/github-copilot/how-we-built-an-internal-data-analytics-agent/
type: bookmark
ingested: 2026-06-20
description: How we built an internal data analytics agent (Qubot)
---

# How we built an internal data analytics agent (Qubot)

**Source:** [GitHub Blog](https://github.blog/ai-and-ml/github-copilot/how-we-built-an-internal-data-analytics-agent/) by Matteo Vasirani & Cynthia Joseph

## Summary
GitHub built "Qubot", an internal data analytics agent powered by GitHub Copilot that answers questions about product analytics by connecting to Trino and Kusto. The post details the architecture, how the agent uses context from users and data sources, and lessons from deploying a production analytics agent inside GitHub.

## Images on page (Playwright MCP extraction)
- **Main architecture diagram**: Shows Qubot receiving context/users and querying Trino + Kusto for answers (core technical visual).
- Author avatars: Matteo Vasirani, Cynthia Joseph.
- Decorative hero images: Copilot with invertocat logo, Mona branding.
- Video thumbnail: "What do slash commands do?"

## Why It Matters
Excellent real-world case study of building a domain-specific internal agent (analytics) using Copilot. Directly relevant to agent-harness patterns, tool integration (Trino/Kusto as data tools), and production deployment of agents inside a company. High-signal for anyone building similar internal tools or data agents.

## Related Notes
- [[github-copilot]]
- [[agent-architecture]]
- [[internal-tools]]

---
*Raw source saved to: raw/github-qubot-data-analytics-agent.md*
*Extracted using Playwright MCP (navigation + image evaluation + content extraction)*
