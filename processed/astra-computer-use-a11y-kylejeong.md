---
tags: ["computer-use", "agents", "browser-agents", "models", "gpt-6"]
source: https://x.com/kylejeong/status/2097077446663372966
date: 2026-09-07
type: bookmark
description: "Kyle Jeong (Browserbase): Astra computer use is a11y-tree + code-mode (Playwright/PyAutoGUI) plus Guardian policy, not vision-pixel clicking."
author: kylejeong
summary: "Kyle Jeong (Browserbase): Astra computer use is a11y-tree + code-mode (Playwright/PyAutoGUI) plus Guardian policy, not vision-pixel clicking."
raw: "[[raw/kylejeong_2097077446663372966]]"
---

# How Astra's Computer Use Actually Works

Kyle Jeong (@kylejeong), Browserbase. X Article on GPT-6 Astra computer use. Vendor-adjacent; extract the architecture.

## History

Claude 3.5 computer use (Oct 2024): vision-only, pixels → JSON click/x/y. Viewport-locked; falls apart on other window sizes. Operator / computer-use-preview / Gemini 2.5 similar. Experiments: DOM+vision hybrids, FDM-1 video encoding.

## Astra / Codex harness

Computer use is **model + harness**. Codex: Node REPL with browser/native bindings. Observe via **text (a11y tree), screenshot, or both**. Act via **code** (`exec_js` / Playwright; PyAutoGUI for native). OpenAI API docs recommend code exec. Local IPC (`CodexComputerUseIPC-5`) JSON-RPC. Then re-observe to check the action actually worked. Session state persists in the REPL.

a11y tree: fewer tokens than screenshots, semantic roles, Chrome autogenerates it.

## Guardian

Astra requires auto-review: GPT-5.6 Luna classifier high/low risk; high → blocking reviewer. Blocks: permission grants, sign-in, sensitive data, consequential clicks, restriction bypass, destructive actions, out-of-scope private data.

## Speed

Smarter → fewer turns, not faster inference. Post-trained heavily in CU environments. Harness: websocket prewarm, connection reuse, `previous_response_id`. Bottleneck above ~300 TPS is action execution.

## Failures

Incomplete a11y/screenshot, stale state, a11y churn, long-horizon still unsolved.

## Related

- [[gpt6-astra-looped-transformers-rasbt]]
- [[llm-as-judge-architectures-runtime-joshrosen]]
