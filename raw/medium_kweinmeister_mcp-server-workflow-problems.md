---
source_url: https://medium.com/google-cloud/build-an-mcp-server-to-solve-your-annoying-workflow-problems-aa696d5ccf44
title: "Build an MCP server to solve your annoying workflow problems"
author: Karl Weinmeister
published: 2026-05-29
ingested: 2026-06-01
sha256: 4aea51817f3e20a73b0887ed75e64d22d1000143b57b2e91364f5bcfddca20b3
platform: Medium
publication: Google Cloud - Community
tags: ["mcp", "agents", "coding-tools", "typescript", "antigravity"]
---

# Build an MCP server to solve your annoying workflow problems

By Karl Weinmeister | Google Cloud - Community | 6 min read | ~May 29, 2026

## Content

If you've written an article on Medium, you might have noticed that Markdown tables aren't natively supported. The workaround is to screenshot a table that is rendered in some other app, but that may not end up looking right.

I built an MCP server to solve this problem. You hand it a markdown table and it gives you back a styled PNG image, ready to paste into your post. It runs inside Antigravity, Claude Code, or your favorite coding agent.

This post walks through how I built it and why building your own MCP server for small workflow problems is worth the effort.

## What's an MCP server?

The Model Context Protocol is a standard that lets AI coding agents (like Antigravity or Claude Code) talk to external tools through a common interface. Before MCP, every coding agent had its own way of calling tools. If you built a tool for one agent, it didn't work with another.

MCP standardizes this with three primitives: **tools** (actions the model can take), **resources** (read-only data), and **prompts** (reusable templates). You build a server that exposes one or more of these, and any MCP-compatible coding agent can use it.

## The rendering pipeline

The server takes a markdown table string and returns a PNG. There are three stages to this process.

**Parsing.** The raw markdown string gets split into headers, rows, and column alignments. The parser strips any HTML (security), checks size limits (50 columns, 500 rows, 50K characters), and returns a clean data structure.

**JSX layout.** The parsed table data feeds into a React component that builds the visual layout. Each theme defines a full set of CSS-in-JS styles for the canvas, card, title, headers, and cells. The component uses flexbox for column sizing, so tables adapt to their content width.

**Image rendering.** Takumi handles the final step. Takumi is a Rust-based renderer that converts JSX directly to PNG in a single pass — no intermediate SVG step. It runs its own layout engine with broad CSS support (flexbox, borders, gradients, text transforms) and embeds font data directly into the output. The result is rasterized at a configurable scale (default 2x for Retina displays).

```typescript
// The full pipeline in takumi.ts
const element = React.createElement(TableRenderer, {
  table: options.table,
  title: options.title,
  theme,
  aspectRatio,
  customWidth,
  transparentBackground: options.transparentBackground,
});
const image = await render(element, {
  width: dimensions.width * scale,
  height: dimensions.height ? dimensions.height * scale : undefined,
  devicePixelRatio: scale,
  fonts,
  format: "png",
});
return Buffer.from(image);
```

## Building an MCP server with FastMCP

You can build an MCP server with the official TypeScript SDK, but FastMCP makes it faster. FastMCP is a higher-level framework that handles the transport layer, error handling, and type safety so you can focus on defining your tools.

Here's the core of the server definition:

```typescript
import { FastMCP } from "fastmcp";
import { renderTableToPng } from "./takumi.js";
import { parseMarkdownTable } from "./parser.js";
import { RenderOptionsSchema } from "./schemas.js";

const server = new FastMCP({
  name: "markdown-table-to-image-mcp",
  version: "1.0.0",
});

server.addTool({
  name: "markdown_table_to_image",
  description: "Converts a raw Markdown table string into a styled PNG image.",
  parameters: RenderOptionsSchema,
  execute: async (args) => {
    const table = parseMarkdownTable(args.markdown);
    const pngBuffer = await renderTableToPng({ table, ...args });
    return await imageContent({ buffer: pngBuffer });
  },
});

server.start();
```

That's about 20 lines to go from "I have an idea" to "my coding agent can call this tool." FastMCP handles the stdio transport, the JSON-RPC protocol layer, and the schema validation. You define the tool name, its description (which the AI model reads to decide when to call it), the parameter schema, and the execute function.

The parameters are defined with Zod, which gives you runtime validation and TypeScript types from a single schema definition:

```typescript
import { z } from "zod";

export const RenderOptionsSchema = z.object({
  markdown: z
    .string()
    .max(50000)
    .describe("The raw markdown table string to convert."),
  title: z
    .string()
    .max(200)
    .optional()
    .describe("Optional title text displayed above the table."),
  theme: z
    .enum([
      "glassmorphism",
      "slate-dark",
      "minimalist-light",
      "emerald-glow",
      "synthwave",
    ])
    .optional()
    .default("glassmorphism"),
  scale: z
    .number()
    .min(0.5)
    .max(4)
    .optional()
    .default(2)
    .describe("Scale multiplier for high-DPI rendering."),
});
```

The `.describe()` calls are important. Coding agents pass these descriptions to the language model, and the model uses them to fill in the parameters correctly. Good descriptions mean fewer wrong guesses.

## Themes, caching, and the details

The server ships with five visual themes. Each theme is a plain object mapping component names (canvas, card, title, header row, data row) to React CSSProperties objects. Adding a new theme means adding another object to the map.

Here's an example Markdown table rendered in a few themes:

```
| Item | Category | Status | Price |
| --- | --- | --- | --- |
| Widget Alpha | Hardware | Active | $5.99 |
| Gadget Beta | Software | Pending | $12.50 |
| Tool Gamma | Service | Active | $42.00 |
| Sensor Delta | Hardware | Error | $18.25 |
| Module Epsilon | Software | Active | $99.99 |
| Proxy Zeta | Network | Active | $0.00 |
```

## Connecting to your coding agent

Once the server is built (`npm run build`), you register it with your coding agent by adding an entry to a JSON config file.

The format is the same for both Antigravity (`~/.gemini/config/mcp_config.json`) and Claude Code (`~/.claude.json` for global scope or `.mcp.json` for project scope):

```json
{
  "mcpServers": {
    "markdown-table-to-image": {
      "command": "node",
      "args": ["/path/to/dist/server.js"]
    }
  }
}
```

## When to build your own

The table-to-image converter started because I was tired of a friction point. It took a few hours to build the first version. That time has already paid for itself.

If you find yourself doing the same manual step over and over while working with a coding agent, that's a good MCP server candidate. Some examples:

- Converting between formats (markdown to HTML, CSV to JSON, YAML to TOML)
- Generating boilerplate from templates
- Querying internal APIs or databases that your coding agent can't reach directly
- Running project-specific validation or linting checks
- Fetching and formatting data from external services

With coding tools to help, the barriers to building an MCP server are lower than ever. In TypeScript, all we needed was FastMCP, a Zod schema, and an execute function. The whole thing can live in a single file. Start with the smallest version that solves your problem, then add themes and caching and options later.

The markdown-table-to-image-mcp source is on GitHub: https://github.com/kweinmeister/markdown-table-to-image-mcp

If you've built an MCP server that solves your own pain point, I'd love to hear about it. Find me on X (@kweinmeister), LinkedIn, or Bluesky.
