---
tags:
- autoresearch
- dynamic-workflows
- self-evolving
- agent-orchestration
- claude-code
source: https://x.com/alokbishoyi97/status/2064281952631525741
date: 2026-06-09
type: bookmark
author: alokbishoyi97
summary: 'evo 0.5 runs two concurrent workflows: the main optimize loop + a meta loop
  that observes and rewrites the harness (phases, prompts, gates, verifiers) on the
  fly. Dynamic workflows make the loop itself evolvable data instead of fixed in-context
  orchestration.'
raw: '[[raw/alokbishoyi97_2064281952631525741]]'
description: 'evo 0.5 runs two concurrent workflows: the main optimize loop + a meta
  loop that observes and rewrites the harness (phases, prompts, gates, verifiers)
  on the fly. Dynamic workflows make the loop itself evolvable data instead of fixed
  in-context orchestration.'
---

# Self-Evolving Autoresearch Workflow Loops

Alok Bishoyi's writeup on making evo's autoresearch loop self-evolving via concurrent meta-workflows.

## Key Idea
Dynamic workflows turn coordination into code. The loop's own shape (phases, prompts, gates) becomes data the system can evolve while running.

Relevant to Hermes goal-execution and self-improving agent systems.