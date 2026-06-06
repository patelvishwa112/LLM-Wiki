---
source_url: https://github.com/github/spec-kit
ingested: 2026-06-06
sha256: 5de229ea524414d88ac037d8c48a7253811c59577e0e0b43626735953ae3ea9e
author: github
---

# 🌱 Spec Kit — Spec-Driven Development Toolkit

By GitHub. 109k stars, 9.7k forks, MIT License. https://github.com/github/spec-kit

## What is Spec-Driven Development?

Spec-Driven Development **flips the script** on traditional software development. For decades, code has been king — specifications were just scaffolding we built and discarded once the "real work" of coding began. Spec-Driven Development changes this: **specifications become executable**, directly generating working implementations rather than just guiding them.

## ⚡ Get Started

### 1. Install Specify CLI

Requires **[uv](https://docs.astral.sh/uv/)**. Replace `vX.Y.Z` with the latest tag from [Releases](https://github.com/github/spec-kit/releases):

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

### 2. Initialize a project

```bash
specify init my-project --integration copilot
cd my-project
```

To check for updates or upgrade:

```bash
specify self check
specify self upgrade --dry-run
specify self upgrade
specify self upgrade --tag vX.Y.Z[suffix]
```

### 3. Establish project principles

Use the **`/speckit.constitution`** command to create your project's governing principles and development guidelines that will guide all subsequent development.

```bash
/speckit.constitution Create principles focused on code quality, testing standards, user experience consistency, and performance requirements
```

### 4. Create the spec

Use the **`/speckit.specify`** command to describe what you want to build. Focus on the **what** and **why**, not the tech stack.

```bash
/speckit.specify Build an application that can help me organize my photos in separate photo albums...
```

### 5. Create a technical implementation plan

Use the **`/speckit.plan`** command to provide your tech stack and architecture choices.

```bash
/speckit.plan The application uses Vite with minimal number of libraries...
```

### 6. Break down into tasks

Use **`/speckit.tasks`** to create an actionable task list from your implementation plan.

```bash
/speckit.tasks
```

### 7. Execute implementation

Use **`/speckit.implement`** to execute all tasks and build your feature according to the plan.

```bash
/speckit.implement
```

## Video Overview

https://www.youtube.com/watch?v=a9eR1xsfvHg

## 🤖 Supported AI Coding Agent Integrations

Spec Kit works with 30+ AI coding agents — both CLI tools and IDE-based assistants. Run `specify integration list` to see all available integrations.

## Available Slash Commands

### Core Commands

| Command                  | Agent Skill            | Description                                                                |
| ------------------------ | ---------------------- | -------------------------------------------------------------------------- |
| `/speckit.constitution`  | `speckit-constitution` | Create or update project governing principles and development guidelines   |
| `/speckit.specify`       | `speckit-specify`      | Define what you want to build (requirements and user stories)              |
| `/speckit.plan`          | `speckit-plan`         | Create technical implementation plans with your chosen tech stack          |
| `/speckit.tasks`         | `speckit-tasks`        | Generate actionable task lists for implementation                          |
| `/speckit.taskstoissues` | `speckit-taskstoissues`| Convert generated task lists into GitHub issues for tracking and execution |
| `/speckit.implement`     | `speckit-implement`    | Execute all tasks to build the feature according to the plan               |

### Optional Commands

| Command              | Agent Skill            | Description                                                                                                                          |
| -------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `/speckit.clarify`   | `speckit-clarify`      | Clarify underspecified areas (recommended before `/speckit.plan`)                                                |
| `/speckit.analyze`   | `speckit-analyze`      | Cross-artifact consistency & coverage analysis (run after `/speckit.tasks`, before `/speckit.implement`)                             |
| `/speckit.checklist` | `speckit-checklist`    | Generate custom quality checklists that validate requirements completeness, clarity, and consistency (like "unit tests for English") |

## 🧩 Extensions & Presets

Spec Kit can be tailored through two complementary systems plus project-local overrides:

| Priority | Component Type                                    | Location                         |
| -------: | ------------------------------------------------- | -------------------------------- |
|      ⬆ 1 | Project-Local Overrides                           | `.specify/templates/overrides/`  |
|        2 | Presets — Customize core & extensions             | `.specify/presets/templates/`    |
|        3 | Extensions — Add new capabilities                 | `.specify/extensions/templates/` |
|      ⬇ 4 | Spec Kit Core — Built-in SDD commands & templates | `.specify/templates/`            |

**Templates** are resolved at **runtime** — Spec Kit walks the stack top-down and uses the first match.

**Extension/preset commands** are applied at **install time** — when you run `specify extension add` or `specify preset add`, command files are written into agent directories.

### Extensions — Add New Capabilities

Use when you need functionality beyond Spec Kit's core — new commands and templates.

```bash
specify extension search
specify extension add <extension-name>
```

Examples: Jira integration, post-implementation code review, V-Model test traceability, project health diagnostics.

### Presets — Customize Existing Workflows

Use when you want to change *how* Spec Kit works without adding new capabilities. Override templates and commands.

```bash
specify preset search
specify preset add <preset-name>
```

Examples: regulatory traceability, Agile/Kanban adaptation, mandatory security review gates, enforce test-first task ordering, localize to different languages.

### When to Use Which

| Goal | Use |
| --- | --- |
| Add a brand-new command or workflow | Extension |
| Customize the format of specs, plans, or tasks | Preset |
| Integrate an external tool or service | Extension |
| Enforce organizational or regulatory standards | Preset |
| Ship reusable domain-specific templates | Either |

## 📚 Core Philosophy

- **Intent-driven development** where specifications define the "*what*" before the "*how*"
- **Rich specification creation** using guardrails and organizational principles
- **Multi-step refinement** rather than one-shot code generation from prompts
- **Heavy reliance** on advanced AI model capabilities for specification interpretation

## 🌟 Development Phases

| Phase                                    | Focus                    | Key Activities                                                                                                                                                     |
| ---------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **0-to-1 Development** ("Greenfield")    | Generate from scratch    | Start with high-level requirements, generate specifications, plan implementation steps, build production-ready applications |
| **Creative Exploration**                 | Parallel implementations | Explore diverse solutions, support multiple technology stacks & architectures, experiment with UX patterns |
| **Iterative Enhancement** ("Brownfield") | Brownfield modernization | Add features iteratively, modernize legacy systems, adapt processes |

## 🔧 Prerequisites

- **Linux/macOS/Windows**
- Supported AI coding agent
- [uv](https://docs.astral.sh/uv/) for package management (recommended) or [pipx](https://pipx.pypa.io/)
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## 📄 License

MIT License.
