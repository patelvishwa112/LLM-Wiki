---
tags:
- mcp
- architecture
- hosts
- clients
- servers
- tools
- resources
- prompts
source: https://x.com/techyoutbe/status/2063553215623577693
date: 2026-06-07
type: bookmark
author: techyoutbe
summary: 'Clean mental model for MCP: Host orchestrates user interaction, Client handles
  protocol, Server exposes Tools/Resources/Prompts, Backend systems do the real work.
  Emphasizes separation of concerns, proper capability modeling (tools for actions,
  resources for data, prompts for templates), common anti-patterns, and enterprise
  deployment shapes.'
raw: '[[raw/techyoutbe_2063553215623577693]]'
description: 'Clean mental model for MCP: Host orchestrates user interaction, Client
  handles protocol, Server exposes Tools/Resources/Prompts, Backend systems do the
  real work. Emphasizes separation of concerns, proper capability modeling (tools
  for actions, resources for data, prompts for templates), common anti-patterns, and
  enterprise deployment shapes.'
---

# MCP Core Architecture Explained

Tech Fusionist's breakdown of the Model Context Protocol architecture.

## Layered Mental Model
- **User** → intent
- **Host Application** → orchestration, UX, deciding when capability is needed
- **MCP Client** → protocol discovery, request/response handling
- **MCP Server** → exposes Tools, Resources, Prompts
- **Backend Systems** → actual execution and data (APIs, DBs, filesystems)

## Key Distinctions
- **Tools**: Action-oriented (create ticket, run code, trigger workflow)
- **Resources**: Read-oriented (fetch document, load config, query logs)
- **Prompts**: Reusable interaction templates

## Common Mistakes
- Mixing host logic with backend logic
- Overloading the server with workflow/UI concerns
- Treating everything as a tool
- Exposing raw backend systems directly

## Best Practices
- Model capabilities explicitly
- Keep boundaries clean
- Prefer modular servers by domain
- Use structured schemas
- Abstract backend complexity

Directly relevant to Hermes MCP integration, skill design, and agent architecture.