---
source_url: https://parlance-labs.com/blog/posts/auto-evals/
ingested: 2026-07-13
author: Antaripa Saha, Hamel Husain
title: "Do Automated Evals Work?"
note: Body via Playwright MCP evaluate on parlance-labs.com; Firecrawl credits exhausted
sha256: 6541a549e600eaae70c1c12fd974ce2c5f8c6fab5c358058cee03be096a3adee

---

# Do Automated Evals Work?

**Authors:** Antaripa Saha, Hamel Husain (Parlance Labs)  
**Published:** July 11, 2026  
**URL:** https://parlance-labs.com/blog/posts/auto-evals/  
**Tags (site):** LLMs, Evals

---

We compared 100 human-annotated traces against automated eval systems. Here’s what we found.

For the past three years, we have answered most questions about AI evals with the same advice: look at your data. In practice, looking at your data means error analysis, where you read your production traces (or logs) and catalog how your product fails. Reviewing traces also changes what you look for. You need criteria to grade outputs, but grading outputs is how you discover your criteria, a phenomenon known as criteria drift. For this reason, we argued against outsourcing evals to an LLM.

Popular eval tools now nudge people the other way. Braintrust, Arize, and LangSmith have each shipped an agent (Loop, Alyx, and Engine) that reads your production traces and reports what is failing. Coding agents have become capable enough to attempt the same job from a folder of log files or traces. We believe in using AI in any workflow where it helps. However, the temptation with these tools is to take the human out of the loop entirely. This raises an important question: how much can these systems catch on their own, and what do they miss?

To find out, we tested it. First, we prepared a dataset of 100 traces from a production apartment-leasing AI, working with a domain expert to label failures by hand. Then we masked those labels and asked each system to review the traces and find the errors on its own. This allowed us to compare human versus automated error analysis.

The automated systems performed admirably. The best recovered 87 percent of failures flagged by humans. Additionally, every system found issues humans missed. But there were downsides. Fully automated approaches always failed to catch interactions that “looked correct” but fell short of providing a great user experience. The systems also flagged a fair number of issues that were not failures, which added some noise.

The rest of this post covers the experiment, the results, and how we would modify the approach to be effective.

## The experiment

The traces come from a real AI agent for apartment leasing (Nurture Boss). Prospects text or call about apartments, and the agent answers questions and books tours. Certain conversations are supposed to be handed to a human. Importantly, this experiment is run on traces from real customers instead of a synthetic benchmark.

To prepare the dataset, a domain expert labeled 100 traces by hand, following the error analysis process. That review produced a failure taxonomy with 39 labeled failures.

We then masked all human annotations and fed the traces to each system with a deliberately light prompt: describe the product briefly, ask for recurring failures and issue clusters with example trace IDs, note acceptable/inconclusive traces, suggest candidate evaluators — without referencing any external rubric or known failures. Each trace also contained an extensive system prompt detailing desired behavior.

Lastly, we wanted to experience each product’s workflow, and we hoped the tools would ask follow-up questions or elicit requirements from us before starting the analysis. They largely did not.

### Scoring

- **Recall:** how many of the 39 human-labeled failures it found.
- **Precision:** how many of the errors flagged were real failures (match human label OR valid issue human missed).
- **Discoveries:** valid flags absent from human review.

Caveat: one dataset, 39 labeled failures — differences between systems come down to a handful of traces. Ranking vendors was not the goal.

## What the tools caught

| System | Recall | Precision | Discoveries | False positives |
|--------|--------|-----------|-------------|-----------------|
| Braintrust Loop | 87.2% | 79.1% | 20 | 9 |
| Arize AX Alyx | 74.4% | 91.0% | 19 | 3 |
| LangSmith (chat agent) | 79.5% | 77.5% | 20 | 9 |
| Codex (GPT-5.5 High) | 84.6% | 82.8% | 20 | 11 |
| Factory Droid (GPT-5.5 High) | 84.6% | 83.3% | 17 | 10 |
| Claude Code (Claude Opus 4.8) | 79.5% | 77.4% | 17 | 14 |

Every system did well when a failure was obvious in the trace: unsupported scheduling claims, repeated confirmation requests, promised follow-ups that didn’t happen, answers contradicting tool output.

Each system also found 17–20 minor issues human review missed (e.g., booking success but agent re-asked for a confirmation already given).

### Platform notes

- **Braintrust Loop:** Highest platform recall; easy upload/export; marked some traces acceptable/inconclusive; more false positives (too strict on completeness, treated internal tool metadata as user-facing).
- **Arize AX Alyx:** Highest precision (91%); strong on ungrounded claims (e.g., “lofts,” affordable housing mislabel, floor level without data); workflow rough spots early (first-200-chars read, compaction/timeouts — Arize fixed quickly).
- **LangSmith:** Best UI for reading traces; Engine found too few issues for full 100-trace comparison, so scored chat agent instead; great citation of exact messages/tools; severity ratings sometimes inflated on wrong findings.
- **Coding agents (Codex, Factory Droid, Claude Code):** Competitive with platforms on finding quality; quoted exact tool args/dates/prices; caught some subtle misses platforms didn’t; platforms win on workflow (link findings to traces, re-run on new data).

## What every system missed

Misses were systematic: traces that *look correct* but fail product goals. Human review caught several that no system flagged reliably:

1. **Sales objections** — agent gave up at first objection instead of addressing concern (leasing goal).
2. **Markdown in SMS** — markdown formatting arrives as stray asterisks on phones.
3. **Interruptions** — voice agent talked over callers.
4. **Missed handoffs** — business rules required human routing; agent kept the conversation.

None are fully visible from the transcript alone without product/business context. That context is often only discovered via human error analysis (**criteria drift**). Tools largely did not interview the operator for missing context.

## What we would do instead

Steering with a full description of good/bad would catch more — but that description rarely exists at the start of evals.

No system treated error analysis as an interview. Preferred workflow (Shreya Shankar demo): annotate traces yourself; coding agent watches annotations (e.g. Claude monitor), builds a failure taxonomy, surfaces new suspected instances; human accepts/dismisses; each round pulls product context into the eval suite. Human stays the judge; AI multiplies throughput.

> As an AI product builder, you should stay in the loop instead of completely outsourcing evals to AI. If a tool could find and fix every issue on its own, it would do the same for your competitors, and there would be nothing left to set your product apart. To stand out, look at your data.

P.S. AI Evals course (live cohort) mentioned for hands-on help.

## Footnotes (condensed)

- Error analysis FAQ; Hamel on not outsourcing evals (“Revenge of the Data Scientist”).
- Vendor agents: Braintrust Loop, Arize Alyx, LangSmith Engine.
- Product: Nurture Boss; Hamel’s “Field Guide to Rapidly Improving AI Products.”
- Dataset not redistributable (permission to analyze/write only).
- No vendor affiliation/sponsorship.
- Criteria drift: Shankar et al., “Who Validates the Validators?”
- Shreya Shankar co-teaches AI evals course.
