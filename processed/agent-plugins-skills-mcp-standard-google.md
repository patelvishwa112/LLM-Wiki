---
tags: ["skills", "mcp", "agents", "agent-harness", "standards", "google-cloud", "coding-tools", "progressive-disclosure", "open-source", "enterprise"]
source: https://x.com/googlecloudtech/status/2087733334617063503
date: 2026-08-13
type: bookmark
description: "Agent Plugins 1.0 Working Draft — portable folder of SKILL.md + mcp.json; Google joins TSC; skills+MCP travel together across clients."
author: googlecloudtech
summary: "Agent Plugins 1.0 Working Draft — portable folder of SKILL.md + mcp.json; Google joins TSC; skills+MCP travel together across clients."
raw: "[[raw/googlecloudtech_2087733334617063503]]"
spec_url: https://agent-plugins.org
---

# Agent Plugins — skills + MCP in one portable folder

@GoogleCloudTech / lavinigam: **Agent Plugins** is an open, vendor-neutral packaging standard for **Agent Skills** plus the **MCP servers** they depend on. Google joins the Technical Steering Committee as a Core Maintainer. Spec: [agent-plugins.org](https://agent-plugins.org). Status: **1.0.0 Working Draft**.

## Problem

Skills solved on-demand expertise (`SKILL.md` progressive load). They never solved **distribution of tools**: instructions in the skill, tools in MCP, binding lived in per-client README snippets. Every client invented its own bundle → rewrite hell.

## Package shape

| Piece | Role |
|-------|------|
| `plugin.json` | Manifest (min: `$schema` + `name`; optional version, description, author, license, keywords, `extensions`) |
| `skills/<dir>/SKILL.md` | Same as Agent Skills tree (`scripts/`, `references/`, `assets/`) |
| `mcp.json` | Declares MCP servers + transports (`stdio`, streamable-http, sse) |

Name rules: 1–64 chars, lowercase alnum/hyphen/period, start/end alnum, no `--` or `..`. Discovery is **one level deep** under `skills/` only — nested category folders vanish silently.

Placeholders: `${PLUGIN_ROOT}` (shipped assets), `${PLUGIN_DATA}` (writable state). Use `./` for bundled binaries. Writes to ROOT → state lost on update.

## Key behaviors

1. **Tools travel with expertise** — MCP defs packaged with skills.  
2. **Independent failure** — dead MCP server does not unload skills; diagnostics scoped.  
3. **Client extensions** — `extensions` namespace for hooks/commands without forking the portable core.  
4. **Schema strictness** — wrong JSON types fatal; unknown top-level fields + non-object extensions reported & ignored.

## Google shipments

- **Agents CLI** expert skills (build, eval, deploy, observability, publish)  
- **Data Agent Kit** — Spanner, Cloud SQL, AlloyDB plugins + BigQuery starter  
- One-command install in supported clients (e.g. Antigravity CLI)

## Gaps / migration

- **Credentials not portable** — no secrets in package; auth stays client-side.  
- Parallel layouts during transition: Claude Code `.claude-plugin/plugin.json` + `.mcp.json`; Antigravity `mcp_config.json` — check which file a client reads.  
- ADK Skills still experimental (version pins in post).  
- No standard linter/conformance suite yet — validate by loading in a real client.

## Why it matters

Closes the skills↔tools packaging hole that every harness hit independently. Aligns progressive-disclosure skill culture with MCP architecture and multi-client portability (same spirit as OKF for knowledge). Practical migration for existing `skills/` trees is mostly “add `plugin.json` + `mcp.json`.”

## Skeptical read

Working Draft + Google Cloud product surface (Agents CLI, Data Agent Kit). Conformance partial across clients/transports. Still the right direction for ecosystem packaging.

## Related

- [[writing-agent-skills-posthog-ian-vanagas]]
- [[dark-arts-of-skill-engineering-pbakaus]]
- [[how-to-create-right-skill-ai-agent]]
- [[show-me-visual-reps-coding-agents-dexhorthy]]
- [[anthropic-claude-code-skills-lessons]]
- [[mcp-core-architecture-hosts-clients-servers]]
- [[mcp-core-architecture-explained]]
- [[open-knowledge-format-okf-google]]
- [[openwiki-02-okf-langchain-bracesproul]]
