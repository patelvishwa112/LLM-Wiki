---
tags:
- security
- anthropic
- claude-code
- vulnerability-scanning
- skills
- enterprise
- threat-modeling
- sandbox
- agent-ops
source: https://claude.com/blog/using-llms-to-secure-source-code
raw: '[[raw/anthropic-securing-source-code-llms]]'
date: 2026-05-27
author: Eugene Yan, Henna Dattani, et al. (Anthropic)
type: bookmark
summary: 'Anthropic''s guide to using Claude Opus for security: a 6-step find-and-fix
  loop (threat model → sandbox → discovery → verification → triage → patching). Key
  insight: discovery is now easy to parallelize; the bottleneck is verification, triage,
  and patching. 1,596 OSS vulns disclosed, 97 patched. Well-defined threat model →
  90% exploitable findings. Adversarial verifier halves non-exploitables; PoC requirement
  → near-zero FPR.'
related:
- '[[anthropic-self-service-analytics-claude]]'
- '[[nvidia-skillspector-security-scanner]]'
description: 'Anthropic''s guide to using Claude Opus for security: a 6-step find-and-fix
  loop (threat model → sandbox → discovery → verification → triage → patching). Key
  insight: discovery is now easy to parallelize; the bottleneck is verification, triage,
  and patching. 1,596 OSS vulns disclosed, 97 patched. Well-defined threat model →
  90% exploitable findings. Adversarial verifier halves non-exploitables; PoC requirement
  → near-zero FPR.'
---

# Using LLMs to Secure Source Code

**Source:** Anthropic (Eugene Yan, Henna Dattani, et al.). Primary takeaway: discovery is straightforward to parallelize — the bottleneck has shifted to verification, triage, and patching.

## The Find-and-Fix Loop

```
Threat Model → Sandbox → Discovery → Verification → Triage → Patching
  (setup, once)   (setup, once)   ← ← ← ← loop ← ← ← ←
```

## 6 Steps

| Step | Purpose | Key Practice |
|------|---------|-------------|
| **1. Threat Model** | Define what counts as a vulnerability | Bootstrap from code/docs/CVEs + interview system owner. Include THREAT_MODEL.md in repo. |
| **2. Sandbox** | Isolate agents, prove exploits | MicroVMs with egress locked, credentials excluded. Pin everything. |
| **3. Discovery** | Find vulnerabilities | Partition search space → parallel agents. Shorter prompts beat checklists. |
| **4. Verification** | Filter non-exploitables | Independent verifier, adversarial stance. PoC requirement → near-zero FPR. |
| **5. Triage** | Deduplicate, rank severity | Root-cause dedup. Answer reachability/control/preconditions/auth/blast-radius before assigning severity. |
| **6. Patching** | Fix + close the loop | TDD: fail test → fix → pass → regressions → re-attack. Feed back into threat model. |

## Key Numbers

- 1,596 OSS vulnerabilities disclosed, 97 patched (5.9%)
- Well-defined threat model: 90% exploitable findings
- Adversarial verifier: halves non-exploitable findings
- PoC requirement: false positive rate near zero
- 40% false positive rate from team where findings were real but outside threat model

## Key Insights

- **Discovery ≠ security.** Finding is the easy part now. Verification, triage, patching are the real work.
- **Threat model is load-bearing.** "The model has good context of the code, but not good context of us." Without it, 40%+ FPR.
- **Separate discovery from verification.** Same agent doing both self-censors and excludes true positives.
- **Sandbox faithfully.** The agent downloading wrong library version → phantom vulnerability.
- **Triage prevents alert fatigue.** Send product engineers a pile where majority are non-exploitable → they stop reading.
