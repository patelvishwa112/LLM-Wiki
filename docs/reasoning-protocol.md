---
title: Reasoning Protocol
type: meta
tags: [meta, reasoning, protocol, second-brain]
description: Depth-triaged, multi-order reasoning loop that pairs vault knowledge with web, emits a visible reasoning chain and labelled sources, with a cheap fast-path for trivial lookups.
status: current
as_of: 2026-09-12
---

# Reasoning Protocol

How the agent *thinks* over what it retrieves. `ROUTER.md` + `docs/retrieval-protocol.md` (T1) decide **what notes to open**; this file decides **how hard to think and how to answer honestly**. Temporal fields (`status`/`as_of`) are governed by `docs/supersession.md` (T3) — this protocol *consumes* them, it does not redefine them.

Design stance, in one line: **reason first to decide what you need, retrieve second, and only pay for depth when the question earns it.** Retrieving before reasoning wastes calls and can *harm* a reasoning chain injected mid-strategy; the win is "fewer, better-timed retrievals." [REALM-RETRIEVE]

This extends the five modes already in `CLAUDE.md` → *Intelligence Operations* (Connection Finder, Question Answerer, Synthesis Generator, Contradiction Detector, Discovery Engine). It does not replace them — it is the control loop that decides *which* mode(s) fire and how deep. Question Answerer is the fast-path floor; deep-path composes Synthesis + Contradiction + Connection + Discovery.

---

## 0. DEPTH TRIAGE (run this first, always)

Before any retrieval, classify the question. This is the gate that stops a "when did X ship" lookup from triggering an expensive three-order cascade, and stops a "should I re-architect my memory layer" question from getting a flat one-note answer.

**Decide in one pass. Default to FAST; escalate to DEEP only on a trigger.**

### FAST-PATH — a lookup. Answer from ≤2 notes, then STOP.
Take fast-path when the question wants a *fact, definition, link, number, list, or "what does my vault say about X"* and one or two notes settle it.

Trigger signals (any one → fast):
- Interrogatives: **what / who / when / where / which / does / is / how many / define / list / link to**.
- The answer is a single value, quote, date, entity, or an existing note's gist.
- No comparison, no "should," no causal chain requested.
- Retrieval (T1) returns a note whose `## section` directly contains the answer.

Fast-path procedure: run T1 (grep `INDEX.tsv` → score → open ≤2 notes), lift the answer, emit the **compact output contract** (answer + 1-line source label + recency note). Do **not** decompose, do **not** reason in orders, do **not** web-search unless T1 hits 0 after two reformulations or the note is older than the asked-about event. Stop.

### DEEP-PATH — analysis / strategy / causation. Run the full loop.
Take deep-path when the question wants *judgement, consequences, trade-offs, or a recommendation*.

