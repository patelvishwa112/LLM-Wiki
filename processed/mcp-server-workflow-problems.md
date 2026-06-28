---
title: Build an MCP server to solve your annoying workflow problems
tags:
- mcp
- agents
- coding-tools
- typescript
- antigravity
- productivity
source: https://medium.com/google-cloud/build-an-mcp-server-to-solve-your-annoying-workflow-problems-aa696d5ccf44
date: 2026-06-01
published: 2026-05-29
authors:
- Karl Weinmeister
type: article
raw: '[[raw/medium_kweinmeister_mcp-server-workflow-problems]]'
description: Build an MCP server to solve your annoying workflow problems
---

# Build an MCP server to solve your annoying workflow problems

## Key Takeaways

- MCP servers are worth building for small, recurring friction points — Karl's table-to-image converter took a few hours and already paid for itself
- FastMCP + Zod schema + an execute function = ~20 lines to a working MCP tool; the framework handles transport, error handling, and type safety
- `.describe()` calls on Zod schemas are critical — coding agents pass these descriptions to the LLM, and good descriptions mean fewer wrong parameter guesses
- The rendering pipeline is clean: markdown string → parser (validates + structures) → React JSX component (CSS-in-JS theming) → Takumi Rust renderer (direct JSX→PNG, no intermediate SVG)
- Takumi is interesting tech: Rust-based, embeds fonts, supports flexbox/gradients/borders, renders at configurable scale (2x default for Retina)
- MCP server config format is identical between Antigravity (`~/.gemini/config/mcp_config.json`) and Claude Code (`~/.claude.json` or `.mcp.json`)
- 5 themes included: glassmorphism, slate-dark, minimalist-light, emerald-glow, synthwave
- Source: https://github.com/kweinmeister/markdown-table-to-image-mcp

## Why This Matters

- Reinforces the MCP ecosystem thesis — the barrier to building custom tools is dropping fast. FastMCP removes most boilerplate
- Takumi as a JSX→PNG renderer could have broader applications beyond table rendering (any JSX layout → image)
- The `.describe()` insight is directly applicable to Hermes tool building — description quality determines LLM behavior
- Fits your Antigravity workflow — you can build small MCP servers to automate personal friction points in your dev/research loop

## Summary

Karl Weinmeister (Google Cloud DevRel) built an MCP server that converts markdown tables into styled PNG images to solve a Medium publishing pain point. The server takes a raw markdown table string and returns a PNG ready to paste. The pipeline: parse markdown into structured data → render with React + CSS-in-JS theming → convert to PNG via Takumi (Rust renderer). Built with FastMCP (higher-level MCP SDK) and Zod schemas. About 20 lines of core code. Connects to both Antigravity and Claude Code via standard JSON config.

## Source

[Medium - Google Cloud Community](https://medium.com/google-cloud/build-an-mcp-server-to-solve-your-annoying-workflow-problems-aa696d5ccf44)
