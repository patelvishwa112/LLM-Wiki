# How Anthropic Enables Self-Service Data Analytics with Claude

**Author:** Chen Chang, Clement Peng, Justin Leder, Johanne Jiao, Josh Cherry (Anthropic Data Science & Data Engineering)
**source_url:** https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
**ingested:** 2026-06-07
**sha256:** 9b9076e28da9a9aa2a31dc30e331bfa34310a30fec89c4ad92d89a6284effcdc

---

At Anthropic, 95% of business analytics queries are automated via Claude, with ~95% accuracy in aggregate.

## The Core Problem

Data analytics is different from coding. Coding is an open-ended solution space that rewards creativity, with documentation and tests as natural guardrails. For analytics, there's often only a single correct answer using a single correct source — and no deterministic way of proving correctness.

The central problem is mapping a user's question to specific, up-to-date entities in the data model and knowing the correct way of working with them. If you can do that, the SQL is trivial.

## Three Failure Modes

1. **Concept ↔ Entity Ambiguity:** With hundreds of viable options in a data model (out of potentially millions of fields), the agent can't choose the correct fields. Example: "active users" — what actions constitute "active"? Include fraudulent users? What lookback window?

2. **Data Staleness:** Sources, business definitions, and schemas change constantly. Agent knowledge goes stale and returns subtly wrong answers.

3. **Retrieval Failure:** The right information exists in the data model and is properly annotated, but given the search space, the agent simply doesn't find it.

## The Agentic Analytics Stack

### Layer 1: Data Foundations

The most important layer. Standard data engineering practices (dimensional modeling, shift-left testing, freshness/completeness checks) still apply. What changes: the end user of your data model is no longer a data expert.

**Key practices:**

- **Create canonical datasets:** Curate a small set of heavily governed, single-source-of-truth datasets. Aggressively deprecate near-duplicates. When an agent searches for "revenue," it should find one governed answer, not forty candidates.
- **Enforce standards structurally:** Route agents to canonical models first. CI blocks changes that bypass governed layers. Mandate that downstream teams build on the governed layer or explain why not.
- **Colocate artifacts:** Nearly all data code (modeling, semantic layer, reference docs, dashboard definitions) lives in a single repo, with CI checks protecting cross-layer integrity. If a modeling change breaks a downstream dashboard, CI flags it and the fix ships in the same PR.
- **Treat metadata as a first-class product:** Column and table descriptions, canonical metric definitions, grain documentation, valid value ranges, lineage, ownership, model tiering — maintained with the same rigor as transformations themselves.

### Layer 2: Sources of Truth

Reference surfaces the agent consults to navigate the warehouse, roughly in descending order of trust:

- **Semantic layer:** Compiled metric and dimension definitions. Agents are structurally required (by skill instruction) to leverage this first. A bootstrapping attempt (LLM auto-generating metric definitions from raw tables) was net-negative — it encoded the very ambiguities they were trying to eliminate.
- **Lineage and transformation graph:** When the semantic layer doesn't cover a question, lineage lets the agent reason about which upstream models feed a concept, which are deprecated, and which share grain.
- **Query corpus:** Raw retrieval access to thousands of prior queries moved accuracy by less than a point. What works: distilling that corpus into structured per-domain reference docs and reusable analysis patterns in skills.
- **Business context:** A company knowledge graph (indexed docs, roadmaps, decision logs, org structure) so the agent can resolve ambient references like "the Q2 launch" and ask better clarifying questions.

The common failure pattern: poor or stale documentation. Claude drafts it, humans curate and own it.

### Layer 3: Skills

If sources of truth are declarative knowledge (what a metric means), skills are procedural knowledge: which sources to consult in what order, how to navigate ambiguity, what finished analysis looks like.

**Results:** Without skills, Claude's analytics accuracy didn't exceed 21% on evals. Adding skills gets numbers consistently above 95%, and ~99% in certain domains.

**Best practices:**

- **Pairwise skills:** A knowledge skill acts as a thin top-level router loading domain details on demand. An "unbook" skill encodes process: clarify the question → find sources → run query → adversarial review → report. Also bundles reusable analysis patterns (retention curves, rate decomposition, funnel analysis).
- **Reference docs written for LLM retrieval:** Describe tables (grain, scope, exclusions), gotchas (e.g., "exclude known free-email domains, but keep custom ones"), and explicit routing triggers without prescriptive recipes that go stale.
- **Skill maintenance as first-class:** Skill markdown files colocated in the same repo as transformation models. PR that changes a model must touch the skill file. ~90% of data-model PRs now include a skill change. Regularly prune skill scaffolding as models improve.
- **Consistent across surfaces:** Same skill provides the same answer in Slack, IDE, dashboard, standalone agent sessions. One canonical source (data repo), auto-synced to plugin marketplace, cloud storage, and MCP.

### Layer 4: Validation

**Offline evals:**
- Dashboard-based evals: auto-generated by Claude, human-validated, covering most common stakeholder questions
- Long tail evals: Claude generates plausible questions across the domain from business context
- Active correction harvesting: every time a stakeholder corrects the agent → candidate eval
- Anchor ground truth: pin every eval to a snapshot date, write against stable fact tables
- Gate launches per domain: domain owner can't announce until eval slice clears ~90%
- Diminishing returns past a few dozen evals per topic, and that ceiling drops with each model generation

**Ablation methodology:**
- Vary exactly one component, compare pass rates against fixed eval set
- Most useful ablation was negative: giving agent direct grep access to thousands of prior SQL queries moved accuracy by less than a point. The bottleneck wasn't access to prior work — it was structure (mapping a question to the right entity).
- Every meaningful skill edit gets a before/after run, delta in the PR description
- Keep a list of what didn't work (e.g., stacking additional doc refinement past a point was net-negative; swapping adversarial reviewer to cheaper model lost accuracy wins)

**Online validation:**
- Adversarial review: +6% accuracy, but +32% tokens and +72% latency
- Provenance footer on every response: source tier, data freshness, owner
- Data quality checks on referenced fields
- Passive monitoring: share of queries resolving through semantic layer, share using correction language
- Active correction harvesting: scheduled agent scans channels for corrections, drafts PR to fix reference doc

## Getting Started

If starting from zero: a handful of canonical datasets, a few dozen offline evals, and a thin knowledge skill capture most of the upside. Everything else is what they added once those were built.

## Key Finding

The greatest gains come from addressing each of the three failure modes: collapsing ambiguity into a single governed answer, making the answer easily discoverable, and flagging when either has gone stale.