Trigger signals (any one → deep):
- Interrogatives/verbs: **why / how should / what happens if / what would it take / is it worth / compare / trade-off / implications / risk / strategy / should I**.
- Two or more vault domains are implicated (cross-domain is where this vault's value lives — `CLAUDE.md`).
- A recommendation or decision is being requested, or the answer changes a plan.
- A contradiction or a stale claim is likely in play (T3 `status` conflicts among candidate notes).
- The honest answer needs downstream / systemic reasoning, not a single fact.

Ambiguous? Two cheap tests: (a) *Would a wrong answer cost more than the extra tokens of the deep loop?* If yes → deep. (b) *Can I answer it in one sentence with one citation and no "because"-chain?* If yes → fast. When still tied, run **one** grep; if the top-2 notes fully answer it, stay fast; if they raise a "but that depends on…", escalate.

---

## 1. THE DEEP LOOP

Five stages. Keep a running, visible reasoning chain (stage headers are the chain). Budget: aim ≤ ~12k reasoning+retrieval tokens; a genuinely systemic question may spend more, but name why.

### Stage 1 — Decompose
Break the question into 2–5 answerable **sub-questions**, ordered so earlier answers feed later ones. Separate the *factual* sub-questions (retrievable) from the *judgement* sub-questions (reasoned). Decomposition is what lets verification happen per-claim later, and is the single biggest lever on not hallucinating a confident-but-wrong synthesis. [CoVe]

State the sub-questions explicitly. Example shape: "(a) what does the vault currently hold on X? (b) what's the mechanism linking X→Y? (c) what breaks at scale? (d) what's the current external state-of-the-art I'm missing?"

### Stage 2 — Retrieve own knowledge (call T1, do not redefine it)
For the *factual/retrievable* sub-questions, run the **retrieval protocol** exactly as specified in `docs/retrieval-protocol.md` (via `ROUTER.md`): grep `INDEX.tsv` → score (`3·tag + 1·desc + 0.5·type + 2·recency`) → open ≤3 notes → optional ≤1 hop. Obey its stop rules and status gate. Deep-path may run T1 **once per sub-question cluster**, but each run still respects the ≤3-notes budget — decomposition, not brute force, is how you cover more ground.

Carry forward, per opened note: its `date`, its `status` (T3), and whether two notes **conflict**. Conflicts are not noise — they are Stage 3 and 5 inputs (Contradiction Detector).

### Stage 3 — Reason in orders
This is the core. Walk three orders explicitly; do not collapse them.

- **1st order — direct answer / facts.** What the notes + parametric knowledge say *directly*. The immediate, on-its-face answer to the question. (What TME calls the direct, immediate consequence. [TME])
- **2nd order — implications / knock-on effects.** "And then what?" Who or what this affects *next*; the indirect consequences a first-order answer overlooks; the incentives it creates. [TME: the next chain of consequences, often overlooked] Ask it literally: *given the 1st-order answer, what changes downstream, and for whom?*
- **3rd order — systemic / long-horizon.** The compounding, feedback-loop, and non-obvious effects over time; second-order effects of the second-order effects; where the system reshapes itself. [TME: broader systemic ripples that compound; self-reinforcing loops] Ask: *what feedback loop does this set up? what breaks or compounds a year out? what's the non-obvious consequence nobody's pricing in?*

Rule: **each order must add something the prior order didn't.** If 3rd-order just restates 2nd, you haven't reached it — push to a feedback loop, a compounding effect, or a second-order-of-a-second-order. Mark inferential leaps as inference (they become `inference`-labelled sources).

### Stage 4 — Gap-fill with web (name the gap first)
Before searching, **name what's missing or stale** — do not reflexively search. A retrieval injected during a strategy/exploration phase *harms* the reasoning in ~31% of failure cases; fewer, better-timed retrievals win. [REALM-RETRIEVE] Web is justified only for a *named, specific* gap, per the boundary in `docs/retrieval-protocol.md`:

- A **fact/number/date/quote** the ≤3 opened notes don't contain.
- Events **newer than the top note's `date`** (the vault's freshness ceiling; also a T3 supersession check — is my current note actually still current in the world?).
- Grep returned **0** after two reformulations.
- The user asks to **verify** a vault claim against a live source.

For each gap: search (`WebSearch`/`WebFetch`, never curl), **capture the source URL and its recency**, and **verify** — cross-check the web claim against the vault claim and against a second source when it drives the recommendation. This is the retrieve-then-verify step; treat a single uncorroborated web hit as `web (unverified)`. When web and vault **conflict**, prefer the more recent *and* apply T3: flag the vault note as possibly superseded, and say which you're trusting and why. [Knowledge-Conflict]

### Stage 5 — Synthesize
Produce the answer the individual notes don't contain (Synthesis Generator). Fold in: the three orders, the contradictions surfaced, the web-filled gaps. Then **calibrate confidence** — separately for the *facts* (are the sources solid, current, corroborated?) and the *reasoning* (how many inferential leaps, how load-bearing?). A well-supported fact reasoned through three shaky inferences is still only as strong as the chain. [Double-Calibration] Emit via the Output Contract.

---

## 2. OUTPUT CONTRACT

Every deep-path answer ends with the same skeleton so the reasoning is auditable and the sources honest. Fast-path uses only the compact form.

### Compact form (fast-path)
```
<answer — 1–3 sentences>
Source: <vault: processed/slug.md | web: url | inference> · as_of <date> · confidence <High/Med/Low>
```

