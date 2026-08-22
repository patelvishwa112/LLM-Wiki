---
tags:
  - skills
  - agents
  - agent-harness
  - agent-memory
  - procedural-memory
  - prompt-engineering
  - hermes
source: https://x.com/samzliu/status/2090977607219396771
date: 2026-08-21
type: bookmark
author: samzliu
description: "Skills are folders that help agents act — they solve recall-vs-recognition, consistency, portable expertise, and reasoning checkpoints, not just prompt reuse."
summary: "Skills are folders that help agents act — they solve recall-vs-recognition, consistency, portable expertise, and reasoning checkpoints, not just prompt reuse."
raw: "[[raw/samzliu_2090977607219396771]]"
published: 2026-08-21
---

# Skills, what are they good for?

Sam Z Liu (Stash) on why smart people talk past each other about agent skills. Skeptics treat them as over-engineered prompts that labs will distill away. Proponents (Garry Tan) treat them as natural-language code — "War and Peace is also just a prompt."

The split is definitional. Dismissers mean a markdown file. Practice has already outgrown that.

## What a skill is

A skill is a **folder of information that helps an agent perform a task** — intentionally vague.

Three boundary cases:

- **Last30days** — mini-program: markdown plus code plus tools that track HN/Reddit/X
- **Symphony** — markdown spec whose install path is "have the agent build the orchestrator from scratch." Same class as Karpathy LLM Wiki: a Schelling point, not a snippet
- **Plugins** (Claude Code, Hermes, Openclaw) — hooks + tools + harness integration. Some capabilities are plugin-only

## Four problems they actually solve

At one user and one prompt, skills look redundant. They matter at **system scale**.

1. **Recall vs recognition** — the GUI vs terminal problem. Skills enumerate moves you would not remember or invent. Examples: YouTube lecture notetaker with slides, 3D graphics, WYSIWYG HTML editor to strip AI slop, record-a-Loom-to-skill.
2. **Consistency** — SOPs / pilot handbook so the agent does not rediscover a path and fall into an irrecoverable hole. Common on Clawhub: external integrations. Without them, agents skip MCP and mint their own API keys via computer-use.
3. **Portable expertise** — O'Reilly books for agents: SEO, cybersecurity, copywriting, HTML slides. Knowledge the user does not have.
4. **Reasoning checkpoint** — personalized skills that accumulate user-specific procedure from prior traces plus feedback (e.g. how you run sales outbound). Early procedural memory.

## How to build them

Think about the **system next week**, not today's one-off. Two frames:

- They are still mostly text — apply writing craft (clarity, structure, proofreading).
- Improving them hits Goodhart the same way model training does. Regularization analogies: evolutionary search, gradient clipping, dropout (he also writes "backdrop").

## Why it matters

Connects skill-writing notes (Aparna, PostHog, agentskills.io) to a **systems** claim: skills are how token-space procedure compounds. Pair with plugin standards when hooks/tools are required.

## Skeptical read

Regularization-as-skill-ops is a metaphor, not a recipe. "Labs will distill public skills" is a real counter if the skill is generic. The four-problem frame is the durable part.

## Related

- [[writing-good-skills-measured-rulebook-aparna]]
- [[how-to-create-right-skill-ai-agent]]
- [[writing-agent-skills-posthog-ian-vanagas]]
- [[agent-plugins-skills-mcp-standard-google]]
- [[dark-arts-of-skill-engineering-pbakaus]]
- [[self-learning-agents-three-layers-user-signal]]
- [[colleague-skill-dot-skill]]
