---
tags:
  - agents
  - agent-loops
  - codex
  - automation
  - deep-research
  - context-engineering
source: https://docs.google.com/document/d/14qXSLPBZENOTmYJMJPQ7xFRtMzm00qCF9foTKqque70/mobilebasic
date: 2026-10-28
type: article
author: unknown
summary: 'Method for turning a self-editing Codex heartbeat every ~1 minute into a long-running research loop: seed with known-good material, keep the automation prompt as the scratchpad, do one bespoke step per wakeup, and let entropy cascade into unknown-unknown discovery.'
description: 'Self-editing heartbeat loop for rare-token research: seed the first prompt with known-good sources, treat the automation prompt as a rewritable scratchpad, take one bespoke action per one-minute wakeup, checkpoint findings to a dataroom, and let random context injection diversify results.'
raw: '[[raw/gdoc_alpha-generation-self-editing-heartbeats]]'
status: current
as_of: 2026-10-28
---

# Alpha generation p1: self-editing heartbeats with seeds

An operating method, not a benchmark result: use an agent automation whose prompt the agent rewrites every cycle, so a research task can run for hours without losing its thread — and can drift productively instead of converging on consensus content.

## Key Takeaways

- **The problem is consensus retrieval.** Agents converge on surface-level, heavily-linked articles. A human rabbit hole finds the second-order Substack or the provincial government PDF; default agent search does not.
- **"Rare tokens"** = information-dense, valuable material that few people have read. That is the target metric of the loop, not volume of sources.
- **Seeding is the quality lever.** Give the model concrete examples of "what good looks like" before it searches: high-engagement posts with expert replies, niche search engines/aggregators (e.g. Secret Web), and sites worth reverse-engineering (government aggregators, regional postings).
- **Three components:** a Codex automation with a ~1 minute heartbeat (which wakes a thread and can edit itself), a scratchpad that lives directly in the automation prompt, and a dataroom where findings accumulate.
- **The agent loop per wakeup:** scope one extension of the task on the scratchpad → execute it → save results to the dataroom → seed the next points. The prompt is the working memory, rewritten each cycle.
- **It solves the bespoke-action problem.** At n=5 a model researches each item individually; at n=100 it batch-enriches and quality drops. A 1-minute heartbeat lets every iteration stay bespoke even at high total volume.
- **Entropy injection is a feature.** Context picked up mid-research updates the agent's priors and lets it cascade into adjacent territory. Sampling k runs produces materially more diverse datarooms than one long planned run.
- **Cost shape:** hundreds to thousands of one-minute cycles per run, so the economics only work when the value of the discovered material is high (deal sourcing, market mapping, literature search).

## The method, concretely

1. **Seed.** First prompt carries the exemplars (tweet + comments, niche index, source to reverse-engineer) and a compact statement of the objective.
2. **Automate.** One agent, one automation, ~60s cadence. Automation is self-editable, so the loop can change its own cadence/scope.
3. **Scratchpad.** Sections such as current objective, ranked leads, deprioritized items, next actions, guardrails, stop condition. Overwrite stale state rather than appending transcripts.
4. **One step per wakeup.** Validate or rank 1–3 items; never broad rescans. Checkpoint durable work (e.g. git commits when the project is a repo).
5. **Notify rarely.** Only when something crosses a defined threshold.
6. **Close the loop.** Delete or update the automation when the objective is done or stale.

The doc also ships an appended skill spec (`heartbeat-scratchpad-loop`) covering the same pattern: prefer heartbeat over cron when the work should continue in-thread; prefer cron only when the work should run detached against a workspace; split into scout / validator / monitor / coordinator automations only when the roles are genuinely separable.

## Reported case studies (self-reported, no baselines)

- **Neo-philanthropy.** Seeded with posts from Nan Ransohoff, Cate Hall, Peter Olivier, Dwarkesh. ~24h produced 841 X accounts, 923 interactions, ~150 useful articles, plus a reading map. Standout finds included Nadia Asparouhova's science-funding report, a FROs/BBNs essay, and a Metascience 101 episode.
- **Foreign industrial project lists.** A Hunan government commercialization posting was the seed; the agent followed ministry attachments and regional portals across languages into 100 more sources and 1,190 translated project ideas. One semiconductor-automation idea seeded a deeper run that reached 261 sources, 1,078 findings, a process map and a vendor landscape, including a Korean wafer-fab scheduling patent using RL + MCTS.
- **Biotech.** Seeded with three biotech-investment posts, recursively followed replies and profiles into 1,450 saved artifacts, 47 note packages, and an overview with 16 editorial picks and six key disagreements; it then wrote a 12-chapter beginner walkthrough with glossary. It converged on Octant Bio via Sri Kosuri's writing and the OpenADMET benchmark.

## Skeptical read

- Every output number is self-reported by the author; no control run, no precision/recall against a human-curated reading list, and no accounting of the per-cycle token cost. "150 helpful articles" is a judgment, not a measurement.
- Authority and popularity seeding biases the search toward who the field already cites — the entropy step widens the tail, but the seed still decides the center of gravity.
- A 1-minute heartbeat is a lot of inference for one unit of work per cycle; the pattern is best reserved for domains where a single rare find pays for the run.

## Related

- [[loop-engineering-clearly-explained]]
- [[agent-loops]]
- [[how-to-design-a-loop-that-prompts-your-agent]]
- [[context-engineering-os-loop-engineering-vartekxx]]
- [[9-step-loop-claude-code-senior-engineer]]
- [[guide-to-goal-codex]]