### Full form (deep-path)
```
ANSWER
  <the recommendation / synthesis, up front>

REASONING CHAIN
  Sub-questions: <the decomposition>
  1st order: <direct facts/answer>
  2nd order: <implications, who/what it affects next>
  3rd order: <systemic / long-horizon / feedback loops / non-obvious>

CONTRADICTIONS / TENSIONS
  <notes or sources that conflict; which you trust and why; or "none surfaced">

CONFIDENCE
  <High/Med/Low> — facts: <why> · reasoning: <#leaps, how load-bearing>

RECENCY
  Vault freshness: <newest load-bearing note date>. Web checked: <date or "not needed">.
  Superseded? <any note flagged per T3, or "no">

SOURCES
  [vault]      processed/slug.md — <what it supplied>
  [web]        https://… (<date>) — <what it supplied> [verified/unverified]
  [inference]  <claim not in any source; my reasoning>
```

Every source line **must** carry one of the three labels — `[vault]`, `[web]`, `[inference]` — so the reader can tell accumulated knowledge from live lookup from the agent's own reasoning. This is non-negotiable; an unlabelled claim reads as fact and erodes trust.

---

## 3. WRITE-BACK RULE

The vault is "a training set building on itself" (`CLAUDE.md`). Reasoning that produces a **durable new insight** or exposes a **gap the vault should hold** is exactly the material worth persisting — otherwise the compounding stops.

