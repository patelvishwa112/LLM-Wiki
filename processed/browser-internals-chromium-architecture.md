---
tags: [browser-internals, chromium, v8, rendering-pipeline, networking, javascript-engine, frontend-performance, browser-agents, web-performance]
source: https://x.com/addyosmani/status/2068394292796871019
type: concept
ingested: 2026-06-20
related: [[browser-agents], [frontend-design], [ui]]
---

# How Modern Browsers Work — Chromium Architecture Deep Dive

**Source:** [X Post by @addyosmani](https://x.com/addyosmani/status/2068394292796871019)

## Summary

Addy Osmani delivers a comprehensive technical overview of how modern web browsers operate, with deep focus on Chromium’s architecture (while noting differences in Gecko and WebKit).

The post demystifies the “black box” by walking through the full pipeline: networking, parsing, styling, layout, painting/compositing, JavaScript execution (V8), multi-process model, security sandboxing, and developer tooling.

### Key Architectural Areas Covered

- **Networking & Resource Loading**: HTTP/2+3, speculative loading (DNS prefetch, preconnect, preload, Early Hints, Speculation Rules API), security checks (CORB, Safe Browsing)
- **Parsing**: Incremental HTML → DOM, CSSOM, script loading strategies (`async`/`defer`/`module`)
- **Styling & Layout**: Layout tree, reflow, box model/flex/grid performance considerations
- **Rendering**: Paint records, compositor thread, Skia rasterization, GPU textures, why certain animations are smooth
- **V8 JavaScript Engine**: Ignition → Sparkplug → Maglev → TurboFan (Turboshaft), type feedback, Orinoco GC, inline caches, deoptimization
- **Multi-process & Security**: Browser/renderer/GPU processes, site isolation, sandboxing, Network Service

Addy noted the post was written by hand (with LLM assistance only for fact cross-referencing).

## Why It Matters

High-signal foundational knowledge for anyone building browser agents, web automation, frontend performance tooling, or agentic web systems. Directly relevant to `browser-agents`, `frontend-design`, and understanding the execution environment that agents interact with. Explains why certain optimizations (compositor-only animations, speculative loading, etc.) matter at the architectural level.

## Related
- [[browser-agents]] and autobrowse patterns
- [[frontend-design]] and UI performance
- Web performance and rendering pipeline concepts in the vault