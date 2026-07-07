---
tags:
  - skills
  - evals
  - agent-harness
  - claude-code
  - progressive-disclosure
  - skillsbench
  - arize
  - prompt-engineering
  - coding-tools
source: https://x.com/aparnadhinak/status/2074569427346174039
date: 2026-07-07
type: bookmark
author: aparnadhinak
description: "Aparna Dhinakaran + @seldo — five measured rules for writing agent skills (SkillsBench, SkillComposer); expert-authored, focused, routed, per-harness, weak-domain eval loops."
raw: "[[raw/aparnadhinak_2074569427346174039]]"
---

# How do you write a good skill? There's actual data now.

**Source:** [X Article @aparnadhinak](https://x.com/aparnadhinak/status/2074569427346174039) (co-authored @seldo)  
**Context:** Post-AIEWF synthesis of three papers measuring skills like any other engineering artifact.

## Definition

Skills = on-demand folders of procedural domain knowledge (instructions, vocabulary, scripts). **Recipes** (Gavrilescu) add evals, judges, and feedback on top. SkillsBench frames skills as portable applications on harness OS + model CPU — not system prompts, RAG snippets, or bare tool descriptions.

## Five measured rules

| # | Finding | Implication |
|---|---------|-------------|
| 1 | Model-authored skills **hurt** (~1.3 pt below no-skill) | Humans must supply expert vocabulary and judgment |
| 2 | **2–3 file** focused skills beat encyclopedic docs | Target repeated wrong judgments; thoroughness competes for attention |
| 3 | **196-skill** flood **−16 pts** vs selective load (+23% tokens) | Route/composer (tiny skill-ID model or internal MoE) is mandatory |
| 4 | Same skill: **4.1–25.7 pt** swing by harness | Ship per-target builds; Codex may ignore skill text |
| 5 | **+4.5** SWE vs **+51.9** healthcare gains | Invest in thin-pretraining / internal / regulated domains |

## Evaluation loop

With-vs-without automated scoring on fixed task suites. **16/84** SkillsBench tasks regressed with skills — polish can mask failure. Accept skill edits only when pass rates rise; ties to recipe/eval-first skill maintenance (Arize AX cited).

**Open gaps:** subjective quality (design), homogenization when everyone shares one frontend skill.

## Why it matters

Turns Hermes/Claude skill authoring from folklore into an eval-gated discipline: write, keep small, route, test per harness, aim at weaknesses — same substrate as trace-mining and harness improvement loops elsewhere in the vault.

## Related

- [[four-loops-ai-engineering-taxonomy-aparna]]
- [[anthropic-claude-code-skills-lessons]]
- [[build-claude-skill-never-paste-prompt-0xlagosaur]]
- [[hermes-seven-skills-cobi-bean]]
- [[problem-first-skill-invert-bad-ideas]]
- [[improving-agents-data-mining-traces]]