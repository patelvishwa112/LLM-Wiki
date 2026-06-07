# Lessons from Building Claude Code: How We Use Skills

**Author:** Thariq Shihipar (Anthropic, Claude Code team)
**source_url:** https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
**ingested:** 2026-06-07
**sha256:** 83b08c86f01f1cedbcdf41ca5dd71138677fd19d7fe6c65ccd620027bfe51d78

---

What Anthropic learned building and scaling hundreds of skills internally. Skills are folders of instructions, scripts, and resources that agents discover and use — not just markdown files.

## 9 Categories of Skills

After cataloging all internal skills at Anthropic, they cluster into nine categories. The best skills fit cleanly into one; skills that straddle several confuse the agent.

### 1. Library and API Reference
Explain how to correctly use a library, CLI, or SDK. Often include reference code snippets and gotchas.

Examples: billing-lib (edge cases, footguns), internal-platform-cli (every subcommand with examples), sandbox-proxy (egress gateway configuration, connection refused debugging).

### 2. Product Verification
Describe how to test or verify that code is working. Often paired with Playwright, tmux, or external tools.

**Verification skills have had the most measurable impact on Claude's output quality internally.** Worth having an engineer spend a week making these excellent.

Examples: signup-flow-driver (headless browser with state assertions), checkout-verifier (drives Stripe test cards, verifies invoice state), tmux-cli-driver (for interactive CLI testing needing TTY).

### 3. Data Fetching and Analysis
Connect to data and monitoring stacks. Include libraries, credentials, specific dashboard IDs, and common workflows.

Examples: funnel-query (which events to join for signup→activation→paid), cohort-compare (retention comparison with statistical significance), grafana (datasource UIDs, problem→dashboard lookup), datadog (field reference, metric prefix conventions).

### 4. Business Process and Team Automation
Automate repetitive workflows into one command. Store previous results in log files for consistency.

Examples: standup-post (aggregates ticket tracker, GitHub, Slack → formatted standup), create-ticket (enforces schema + post-creation workflow), weekly-recap (merged PRs + closed tickets + deploys → recap post).

### 5. Code Scaffolding and Templates
Generate framework boilerplates for a specific function. Especially useful when scaffolding has natural language requirements.

Examples: new-framework-workflow (scaffolds with org annotations), new-migration (template + common gotchas), create-app (auth, logging, deploy config pre-wired).

### 6. Code Quality and Review
Enforce code quality and help review code. Include deterministic scripts for maximum robustness. Run automatically via hooks or GitHub Actions.

Examples: adversarial-review (fresh-eyes subagent critiques, iterates until findings degrade to nitpicks), code-style (enforces styles Claude doesn't do well by default), testing-practices (instructions on what to test and how).

### 7. CI/CD and Deployment
Help fetch, push, and deploy code. May reference other skills to collect data.

Examples: babysit-pr (monitors PR, retries flaky CI, resolves merge conflicts, enables auto-merge), deploy-service (build → smoke test → gradual rollout with error-rate comparison → auto-rollback), cherry-pick-prod (isolated worktree → conflict resolution → PR with template).

### 8. Runbooks
Take a symptom (Slack thread, alert, error signature), walk through multi-tool investigation, produce structured report.

Examples: service-debugging (maps symptoms→tools→query patterns), oncall-runner (fetches alert→checks usual suspects→formats finding), log-correlator (pulls matching logs from every system touching a request ID).

### 9. Infrastructure Operations
Routine maintenance and operational procedures, some involving destructive actions benefiting from guardrails.

Examples: resource-orphans (finds orphaned resources→posts to Slack→soak period→user confirms→cleanup), dependency-management (org's approval workflow), cost-investigation (why did storage/egress bill spike, with specific buckets and query patterns).

## Tips for Making Skills

### Don't state the obvious
Claude already knows how to code. Focus on information that pushes Claude out of its normal way of thinking. The frontend design skill is an example — built by iterating with customers on improving Claude's design taste, avoiding patterns like Inter font and purple gradients.

### Build a gotchas section
The highest-signal content in any skill. Built up from common failure points. Examples: "The subscriptions table is append-only. The row you want is the one with the highest version, not the most recent created_at." "This field is called @request_id in the API gateway and trace_id in the billing service. They're the same value."

### Use progressive disclosure
A skill is a folder, not just a markdown file. SKILL.md points to other files for specific situations. Split detailed function signatures into references/api.md. Include template files in assets/. Claude reads files at appropriate times.

### Avoid railroading Claude
Give Claude the information it needs, but flexibility to adapt. Being too specific in reusable instructions causes problems.

### Write descriptions for the model, not for humans
When Claude Code starts a session, it builds a listing of every available skill with its description. This listing is what Claude scans to decide "is there a skill for this request?" The description field is not a summary — it's a trigger description. Include trigger keywords like "babysit."

### Help Claude remember
Store data within skills — append-only text log files, JSON, or SQLite databases. A standup-post skill keeps a standups.log with every post, so next run Claude reads its own history and knows what changed. Use `${CLAUDE_PLUGIN_DATA}` for stable storage.

### Store scripts and generate code
Give Claude scripts and libraries so it spends turns on composition rather than reconstructing boilerplate. A data-science skill might include a library of functions to fetch data from your event source.

### Use on-demand hooks
Hooks activated only when the skill is called, lasting only for the session. Examples: `/careful` (blocks rm -rf, DROP TABLE, force-push via PreToolUse matcher), `/freeze` (blocks any Edit/Write outside a specific directory).

### Think through setup
Use config.json in the skill directory. If config is not set up, agent asks the user. Use AskUserQuestion for structured multiple-choice questions.

## Distributing Skills

Two methods:
- Check into repo under `./.claude/skills` — works for smaller teams across few repos
- Plugin marketplace — for scale, allows selective installation and setup flows

At Anthropic: no centralized team decides. Skills uploaded to a sandbox folder in GitHub, shared via Slack. Once a skill gets traction, PR to move it into the marketplace.

## Composing Skills

Dependency management not natively built into marketplaces yet, but you can reference other skills by name and the model will invoke them if installed.

## Measuring Skills

PreToolUse hook logs skill usage within the company. Find skills that are popular or undertriggering compared to expectations.

## Getting Started

Most of the best skills began as a few lines and a single gotcha, then improved as people kept adding to them as Claude hit new edge cases.
