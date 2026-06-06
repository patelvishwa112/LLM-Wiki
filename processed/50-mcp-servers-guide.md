---
tags: ["mcp", "agents", "claude-code", "codex", "gemini", "tools", "catalog"]
source: https://x.com/explorax_/status/2062448236439155173
date: 2026-06-04
type: bookmark
author: "m0h (@exploraX_)"
raw: "[[raw/explorax_2062448236439155173]]"
related: []
---

# 50 MCP Servers That Give Claude, Codex & Gemini Superpowers

## Key Takeaways

- **The MCP ecosystem is enormous but dangerous.** 20,000+ servers, ~97M SDK downloads/month (March 2026). But security issues found in ~2/3 of popular ones. Don't install 50 — more than 5-7 and your agent chokes on tool bloat, getting slower and dumber.
- **Three rules before anything else:** (1) Don't install 50, pick 3-5. (2) Treat every server like a CLI from a stranger's GitHub — pin versions, scope tokens read-only first. (3) Never enable writes against production from an agent loop.
- **Universal core (5 servers worth it on almost any machine):** GitHub (repos/PRs/issues), Context7 (current docs, stops API hallucinations), Playwright (real browser), Filesystem (scoped file access), Brave Search (web search inside agent).
- **Structured by domain:** Databases & Backend (Postgres, Supabase, Neon, SQLite, MongoDB, Redis, Pinecone, Firecrawl), Ops/Infra/Cloud (Sentry, Vercel, Cloudflare, Docker, K8s, AWS, Linear, Notion), Corporate/Productivity (GDrive, Calendar, Slack, Jira, Figma, Airtable, Obsidian, Excalidraw), Payments (Stripe, Plaid), Trading & Markets, Creator Tools, Reasoning & Memory (Mem0, Sequential Thinking).
- **How to choose:** Start with universal core. For databases, prefer provider-official over archived reference servers. Start everything read-only. This is a menu, not a shopping spree.

## Summary

m0h provides a curated, security-conscious catalog of 50 MCP servers organized by domain, with install commands for Claude Code, Codex, and Gemini CLI, plus gotchas for each. The guide opens with critical safety rules before listing any servers — a refreshingly honest approach given the audit finding security issues in ~2/3 of popular MCP servers. Each entry includes the install command, link to source, and a practical gotcha drawn from real usage.
