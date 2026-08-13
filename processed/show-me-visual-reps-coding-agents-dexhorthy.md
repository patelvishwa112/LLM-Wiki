---
tags: ["skills", "coding-tools", "agents", "agent-harness", "prompt-engineering", "claude-code", "ux", "productivity", "progressive-disclosure", "design"]
source: https://x.com/dexhorthy/status/2087569590268391897
date: 2026-08-12
type: bookmark
description: "HumanLayer /show-me skill — force coding agents to answer with trees, stacks, diffs, types, Mermaid/HTML instead of prose walls."
author: dexhorthy
summary: "HumanLayer /show-me skill — force coding agents to answer with trees, stacks, diffs, types, Mermaid/HTML instead of prose walls."
raw: "[[raw/dexhorthy_2087569590268391897]]"
---

# /show-me — compact visual reps for coding agents

@dexhorthy (HumanLayer): agents got “smarter” on paper while **UX degraded** — jargon, corporate tone, prose walls (Claude soul flushed by RL; Sol less cringe but still glazes). Counter-skills like Dillon Mulroy’s `/bro` simplify language; **show-me** goes further: **converse visually**.

## Install

```bash
npx skills add humanlayer/skills --skill show-me
# or full HumanLayer (inline HTML/diagrams first-class)
brew trust humanlayer/humanlayer && brew tap humanlayer/humanlayer && brew install humanlayer
```

Invoke: `/show-me`, “this is too much content. show me.”, “/show-me as an html explainer” — point at route, service, feature, PR, or restate last answer.

## Formats (dev-work shaped)

| Format | Use |
|--------|-----|
| **Component trees** | UI structure + relevant state/hooks + module boundaries |
| **Call stacks / trees** | Orchestration, control flow, backend paths |
| **Diagrams** | Mermaid state/sequence — better than words even if sloppy |
| **File layouts** | Shallow tree of responsibility — scoping refactors |
| **Pseudocode** | Algorithms before code |
| **Types & signatures** | Shape of APIs before implementation |
| **Diff syntax** | Component / call-tree / file-layout / control-flow deltas |
| **HTML mockups / explainers** | Prototyping (HTML > Figma for many); open in browser |

Lighter/faster than always-on HTML; good enough for most coding problems.

## Inspiration

- Coda Hale: **intuition vs attention** — visual cortex cheap; analyzing prose hard  
- Matt Pocock `/teach` HTML explainers  
- Tools should fit the mind the way an axe fits the hand  

## Why it matters

Harness/skill design as **output modality control**, not only tool/prompt packing. Reduces review fatigue and context thrash when agents default to essay mode. Pairs with progressive-disclosure skill writing and agentic-engineer preference notes.

## Skeptical read

HumanLayer product skill + brew install CTA. Visuals can be wrong or pretty-wrong (Mermaid “sloppy”); still need V.U.E.-style verification. Prose isn’t always the enemy for soft reasoning.

## Related

- [[writing-agent-skills-posthog-ian-vanagas]]
- [[dark-arts-of-skill-engineering-pbakaus]]
- [[how-to-create-right-skill-ai-agent]]
- [[hundred-x-agentic-engineer-preferences-systematicls]]
- [[loop-engineering-quietly-ate-prompt-engineering]]
- [[reverse-prompting-101-alex-prompter]]
- [[huggingface-model-architecture-visualizer]]
- [[master-agent-architecture-harness-loop-graph-marfin]]
