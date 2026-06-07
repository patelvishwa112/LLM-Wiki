# Running an AI-Native Engineering Org

**Author:** Fiona Fung (Director of Engineering, Claude Code & Claude Cowork, Anthropic)
**source_url:** https://claude.com/blog/running-an-ai-native-engineering-org
**ingested:** 2026-06-07
**sha256:** 98ae6cc111cc56f0109aa378f11957b7bc4dd77ab0939de3c2c5fc687e4ba0c2

---

From Code w/ Claude SF 2026. How the Claude Code team's processes and structure changed once agentic coding became the default way of working.

## The Bottleneck Shift

Writing code, writing tests, and refactoring rarely slow the team down anymore. But the bottlenecks didn't go away — **verification, code review, and security** took their place.

> "We can all generate a lot of code really fast now, but this also brings up new questions: Is this code correct? How is it maintained?"

## Four Norms That Broke

### 1. Planning: Shift to Just-in-Time (JIT)

**Old norm:** Six-month roadmaps, design docs, product reviews.

**Why it broke:** A good six-month roadmap was out of date by month three because of Claude Code.

**New norm:** JIT planning. Prototype, get internal users on it fast, act on their feedback. Discussions happen in PRs and prototypes, not design docs. Minimal product reviews.

### 2. Context Gathering: Ask Claude, Not the Author

**Old norm:** Find the person who wrote the code.

**Why it broke:** All PRs are Claude-assisted. "Who made this change?" is no longer sufficient.

**New norm:** Go a level deeper. What do you actually need to know? Ask Claude that question directly. Also ask: "Is there a way to automate this?" Example: having Claude summarize customer feedback channels every morning.

### 3. Code Review: Trust but Verify

**Old norm:** Humans review everything.

**New norm:** Claude handles style, linting, PR feedback, catching bugs, adding tests. Humans review where domain expertise matters: legal review, trust boundaries, security-sensitive code, product taste. The right balance of trust vs. verify keeps changing as models improve.

### 4. Team Makeup: Blurring Roles

**Old norm:** Fixed roles — engineers code, PMs plan, designers design.

**New norm:** PMs prototype and code. Engineers take on content and design. Nontraditional coders do engineering.

**Two profiles that matter most:**
- Creative builders with product sense — dreamers curious about shipping products that solve problems
- Engineers with deep systems expertise

**What matters less:** Raw throughput. The models handle that.

| | Before | After |
|---|---|---|
| Planning | Six-month roadmaps | JIT: prototype → internal users → feedback |
| Context | Find the author, ask them | Ask Claude first, then automate it |
| Code Review | Humans review everything | Claude: style/bugs/tests. Humans: domain expertise |
| Team | Fixed roles | Roles blur. Hire builders + systems experts |

## Core Team Principles (Non-Negotiable)

1. **Relentlessly dogfood your product** — every team member uses Claude Code and Claude Cowork
2. **Keep the team as flat as possible** — every manager starts as IC first, ships real code, understands what it's like to be an engineer
3. **Don't hesitate to kill processes that no longer work** — explicit permission to question and kill old processes

Within these, each pod has agency over triage, planning rituals, standups, and which workflows get "Claudified" first.

## Three Metrics to Track

1. **Onboarding ramp time goes down** — engineers ship real code within their first week (much faster than a year ago)
2. **PR cycle time goes down** — dig into where the pipeline struggles to scale (build systems, CI)
3. **Claude-assisted commits going up** — every commit is Claude-assisted. "I don't think I've seen a non-Claude-assisted commit in the last four months."

**Don't confuse throughput with success.** Throughput is one metric. The real metric is measuring the thing you're trying to solve.

## Getting Started

Pick your noisiest workflow — the most expensive one, the one you dread, the one the team doesn't look forward to. Ask: is it still serving its purpose? If so, can you automate it?

Example: A team had an expensive weekly review with everyone on laptops except during their status report. One question — "Why are we having this meeting?" — made everyone realize it wasn't needed. Canceled.
