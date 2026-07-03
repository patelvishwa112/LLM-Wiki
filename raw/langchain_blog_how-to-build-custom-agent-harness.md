---source_url: https://www.langchain.com/blog/how-to-build-a-custom-agent-harness
ingested: 2026-07-03
author: Sydney Runkle
title: "How to Build a Custom Agent Harness"
note: Full text via mcp_firecrawl_firecrawl_scrape; Related content footer omitted.
sha256: 86c9f70c680f1cedb15df3a894fd4f46c647b083a2a05fc9e305c5e9c2fed8ba
---

# How to Build a Custom Agent Harness

**Author:** Sydney Runkle (LangChain)  
**Published:** June 3, 2026

## Key Takeaways

- A harness is the scaffolding around the model that connects it to the real world.
- How well a harness fits the task at hand determines how useful an agent is.
- LangChain's `create_agent` is the easiest way to build a custom harness tailored to a given task.

Building useful agents is largely about **customization:** connecting your agent to the right context, data, and environment(s) for the task at hand.

At its core, an agent is a model calling tools in a loop until it completes a task and returns a result.

> agent = model + harness

The harness is the scaffolding around the model that connects it to the real world.

Assumptions:
1. An agent is only as good as the context provided to the model
2. The job of a harness is to provide context to the model at every step

## The base harness

`create_agent` is LangChain's primitive for building a harness. Pass in a model, tools, and a system prompt.

```python
from langchain.agents import create_agent

agent = create_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=tools,
    system_prompt="you are a helpful assistant..."
)
```

Deep Agents and Claude Agent SDK come pre-assembled with opinionated middleware. `create_agent` is **purposefully minimalistic** (Pi-like philosophy): core agent loop + **middleware** for customization.

## Middleware: how you customize the harness

Middleware hooks into the agent loop at each step: before/after model calls, before/after tool calls, startup/teardown. Composable units.

Levers:
- **Deterministic logic** — policy, dynamic model/prompt swaps, compaction edits to message history
- **Tools** — lifecycle setup/teardown/registration near governing logic
- **Custom state** — counters/flags across hooks
- **Stream handlers** — filter/route events (UI tokens, audit logs, latency monitoring)

Prebuilt + custom middleware; reusable org-wide.

## Harness capabilities (middleware map)

| Capability | Why | Middleware examples |
| --- | --- | --- |
| Prevent context overflow | Long sessions overflow window | SummarizationMiddleware, ContextEditingMiddleware |
| Access/update memory | Load at startup, write back | FilesystemMiddleware, MemoryMiddleware, SkillsMiddleware |
| Take actions in environment | Fixed toolset limits creativity | ShellToolMiddleware, FilesystemMiddleware, CodeInterpreterMiddleware |
| Delegate tasks | Subagents + progress tracking | SubAgentMiddleware, AsyncSubAgentMiddleware, TodoListMiddleware |
| Handle transient failures | Retries/fallbacks | ToolRetryMiddleware, ModelRetryMiddleware, ModelFallbackMiddleware |
| Enforce policies | PII/compliance every call | PIIMiddleware, HumanInTheLoopMiddleware |
| Steer the agent | Approval gates | HumanInTheLoopMiddleware |
| Control costs | Caching + limits | ModelCallLimitMiddleware, ToolCallLimitMiddleware, PromptCachingMiddleware |

## Task-harness fit

Match harness to task demands: context, failures, policies, environment. CS agent ≠ long-running coding agent. LangChain GTM agent, open-swe, LangSmith Fleet built on `create_agent` + tailored middleware stacks.

## References (from post)

- create_agent quickstart, agents guide, middleware built-in/custom, Deep Agents overview