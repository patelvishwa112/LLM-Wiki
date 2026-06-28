---
tags:
- agents
- generative-ui
- mcp
- ag-ui
- a2ui
- copilotkit
- frontend
source: https://x.com/saboo_shubham_/status/2062220865643982875
date: 2026-06-03
type: bookmark
author: Shubham Saboo
raw: '[[raw/sabooshubham_2062220865643982875]]'
description: Generative UI Is the New Frontend
---

# Generative UI Is the New Frontend

## Key Takeaways

- **Three Gen UI patterns, not one.** Controlled (pre-built components, agent picks), Declarative/A2UI (agent emits schema, app maps to components), Open-ended (agent writes raw HTML in sandbox). Most teams pick one without knowing they chose — and hit scaling walls they didn't see coming.
- **The protocol stack matters.** MCP (agent↔tools), A2A (agent↔agent), AG-UI (agent↔user). AG-UI is the bidirectional streaming layer over SSE that carries everything: tool calls, A2UI schemas, MCP App events, state deltas.
- **Controlled breaks past ~15-25 components.** Every registered component sits in context at ~400 tokens each. 25 components = 10K tokens per turn. The agent also starts confusing semantically similar tools. Use for top 3-10 high-value flows only.
- **Declarative scales flat.** One tool. Many UIs. Token cost stays constant regardless of component library size. The catalog is the contract — Zod schemas + renderers. Match CATALOG_ID on both sides or everything silently falls back to generic.
- **Open-ended is for throwaway only.** Sandboxed HTML is great for one-shot visualizations. But brand consistency is impossible — "Neo-brutalist on Tuesday, iOS 4 clone on Wednesday." Never as the primary surface.
- **Default to Declarative.** Upgrade to Controlled for pixel-perfect flows. Open-ended only for disposable. Past 15 render tools, you're in Controlled and the wall is close — start wiring A2UI this week.

## Summary

Shubham Saboo lays out the three architectural patterns for Generative UI in 2026, built on the CopilotKit + AG-UI + ADK stack. The core insight: these aren't cosmetic differences — each pattern breaks your app in a different way at scale.

The Controlled pattern gives design precision but burns tokens and confuses agents past ~15 components. The Declarative pattern (A2UI) scales flat with one tool that emits JSON schemas — the agent writes the component tree per turn, and your catalog maps it to React. The Open-ended pattern gives the agent raw HTML in a sandboxed iframe, great for one-shot throwaways but unusable as a primary surface due to brand drift.

Key operational details: AG-UI uses SSE with bidirectional state flow. CopilotKit's MCPAppsMiddleware connects any MCP Apps server. The A2UI pattern uses three operations (create_surface, update_components, update_data_model) and supports both fixed and dynamic schemas.

## Related

- [[the-html-brand-input-based-outcomes]]
