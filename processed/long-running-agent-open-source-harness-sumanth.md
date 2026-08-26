---
tags:
  - harness-engineering
  - agent-harness
  - agents
  - mcp
  - skills
  - context-engineering
  - trueforge
  - open-source
source: https://x.com/sumanth_077/status/2092242081154847137
date: 2026-08-25
type: bookmark
author: sumanth_077
description: "Sumanth walks a TrueForge research agent through the harness: loop, MCP, skills, sandbox offload, subagents, compaction, runtime approval gates, durable event stream."
summary: "Sumanth walks a TrueForge research agent through the harness: loop, MCP, skills, sandbox offload, subagents, compaction, runtime approval gates, durable event stream."
raw: "[[raw/sumanth_077_2092242081154847137]]"
published: 2026-08-25
---

# Build a Long-Running Agent With an Open Source Harness

Sumanth (@Sumanth_077), Aug 25 2026. Prompted by Sam Altman: “a reason to favor open-source harnesses.” Worked example: TrueForge (TrueFoundry). Repo: https://github.com/truefoundry/trueforge

## Claim

A raw model is stateless. Minutes-long work — search, code, dozens of steps, recover from disconnect — is a **harness** problem. The loop is easy to write in an afternoon. Surviving a real task is not.

## Anatomy (research agent)

Model + Exa MCP + `web-artifacts-builder` skill + sandbox. `npx @truefoundry/trueforge` → localhost:8790. Save the agent so the app only references the config.

Loop: model → tool → harness executes → result back → repeat.

## Pieces that make the loop survive

- **MCP / progressive disclosure** — don’t dump every tool schema into every call. Discover, then load.
- **Skills** — *how* to do a class of work. Same disclosure: know the catalog, load the procedure when relevant. MCP = can; skills = how.
- **Sandbox** — code/files isolated from the agent server. Also the offload path: process a 20k-token search in the sandbox, return a summary/file ref.
- **Context** — two piles: what you inject (prompt, tools, skills) vs what the run generates (results, history). Four techniques: progressive disclosure, Code Mode (filter in code), large-result offload, compaction/summarize past a threshold.
- **Subagents** — fan-out parallel research with isolated context; parent gets conclusions only. Not free: skip if the task fits one window.
- **Approval gates** — runtime, not a prompt. Tool metadata → harness pauses before execute. Model cannot reason around it.
- **Durable event stream** — ordered persisted events. Browser close does not kill the run. Replayable trace: searches, tool surprises, what the parent did with a subagent’s conclusion.

## Why it matters

Same map as Deep Agents / Claude Code (plan, sandbox, subagents, hooks). Makes the Altman line concrete: the reusable layer is the harness, not the model. Skills-as-folders (Liu) sit inside this runtime.

## Skeptical read

TrueFoundry-sponsored walkthrough. Read-only research agent never hits the hard approval/write cases. Compaction loses early detail — the article admits it.

## Related

- [[harness-is-the-product-context-aware-agents]]
- [[learn-harness-engineering]]
- [[deepseek-harness-five-patterns-saboo]]
- [[skills-what-are-they-good-for-samzliu]]
- [[ai-native-sdlc-playbook]]
- [[how-to-use-rlms-in-deep-agents]]
