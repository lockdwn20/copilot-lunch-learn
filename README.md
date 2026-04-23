# GitHub Copilot — Lunch & Learn Series
**Progressive Learning Path | 7 Sessions**

---

## Overview

This series is designed to build on each prior session, moving from foundational awareness to advanced customization and automation. Each session stands alone but rewards attendees who follow the full path.

| Session | Topic | Builds On |
|---------|-------|-----------|
| 1 | Chat Panel Fundamentals | — |
| 2 | Inline Suggestions & Editor Flow | Session 1 |
| 3 | Slash Commands & Structured Prompting | Sessions 1–2 |
| 4 | Git Workflows with Copilot | Sessions 1–3 |
| 5 | Test Generation Workflows | Sessions 1–4 |
| 6 | Custom Agents & Agent Instructions | Sessions 1–5 |
| 7 | MCP Integrations & Full Project Builds | Sessions 1–6 |

---

## Session 2 — Inline Suggestions & Editor Flow
**Prerequisite:** Session 1 | **Estimated Length:** 60 min

**Why here:** Inline suggestions are the most immediate Copilot experience — attendees will encounter ghost text the moment they open a file. Understanding how to work with it effectively is a natural complement to Chat panel fluency.

**Suggested Topics:**
- Ghost text completions — accepting, cycling, and dismissing suggestions
- Next Edit Suggestions — how Copilot predicts your next change
- Inline Chat (`Ctrl+I`) — asking questions without leaving the editor
- Writing comment-first prompts to guide inline suggestions
- When to use inline vs Chat panel

---

## Session 3 — Slash Commands & Structured Prompting
**Prerequisite:** Sessions 1–2 | **Estimated Length:** 60 min

**Why here:** Once attendees are comfortable with both Chat and inline suggestions, slash commands provide a precision layer — reducing ambiguity and improving consistency of results.

**Suggested Topics:**
- `/explain` — understanding unfamiliar code
- `/fix` — targeted error resolution
- `/tests` — scaffolding test coverage
- Combining slash commands with natural language for richer prompts
- Version variability — how to check available commands in your installed version

---

## Session 4 — Git Workflows with Copilot
**Prerequisite:** Sessions 1–3 | **Estimated Length:** 60 min

**Why here:** Git is where many non-developer-heavy teams feel least confident. This session bridges Copilot's AI assistance with everyday source control tasks in a way that directly reduces friction with AZDO workflows.

**Suggested Topics:**
- Commit message generation from staged changes
- Using Copilot Chat to review diffs and summarize changes
- Pull request descriptions — generating meaningful PR summaries
- Branch management concepts with Copilot assistance
- AZDO-specific considerations — pushing, PRs, and review workflows

---

## Session 5 — Test Generation Workflows
**Prerequisite:** Sessions 1–4 | **Estimated Length:** 60 min

**Why here:** Test generation requires understanding both the codebase and Copilot's context model — attendees need the prior sessions to get real value here. This session also reinforces the "always review output" discipline in a high-stakes context.

**Suggested Topics:**
- Generating unit tests for existing functions using Chat
- Using `/tests` slash command vs natural language prompts
- Reviewing and validating generated tests — what to look for
- Testing frameworks — how to guide Copilot toward the right library
- Iterating on test coverage through conversation

---

## Session 6 — Custom Agents & Agent Instructions
**Prerequisite:** Sessions 1–5 | **Estimated Length:** 60 min

**Why here:** Custom agents represent a shift from using Copilot to configuring it. This requires confidence with the tool before attendees can meaningfully define how it should behave.

**Suggested Topics:**
- What agent instructions are and where they live (`.github/copilot-instructions.md`)
- Defining project-wide coding standards and conventions
- Creating task-specific agent personas (e.g. a documentation agent, a review agent)
- Scoping agent tool access — what to allow and restrict
- Team-shared instructions — consistency across contributors

---

## Session 7 — MCP Integrations & Full Project Builds
**Prerequisite:** Sessions 1–6 | **Estimated Length:** 75–90 min

**Why here:** This is the capstone session — combining everything learned into an end-to-end workflow. MCP integrations extend Copilot into external systems, and full project builds demonstrate autonomous multi-step execution at scale.

**Suggested Topics:**
- What MCP (Model Context Protocol) is and why it matters
- Connecting Copilot to external tools and data sources via MCP servers
- Full project scaffolding — giving Agent mode a high-level goal and reviewing the output
- Handing off between Plan and Agent modes for complex builds
- Guardrails at scale — reviewing autonomous changes safely

---

## Recommended Cadence

| Cadence | Notes |
|---------|-------|
| **Bi-weekly** | Allows time to practice between sessions — recommended |
| **Monthly** | Better for teams with limited availability |
| **Weekly** | Fast-track option; risk of information overload |

---

*This series is designed to complement the GitHub Copilot for VS Code current release and may need adjustment as the product evolves.*
*Last updated: March 2026*