Write back when (any):
- The synthesis produced a cross-domain insight **no single existing note contains** (Synthesis/Connection output).
- Stage 4 surfaced a fact/event the vault lacked and will want again.
- A contradiction between notes was **resolved** (record the resolution, don't silently pick a side).
- A web check showed a vault note is **superseded** by newer reality.

Do **not** write back: one-off lookups, restatements of an existing note, or anything speculative you'd label `inference` with Low confidence.

How (respect T3 + `CLAUDE.md` ingestion SOP — additive, never edit in place here):
1. New `processed/slug.md` with required frontmatter (`type`, `description`, `tags`, `date`), plus T3 fields: `status: current`, `as_of: <today>`.
2. If it **supersedes** an existing note's claim, do **not** delete the old note — per `docs/supersession.md`, set the old note's `status: superseded` and link forward; the new note carries `supersedes: [[old-slug]]`. Retrieval's status gate then prefers the new one automatically.
3. Put `## Related` wikilinks in the body (not YAML — breaks TAG-INDEX, per `CLAUDE.md`).
4. Rebuild the index so it's findable: `python3 scripts/build-search-index.py`; append changelog per SOP.
5. Label provenance in the note: if the insight is synthesis-over-vault, say so; if web-sourced, include `source:`/date.

Rule of thumb: **write back the conclusion and its provenance, not the whole reasoning transcript.** One tight note the next query can retrieve beats a wall of chain-of-thought.

---

## 4. WORKED EXAMPLES (real notes, this vault)

### Example A — FAST-PATH (a lookup)

**Q:** "How much does the typed graph add to GBrain's retrieval precision vs vector+keyword alone?"

**Triage:** interrogative "how much" + single number wanted + no "should"/causation → **FAST**.

**T1:** `grep -iE 'gbrain|brainbench' INDEX.tsv` → top hit `processed/gbrain-markdown-git-brain-mem0.md` (tags `gbrain, knowledge-graph, retrieval`; score dominated by 3 tag hits). Open one note, section `## Benchmark signal`.

**Answer (compact contract):**
> The typed regex/wikilink graph contributes **~31 P@5 points** over vector+keyword alone on GBrain's internal BrainBench v0.20 — relational questions ("who at portfolio companies…") need edges, not cosine alone. (Internal, non-head-to-head benchmark.)
> Source: [vault] processed/gbrain-markdown-git-brain-mem0.md · as_of 2026-06-26 · confidence High (single primary note, direct figure; caveat: vendor-internal benchmark).

One note, no orders, no web. Stop. (Total: ~1 grep + 1 sectional read ≈ 2k tokens.)

---

### Example B — DEEP-PATH (strategy / "what happens if", reaching 3rd order)

**Q:** "My second-brain agent keeps its knowledge as markdown+git with a grep'd `INDEX.tsv` (this vault). As it grows past ~2,000 notes, should I migrate to a vector-DB memory — and what happens if I don't?"

**Triage:** "should I" + "what happens if" + spans retrieval + agent-memory + this vault's own architecture → **DEEP**.

**Stage 1 — Decompose.**
(a) What does the vault's own design say about lexical-vs-embedding retrieval? (b) What does the field say markdown+git vs vector memory actually buys? (c) What breaks at scale for a grep-first index? (d) What's the current external state-of-the-art I might be missing? (e) So: migrate, don't, or a third option?

**Stage 2 — Retrieve own knowledge (T1, per `docs/retrieval-protocol.md`).**
- `grep -iE 'retrieval|embeddings|bm25' INDEX.tsv` → `docs/retrieval-protocol.md` (design rationale: lexical grep beats dense embeddings on small, structured, exact-term corpora; "add a dense sidecar as a *fourth* tier — do not replace tiers 1–3"; fuse with RRF).
- `grep -iE 'gbrain|agent-memory' INDEX.tsv` → `processed/gbrain-markdown-git-brain-mem0.md` (markdown+git = authoritative, diffable, revertible; graph beats vector on relational; nightly dream-cycle dedup/contradiction) and `processed/agent-memory-four-layer-stack-matthew-gunnin.md` ("markdown discipline, not embedding magic"; index always in context; gbrain MCP = semantic recall *over* the vault, not instead of it).
- Conflict check: no direct contradiction; all three converge on file-first-as-truth. `status` empty ⇒ current (T3).

**Stage 3 — Reason in orders.**
- **1st order (direct):** No, don't migrate *the source of truth*. The vault's own doctrine and two field notes agree markdown+git should stay authoritative; retrieval is grep-over-`INDEX.tsv`, and even the design explicitly reserves embeddings for a *4th tier sidecar*, not a replacement. At 550 notes the loop costs ~5k tokens/answer.
- **2nd order (implications):** At ~2k notes, grep hit-counts balloon — a broad keyword can return hundreds of rows, inflating the routing-token step the protocol was built to keep small, and **paraphrase recall degrades**: the agent silently misses relevant notes it can't keyword-match. The failure is *invisible* — answers look fine but quietly drop sources. That affects the owner (subtly worse answers) and every downstream write-back (built on incomplete retrieval).
- **3rd order (systemic / feedback loop):** The vault's whole thesis is "a training set building on itself." If retrieval silently under-recalls, **write-back compounds on gaps** — new notes synthesize over an incomplete view, contradictions go unsurfaced, and the compounding *reverses*: the graph accretes noise faster than signal, and trust erodes (the same self-reinforcing "culture of dishonesty" dynamic TME describes, here between agent and owner). The non-obvious consequence: a *later* forced migration to vector-only would be strictly worse than the sidecar-now move — it abandons git's diff/revert/dream-cycle contradiction-surfacing (a "dual source of truth" is exactly the anti-pattern gbrain warns against), and you'd re-embed 2k notes under time pressure. So the real answer isn't the binary the question poses.

**Stage 4 — Gap-fill with web (named gap).** Gap: *at what corpus size does lexical recall actually degrade, and is hybrid the current SOTA?* Vault asserts it but with no scale threshold; also want a claim newer than the 2026-06 notes.
- BM25/keyword holds on rare/exact terms but embeddings win on paraphrase recall as corpora grow; **hybrid retrieval fused with RRF (k=60) reliably beats either alone** — matches the vault's own sidecar recommendation. [sesen.ai, via retrieval-protocol.md; corroborated]
- Timing matters: "fewer, better-timed retrievals outperform frequent fixed-interval retrievals," and mid-reasoning retrieval can *harm* strategy phases. [REALM-RETRIEVE, 2026] → argues for a sidecar the agent *chooses* to consult, not always-on embedding.
- No source contradicts the vault; web *confirms and dates* the sidecar path. Verified across two.

**Stage 5 — Synthesize → Output Contract.**

> **ANSWER**
> Don't migrate — and don't stay static either. Keep **markdown+git as the source of truth** and add a **dense sidecar as the 4th retrieval tier** (exactly what `docs/retrieval-protocol.md` reserves), fused with your existing grep via **RRF**. Trigger the build when you observe recall misses, not at an arbitrary note count. This gets paraphrase recall without a dual source of truth or a panicked re-embed later.
>
> **REASONING CHAIN**
> Sub-questions: (a) vault doctrine (b) field consensus (c) scale failure mode (d) external SOTA (e) decision.
> 1st: vault + 2 notes agree file-first stays authoritative; embeddings are a sidecar, not a replacement.
> 2nd: at ~2k notes grep routing tokens balloon and paraphrase recall silently degrades → invisible under-recall.
> 3rd: under-recall + write-back → the "compounds on itself" thesis reverses; a later vector-only migration is strictly worse (loses diff/revert/dream-cycle, dual-truth anti-pattern). The question's migrate/don't binary is the wrong frame.
>
> **CONTRADICTIONS / TENSIONS**
> None between sources — vault and web converge. Tension is only in the question's framing (binary migrate-or-not) vs. the layered answer.
>
> **CONFIDENCE**
> Med-High — facts: three converging vault notes + two corroborating web sources, current. Reasoning: 2 load-bearing inferences (the 2k-note recall-degradation threshold is estimated, not measured on *this* corpus; "invisible under-recall" is inferred). Lower to Med if you need the exact threshold.
>
> **RECENCY**
> Vault freshness: newest load-bearing note 2026-07-02. Web checked 2026-09-12; nothing supersedes the sidecar recommendation. Superseded? No.
>
> **SOURCES**
> [vault] docs/retrieval-protocol.md — lexical-beats-dense rationale; explicit "dense sidecar as 4th tier"; RRF fusion.
> [vault] processed/gbrain-markdown-git-brain-mem0.md — markdown+git as diffable/revertible truth; graph>vector on relational; dual-truth risk.
> [vault] processed/agent-memory-four-layer-stack-matthew-gunnin.md — "markdown discipline, not embedding magic"; semantic recall as a layer *over* the vault.
> [web] sesen.ai BM25-vs-embeddings — hybrid + RRF(k=60) beats either alone; embeddings win paraphrase recall at scale (2026). verified.
> [web] arxiv REALM-RETRIEVE (2026) — fewer/better-timed retrievals win; mid-reasoning retrieval harms ~31% of failure cases → agent-chosen sidecar. verified.
> [inference] the ~2k-note degradation point and the "silent under-recall reverses compounding" feedback loop — my reasoning, not measured on this vault.
>
> **WRITE-BACK:** yes — this synthesis (file-first + RRF sidecar + trigger-on-observed-miss) is a durable cross-domain insight absent from any single note. New `processed/second-brain-retrieval-scaling-sidecar.md`, `status: current`, `as_of: 2026-09-12`, `## Related` → the three notes above. Rebuild index.

---

## Sources (this protocol's own research)

- TME.NET, *First-, Second-, and Third-Order Thinking & Consequences* — order definitions; third-order feedback loops / self-reinforcing systemic effects. https://tme.net/blog/first-second-third-order-thinking-consequences/
- *When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models* (REALM-RETRIEVE), arXiv 2026 — reason-then-retrieve; fewer better-timed retrievals win; mid-reasoning retrieval harms strategy phases (~31% of failure cases). https://arxiv.org/html/2604.26649v1
- Dhuliawala et al., *Chain-of-Verification Reduces Hallucination in LLMs*, arXiv:2309.11495 — decompose into independently-answerable verification questions before finalizing. https://arxiv.org/pdf/2309.11495
- *Explicit Knowledge Conflict Resolution for LLM Inference*, arXiv 2606.20245 — reconciling unreliable parametric vs contextual/retrieved knowledge. https://arxiv.org/html/2606.20245v1
- *Double-Calibration: Calibrating Knowledge and Reasoning Confidence*, arXiv 2601.11956 — calibrate the fact and the reasoning-chain confidence separately. https://arxiv.org/html/2601.11956v1
- Retrieval scaling / hybrid claims are inherited from `docs/retrieval-protocol.md` (sesen.ai BM25-vs-embeddings; Spice AI RRF) — not re-cited here.
