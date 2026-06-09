---
tags: [skills, security, supply-chain, agent-security, nvidia, skillspector, static-analysis, claude-code, codex, antigravity, cursor, mcp, prompt-injection, ci-cd, github-actions, sarif]
source: https://x.com/dani_avila7/status/2063336153630011728
raw: "[[raw/dani_avila7_2063336153630011728]]"
type: article
author: Daniel San (@dani_avila7)
date: 2026-06-06
---

# NVIDIA SkillSpector: Static Security Scanner for AI Agent Skills

AI agents run code they didn't write — skills, tools, MCP servers, prompts pulled from external repos. The attack surface is real, and most teams aren't thinking about it yet. NVIDIA's SkillSpector is their answer.

## What it is

**SkillSpector** is a static security scanner built for AI agent skills (Claude Code, Codex, Antigravity, Cursor, etc.). It answers one question: **is this skill safe to install?**

Repo: https://github.com/nvidia/skillspector (Apache-2.0)

It analyzes the SKILL.md and every script in the folder, runs **64 detection patterns** across **16 categories**, and produces a risk score from 0–100 with a clear verdict.

## How it Works

The scanner builds a context from the skill folder, then runs analyzers in parallel:

1. **Prompt injection and instruction overrides**
2. **Data exfiltration** — env var harvesting, context leakage, external transmission
3. **Supply chain** — curl | bash, CVEs via OSV.dev, typosquatting
4. **Behavioral AST** — eval, exec, subprocess, dynamic imports
5. **Taint tracking** — credentials flowing to the network, file read to exfiltration
6. **YARA signatures** — malware, webshells, cryptominers
7. **MCP-specific patterns** — tool poisoning, unicode deception, least-privilege violations

## Scoring

| Severity | Points |
|----------|--------|
| LOW | +5 |
| MEDIUM | +10 |
| HIGH | +25 |
| CRITICAL | +50 |

- A single CRITICAL pattern puts you at 50 before anything else is counted
- If executable scripts are present, the total is **multiplied by 1.3**
- Final score maps to a verdict on 0–100 scale
- **Anything above 50 is blocked automatically**

Reports output as: terminal, JSON, Markdown, or SARIF (drops into CI cleanly).

## CI/CD Integration (GitHub Actions)

- On every PR touching the skills directory, only **changed skills** are scanned
- Fast, deterministic, **no API keys needed** in `--no-llm` mode
- Posts a **Markdown report** directly on the PR
- Uploads **SARIF** to the Security tab
- **Blocks merge** if any skill scores above 50
- A separate **weekly workflow** scans the full registry for ongoing visibility but never blocks — the gate only lives on PRs

## Real-World Example

Claude Code Templates (aitmpl.com) runs SkillSpector on every PR. A synthetic malicious skill submitted for testing scored **84/100 CRITICAL** and was blocked before merge.

PR example: https://github.com/davila7/claude-code-templates/pull/623

## Why It Matters

The Skills ecosystem is growing faster than security practices. Most developers installing a community skill have no idea what scripts it runs or where it sends data. SkillSpector makes that visible **before anything executes**.