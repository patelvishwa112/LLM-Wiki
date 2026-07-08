---
tags:
  - skills
  - agent-harness
  - claude-code
  - progressive-disclosure
  - skillsbench
  - prompt-engineering
  - security
  - agentskills
source: https://x.com/free_ai_guides/status/2071666929451094227
date: 2026-06-29
type: bookmark
author: free_ai_guides
description: "Practitioner guide to SKILL.md skills vs prompts/config, progressive disclosure, four failure-mode skill patterns, and community skill security."
summary: "Practitioner guide to SKILL.md skills vs prompts/config, progressive disclosure, four failure-mode skill patterns, and community skill security."
raw: "[[raw/free_ai_guides_2071666929451094227]]"
---

# How to Create the Right Skill for Your AI Agent

@free_ai_guides argues agents need **durable skills** (agentskills.io `SKILL.md`), not one-off prompts—citing **SkillsBench** (+16.2pp with curated skills; self-generated skills unreliable).

## Skill vs prompt vs config

| Mechanism | Load model |
|-----------|------------|
| Prompt | Ephemeral chat instruction |
| Config (CLAUDE.md, rules) | **Push** every session |
| Skill | **Pull** on relevance (YAML name + description triggers model-invoked load) |

**Progressive disclosure:** tier-1 metadata only in context → full SKILL.md when matched → scripts/templates at step time.

## Four failure modes → skill patterns

1. **Misalignment** → “grill me” / design-tree questioning before code  
2. **Verbose rediscovery** → shared `CONTEXT.md` / ubiquitous language skill  
3. **No feedback loop** → strict TDD skill (failing test first)  
4. **Mud architecture** → periodic depth/coupling review skill (Ousterhout-style)

## Writing + security

- Start from **problem/failure mode**; short descriptions with trigger + “do not fire” cues; many effective skills are &lt;30 lines.  
- Audit **community skills** (prompt injection / ToxicSkills-class risk); test in disposable projects.

## Related

- [[writing-good-skills-measured-rulebook-aparna]]
- [[anthropic-claude-code-skills-lessons]]
- [[build-claude-skill-never-paste-prompt-0xlagosaur]]
- [[your-ais-memory-is-quietly-making-it-dumber]]