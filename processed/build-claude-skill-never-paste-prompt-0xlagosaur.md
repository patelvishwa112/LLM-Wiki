---
tags: [skills, claude, claude-code, prompt-engineering, progressive-disclosure, agent-harness, hermes, mcp]
source: https://x.com/0xlagosaur/status/2068693290581414390
raw: "[[raw/0xlagosaur_2068693290581414390]]"
date: 2026-06-23
type: bookmark
author: 0xlagosaur
summary: "0xLagosaur on prompts vs Skills: SKILL.md folder with 'Use when I…' triggers, lazy-loaded instructions and references/, four copy-paste starters (voice, fact-check, should-i, checkpoint), and open standard across Claude Code, API, Cursor, Copilot."
---

# Build a Claude Skill — Stop Re-Pasting Prompts

By **@0xLagosaur**.

## Idea

Recurring prompts belong in **Skills** so the model **pulls** them when the job matches — same pattern as Hermes `skill_view` / `skill_manage` and Anthropic progressive disclosure.

| | Prompt | Skill |
|---|--------|-------|
| Who decides | You, every turn | Model when description matches |
| Context cost | Paste full text | Description always; body on trigger |

## Structure

```
job-name/
  SKILL.md          # name + description + instructions
  references/       # optional lazy-loaded refs
```

Description must mirror **your actual words** ("Use when I ask: should I ship this?").

## Starter pack (from article)

- **my-voice** — anti-slop writing rules  
- **fact-check** — claim ledger, no rewrite  
- **should-i** — ship/fix/kill  
- **checkpoint** — long-session handoff cap 200 words  

## Why it matters

Aligns with [[anthropic-claude-code-skills-lessons]], [[hermes-seven-skills-cobi-bean]], and vault SOP: procedures in skills, facts in memory. "Dotfiles for taste."

## Related

- [[anthropic-claude-code-skills-lessons]]
- [[15-claude-skills-that-stuck-vaibhav-sisinty]]
- [[hermes-seven-skills-cobi-bean]]
- [[feedback-loops-claude-code-less-babysitting]]
- [[problem-first-skill-invert-bad-ideas]]
- [[nvidia-skillspector-security-scanner]]