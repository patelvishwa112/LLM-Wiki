---
tags:
- graph-engineering
- loop-engineering
- agents
- multi-agent
- orchestration
- verification
- claude-code
- dynamic-workflows
- cost-optimization
- agent-harness
source: https://x.com/anatolikopadze/status/2080668775796314331
date: 2026-07-25
author: Anatoli Kopadze (@AnatoliKopadze)
type: bookmark
description: "Graph engineering field guide: fake-edge test, diamond (fan-out/reduce/synthesize), fresh-context checkers, anchors for truth, Claude Code 'workflow' fleets. Graphs buy breadth not judgment; Bun rewrite ~$165k caution."
summary: "Graph engineering field guide: fake-edge test, diamond (fan-out/reduce/synthesize), fresh-context checkers, anchors for truth, Claude Code 'workflow' fleets. Graphs buy breadth not judgment; Bun rewrite ~$165k caution."
raw: "[[raw/anatolikopadze_2080668775796314331]]"
---

# Graph engineering: fake edges, diamond, anchors

Long-form @AnatoliKopadze guide after the loops→graphs rename wave. Thesis: most people use AI at 5–10%; graph skill is designing how **hundreds** of jobs run, not doing one job better. Decades-old coordination pattern, new name (good news).

## Vocabulary

- **Node** — one bounded job, defined I/O contract (not free-text walls)  
- **Edge** — real data dependency; only counts if something real passes  
- Linear A→B→C→D is already a (sad) graph  

## Fake-edge test (headline move)

At each step: does this **need** the prior result? If no, parallelize. Example: review file A then B — no data dependency → run side by side. Most workflows hide 2–3 free waits. Model wasn't the bottleneck; the **line you drew** was.

40 sequential steps → 40 failure points + sum latency. Same work as a graph → few real deps, finishes at slowest **layer**.

## Diamond pattern

**Fan out → reduce (code) → synthesize (strong model).** Claude research-style. Ask "where is the split, where is the merge" not "more steps." Coordination as code (`workflow` in Claude Code) so handoffs don't re-spend main context.

## Checker is the trick

Never self-grade. Separate verifier node; **fresh context**; real signals (tests passed, not "agent said done"). Three lenses: correct / current / source real. Shared context = loop in costume.

## Break modes

1. Context collapse on fan-in → layered summaries  
2. False independence (shared files/APIs) → isolate workspaces (Bun overwrite story)  
3. Silent node death → merge steps count expected inputs  

## Skip the graph when

Small/isolated; step-by-step human approve; exploratory; truly sequential; fake-edge test finds no free edges.

## Anchors (deeper trap)

Topology ≠ truth. Self-referential audit graphs go green and still wrong. Need unarguable anchors: tests that ran, banked revenue, retained customers; frozen rules optimizers would weaken.

## Build / cost

Claude Code dynamic workflows via the word **workflow**. Ready diamonds: research desk, SEO, GTM, repo refactor, open-ended discovery. Public Bun rewrite example: ~50 workflows, ≤64 agents, ~11 days, **~$165k** usage + human supervision + reviewability criticism. Start small; caps and monitoring required.

## Skeptical read

Creator CTA (Telegram). Substance overlaps 0xcodez/akshay graph posts; strongest unique pack is fake-edge pedagogy + anchors + cost honesty.

## Related

- [[graph-engineering-substance-over-meme-akshay]]
- [[graph-engineering-14-step-roadmap-0xcodez]]
- [[graph-engineering-dynamic-workflows-fleet-0xcodila]]
- [[loops-vs-graphs-polygres-infinite-context-daleverett]]
- [[wtf-is-a-loop]]
- [[four-loops-ai-engineering-taxonomy-aparna]]
- [[claude-code-dynamic-workflows-intro]]
- [[fable-orchestrate-huge-project-40-subagents-ryancarson]]
