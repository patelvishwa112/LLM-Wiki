---
tags:
  - agents
  - project-ideas
  - critique
  - agentic-ai
  - personal-tools
created: 2026-05-30
source: Claude Code DeepSeek V4 Pro research session
type: research-synthesis
related:
  - "[[Agent Systems and Context Engineering Projects 2026]]"
  - "[[Bookmarks Index]]"
---

# Non-Obvious Agent Projects — Beyond the Listicles

**Generated:** May 30, 2026 via Claude Code on DeepSeek V4 Pro
**Prompt:** Find the popular "learn agentic AI" project lists, critique them, propose genuinely interesting alternatives

## The Standard Lists (What Everyone Builds)

Every "top 10 agent projects" list converges on these 8 templates:

| Project | Reality |
|---------|---------|
| Chatbot / Customer Support | LLM + system prompt + maybe vector DB |
| RAG "Chat with PDFs" | Embeddings → vector DB → LLM |
| Web Research Agent | Search API → scrape → summarize |
| SQL Query Agent | NL → schema → LLM generates SQL |
| Multi-Agent Content Crew | 3 LLM calls with role-named prompts |
| Code Review Agent | Diff → LLM → checklist |
| Email Responder | LLM + Gmail API wrapper |
| Financial Analyst | Stock API → LLM sentiment summary |

## Why They're Boring (7 Criticisms)

1. **All the same shape:** `structured input → LLM call → structured output`. Once you've built one, you've built all.

2. **"Multi-agent" is LARPing:** Giving LLMs role names and passing messages. In 95% of cases, a single well-prompted LLM does better. Adding latency and cost for an org chart.

3. **Zero learning:** None get better over time. Same failure modes on day 100 as day 1. Calling a vector DB "memory" is like calling a cache a personality.

4. **Solutions looking for problems:** "Travel planner" — Google Flights exists. Built because it's easy, not because it needs to exist.

5. **No real-world constraints:** No budget management, no reliability engineering, no prompt drift detection, no evaluation harness.

6. **All request-response, no continuity:** No agent runs continuously, maintains state, makes decisions over time, or notices things without being asked.

7. **The evaluation void:** Success criterion is "did it run without errors." Never "is this actually getting better, and how would I know?"

---

## 5 Actually Interesting Projects

### 1. Adversarial Critic Agent — Learns Your Blind Spots

**The spark:** The best engineers argue with themselves. Can an agent develop a model of *your specific blind spots* and get better at finding arguments you actually change your mind about?

**Mechanism:** Watches your Claude Code / Hermes workflow. Interrupts with "have you considered X?" Tracks which critiques you act on vs dismiss. Learns which interventions change your behavior. Over weeks, builds a calibrated model of your cognitive blind spots.

**Surprise outcome:** You discover you're overconfident about performance claims and underconfident about architectural decisions — and the pattern is consistent enough that it preempts you: "You're about to optimize prematurely. Your last 4 premature optimizations added complexity for <2% improvement."

**Time:** 2-3 weeks

### 2. Attention Archaeology Agent — Signal You Missed

**The spark:** How many times have you realized, three weeks too late, that someone already told you the answer? A paper in Slack you skimmed, a PR comment you meant to follow up on.

**Mechanism:** Continuously ingests everything you consume (browser history, Slack, email, GitHub, Claude conversations). Periodically surfaces "the signal you missed" via resonance detection: "Three weeks ago, Alice shared a paper about exactly the failure mode you're debugging right now."

**Surprise outcome:** You miss ~40% of information that later turns out relevant, and the patterns of what you miss (long-form, low-urgency, from people outside immediate team) are highly predictable.

**Time:** 3-4 weeks

### 3. Belief Calibration Agent — Your Predictions vs Reality

**The spark:** You make predictions constantly — "this will be 2x faster," "we can ship in 3 weeks." How often are you right? Where are you wrong consistently?

**Mechanism:** Monitors conversations for explicit predictions and confidence claims. Logs them. Checks back against reality over days/weeks. Builds a personal calibration curve showing which domains you're overconfident in, which you're underconfident in.

**Surprise outcome:** You're well-calibrated on technical estimates but systematically overconfident about human/organizational timelines. Or calibration degrades measurably when context-switching across >3 projects.

**Time:** 2-3 weeks

### 4. Codebase Anthropology Agent — Git as Fossil Record

**The spark:** A codebase is a fossil record of organizational behavior. Which team's abstractions keep getting ripped out? Whose code gets refactored most by others? Where do comments accumulate and rot?

**Mechanism:** Runs `git log` analysis continuously. Watches for ownership churn hotspots, abstraction lifecycle (added → trusted → questioned → removed), comment rot rates, file-level bus factor. Produces periodic "state of the codebase" anthropology reports.

**Surprise outcome:** The correlation between "clean code" metrics and "code that actually ships value" is close to zero. The most valuable engineers aren't the ones who write the most code — their code survives the longest without being rewritten.

**Time:** 1-2 weeks

### 5. Regulatory Pre-Mortem Agent — Future-Proof Your AI Systems

**The spark:** Everyone is building AI in a shifting regulatory landscape. The question isn't "are we compliant today" — it's "if a regulator looks at this in 2027, what will they flag?"

**Mechanism:** Takes project description, architecture, data flows, model choices. Simulates "regulatory futures" by reading current regulatory trajectory (EU AI Act, NIST, FTC). Generates pre-mortems from a future regulator's perspective. Produces gap analysis between current documentation and what you'd need to defend.

**Surprise outcome:** Most teams document what's technically interesting (architecture, performance) and completely neglect what regulators actually care about (data lineage, decision audit trails, human override pathways, disparate impact analysis).

**Time:** 2-3 weeks

---

## Why These Are Different

Every one:
- **Runs continuously or across time**, not just request-response
- **Learns and adapts** from actual outcomes
- **Surfaces non-obvious patterns** you wouldn't think to look for
- **Has a real feedback loop** — you know it's working when it tells you something you didn't already know
- **Treats the agent as observer/analyst**, not a task-completion machine
- **Could genuinely surprise you** with its findings

The standard listicle projects answer "can I wire up an LLM to an API?" — answered in 2023. These answer "can an agent help me understand something I wouldn't have seen on my own?"
