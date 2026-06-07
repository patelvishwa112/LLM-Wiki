# Using LLMs to Secure Source Code

**Author:** Eugene Yan, Henna Dattani, et al. (Anthropic)
**source_url:** https://claude.com/blog/using-llms-to-secure-source-code
**ingested:** 2026-06-07
**sha256:** 4d60fa74b1ddb2297e18418c2076488cd7985a616085d94f32a82c0b15943688

---

Anthropic's guide to using Claude Opus for vulnerability discovery and patching. Primary takeaway: **discovery is now straightforward to parallelize, and the bottleneck has shifted to verification, triage, and patching.**

As of May 22, 2026, Anthropic had disclosed 1,596 vulnerabilities from open source scanning. Only 97 had been patched.

## The Find-and-Fix Loop (6 Steps)

### 1. Threat Model: Define what counts as a vulnerability

The most common cause of false positives: the model lacks understanding of your trust boundaries. When the threat model was well-defined, findings were "exploitable 90 percent of the time."

**Two-step process:**
- **Bootstrap from code, docs, and vulnerability history:** Feed architecture docs, wikis, entry points, git history, past vulnerabilities. Have the model create a threat model with system context, assets, entry points, trust boundaries, and relevant vulnerability classes.
- **Interview someone who knows the system:** Use Shostack's four questions (what are we building, what can go wrong, what are we doing about it, did we do a good job). Run bootstrap first so the interviewee starts from a draft, not scratch.

**Key practices:**
- Consider dependencies' security policies directly (vLLM's security.md, SQLite's defense guide, ImageMagick's security policy)
- Name what is trusted (config files, authenticated clients)
- Include a THREAT_MODEL.md in the repo, updated as code changes
- Use the threat model in discovery (as scope/partitioning) and triage (as severity filter)

**Result:** One team had a 40% false positive rate because findings were reproducible and exploitable but didn't fit the project's threat model. Another CISO: "[The model has] good context of the code, but not good context of us."

### 2. Sandbox: Run agents safely and verify exploitability

**Isolation:** Containers for discovery agents reading code. MicroVMs (Firecracker) or full VMs with egress locked down for running targets and PoCs. Never have credentials available to the agent.

**Setup process:** Pull dependencies, build, install tools, deploy the target, run existing tests to confirm everything works. Snapshot the environment, remove network access, allow traffic only to the model API through a local proxy. Load snapshot at start of each run.

**Proof of exploitability:** Teams that gave the agent a test bed where it could compile code, run tests, and detonate PoCs saw non-exploitable findings drop significantly. One offensive-security team's assessment: "the biggest efficacy lever has been giving the model test beds, live systems, and running the PoCs."

**Pinning:** Image tags, commit SHAs, dependencies, build commands — all pinned. Cache locally so builds require no network. One team's scan flagged a vulnerability because the agent downloaded an older library version instead of what was deployed.

**If a representative sandbox is impractical:** Start with discovery from source code only. Frontier models are good at finding vulnerabilities from static analysis. The trade-off is more verification time without PoCs.

### 3. Discovery: Rich context, shorter prompts, useful tools

**Prompting tips:**
- Provide goal and context, not prescriptive checklists (they reduce creativity and generate fewer novel bugs)
- Try asking for a specific vulnerability class guided by prior CVEs
- Define structured output with rationale → finding → impact → severity, with an escape hatch for weak findings
- Give the model tools: grep, glob, SAST scanners, fuzzers. Let the model build tools as needed.

**Partition the search space:** First pass partitions by attack surface, endpoint, or component. Feed partitions to parallel discovery agents. Then run a system-level pass. Brute-force horizontal scaling hits diminishing returns — teams got "tons of issues, most duplicates."

**PoC generation:** If you have a sandbox, ask the discovery agent to build a PoC (script, crashing input, failing test). This helps the agent iterate and pin down the finding, and gives the verifier concrete evidence.

### 4. Verification: Filter out non-exploitable findings

**Discovery optimizes for recall; verification optimizes for precision.** Doing both in one step causes the agent to self-censor and exclude exploitable true positives.

**Verifier must be independent:** Fresh container, no shared filesystem or conversation history. Give the verifier only (1) the PoC or written finding and (2) the codebase, so it can search for mitigations the finder missed (upstream validation, auth gates, type constraints, unreachable code).

**Multi-verifier and adversarial approach:**
- Run multiple independent verifiers, take majority vote
- Prompt the verifier to assume each finding is a false positive and search for reasons it's wrong
- Adding an adversarial verifier roughly halved the rate of non-exploitable findings
- Requiring a PoC brought false positive rate to near zero

### 5. Triage: Deduplicate by root cause, rank by preconditions and impact

**If you submit too many bugs that are duplicated or have inflated severity, product engineers stop reading them.** Open source maintainers are especially vulnerable to alert fatigue.

**Deduplication:** First, cheap deterministic pass (same file, category, line numbers within 10). Then model-applied qualitative rules: treat as duplicate if same root cause, same vuln at multiple call sites, missing global protection reported per endpoint. Treat as distinct if different vulnerability classes, different variables reaching different sinks, independent bugs in one helper.

**Severity rubric:**
- Reachability: real entry point or internal-only?
- Attacker control: does untrusted input reach the sink intact?
- Preconditions: non-default setting, feature flag, narrow time window?
- Authentication: unauthenticated vs logged-in vs admin?
- Read vs. write
- Blast radius: one user or all?

Have the model write answers to each question before assigning severity — prevents anchoring on bug class. Zero preconditions + unauthenticated remote = critical/high. One or two preconditions = medium. Three+ or local-only = low.

### 6. Patching: Close the loop and improve context for next cycle

**TDD for patches:** Write a new test that fails with existing code. Implement the fix. Confirm the test passes without breaking anything else.

**Validation ladder (cheapest first):**
1. Build — compiles, new tests pass
2. Reproduce — original PoC should stop working
3. Regressions — original test suite still passes
4. Re-attack — fresh discovery agent runs adversarial check

**Common patch failures:**
- Too restrictive, breaking connections with other services
- Fixing the symptom instead of the root cause
- Human still needs to own the patch — validate as much as possible so human review requires less effort

**Close the loop:** Update the threat model with validated findings and patches. Feed past findings into the next scan's context. Each cycle hardens the codebase and makes the next scan better informed.

## Key Numbers

- 1,596 vulnerabilities disclosed from OSS scanning, 97 patched
- Well-defined threat model → 90% exploitable findings
- Adversarial verifier → halved non-exploitable findings
- PoC requirement → near-zero false positive rate
- Discovery is the easy part now — verification, triage, and patching are the bottleneck

## Getting Started

Clone `defending-code-reference-harness` repo, run `/quickstart` in Claude Code. Includes skills for interactive workflows and a demo harness for autonomous scanning. Also: `claude-code-security-review` GitHub Action for per-PR security review.
