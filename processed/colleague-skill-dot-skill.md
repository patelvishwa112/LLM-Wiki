---
title: COLLEAGUE.SKILL — Expertise as Editable, Versioned Files
tags:
- skills
- agents
- agent-skills
- knowledge-capture
- claude-code
- hermes
source: https://x.com/alphasignalai/status/2061521674546119026
date: 2026-06-02
published: 2026-06-01
authors:
- AlphaSignal AI
- Shanghai AI Lab
type: bookmark
raw: '[[raw/alphasignalai_2061521674546119026]]'
description: COLLEAGUE.SKILL — dot-skill Paper from Shanghai AI Lab
---

# COLLEAGUE.SKILL — dot-skill Paper from Shanghai AI Lab

dot-skill reads a person's scattered work traces (docs, code reviews, chat decisions) and writes them into a SKILL.md that any compatible agent (Claude Code, OpenClaw, Codex, Hermes) can load. The paper drops the "digital twin" framing for a narrower claim: this is a file format for expertise, not a copy of a person.

## Key Takeaways

- **Work/persona split is the sharpest design choice.** work.md = what the person knows (review criteria, workflows, heuristics). persona.md = how they act (tone, interaction rules). Three entry points: full, work-only, persona-only. Work-only is safer.
- **Built on the Agent Skills standard.** SKILL.md folder + optional scripts/references. 215 community skills from 165 contributors. Hermes, Claude Code, OpenClaw, Codex all compatible.
- **Correction loop is plain English.** Say "he wouldn't push back there" — handler routes to work fix (patches a ## section) or behavior fix (appends {scene, wrong, correct} to persona.md). Auto-archives prior version, rollback to any of last 10.
- **No fidelity evidence.** Paper ships no held-out evaluation. Authors name "behavioral fidelity frontier" as their own open problem. You're trusting extraction quality you can't measure.
- **Persona tags can be dangerous.** Freeform tags like "blame-shifter" or "PUA" compile into Layer 0 rules. Demo shows the skill dodging blame on cue. Bias compiled into behavior, by design.
- **MIT license, real software.** Collectors, writer, installers, rollback, 35 passing tests. Hermes install: `python3 tools/install_hermes_skill.py --force`.

## Architecture

**S = (A, M, L):** Generated files (A), install metadata (M), lifecycle state (L) — version, correction count, rollback history.

**Seven output files (schema v3):** SKILL.md, work.md, persona.md, work_skill.md, persona_skill.md, manifest.json, meta.json.

**Three presets:** colleague (main), celebrity, relationship.

**Trace ingestion:** Auto-collect from Feishu/DingTalk/Slack, or upload PDFs, screenshots, .eml, pasted text. Can also skip collection and generate from intake alone.

## AlphaSignal's Verdict

Adopt the work-only path. Package a departing engineer's review checklist as work.md, test against graded reviews, keep persona off until fidelity is measured. The product page sells digital twins but the paper only claims a file format.

## Relevance to Hermes

This is how Hermes skills should be authored — inspectable, versioned, correctable in plain English. The work/persona split mirrors what we already do with skills (capability) vs persona (the Hermes Agent Persona doc). The correction loop (plain English → patch → archive → rollback) is worth stealing for skill maintenance workflows.

Key caution: persona tagging can encode bias. Hermes's persona is already defined — the question is whether auto-generated persona skills could be useful or just dangerous.

## Links

- Paper: https://arxiv.org/abs/2605.31264
- Repo: https://github.com/titanwings/colleague-skill
- Gallery: https://titanwings.github.io/colleague-skill-site/
- Agent Skills standard: https://agentskills.io/home

## Related

- [[rethinking-search-as-code-generation]]
