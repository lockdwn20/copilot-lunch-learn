# GitHub Copilot in VS Code — Lunch & Learn
**Session 3: Slash Commands & Structured Prompting | Speaker Notes | 60 Minutes**

---

## 0:00 – 0:05 | Welcome & Session 2 Recap

**What to say:**
- Welcome back — today we add precision to everything we've learned so far
- Quick Session 2 recap: ghost text completions, Next Edit Suggestions, Inline Chat with `Ctrl+I`, comment-first prompting
- Today's focus: slash commands — shorthand instructions that remove ambiguity and give Copilot a clear, structured intent
- Same rule applies: **always review output before accepting**

---

## 0:05 – 0:15 | Slash Commands Overview

**What slash commands are:**
- Slash commands are shorthand prompts for common tasks — type `/` in the Chat panel or Inline Chat to see available options
- They remove the need to write complex natural language instructions for things Copilot already knows how to do well
- They work in both the Chat panel and Inline Chat (`Ctrl+I`)

**How to access them:**
- In the Chat panel: type `/` in the input field — a popup list of available commands appears
- In Inline Chat: press `Ctrl+I`, then type `/` — same popup, scoped to the editor context
- Commands are context-aware — the list may vary depending on what you have selected

**Version variability — important callout:**
- Available slash commands vary depending on your installed Copilot version and subscription tier
- Always type `/` first to see what's actually available in your environment rather than assuming
- If a command isn't listed, it likely isn't supported in your current version — use natural language as the fallback

**Common slash commands reference:**

| Command | What it does |
|---------|-------------|
| `/explain` | Explains selected code in plain language |
| `/fix` | Identifies and fixes issues in selected code |
| `/tests` | Generates unit tests for selected code |
| `/doc` | Generates documentation or docstrings |
| `/new` | Scaffolds a new file or project structure |

---

## 0:15 – 0:30 | Live Demo: `/explain` & `/fix`

### `/explain` Demo
- Open `copilot_demo.py`
- Select the `parse_log_entry` function (the intentionally complex one)
- Open Chat panel, type `/explain`
- Walk through Copilot's plain language breakdown
- **Key message:** This is immediately useful for onboarding to an unfamiliar codebase — no need to trace logic manually

- Second example: select the regex pattern line only
- Type `/explain` again — show that it scopes to the selection
- **Key message:** The smaller and more focused your selection, the more precise the explanation

### `/fix` Demo
- Select the `calculate_discount` function (contains intentional bugs)
- Open Chat panel or Inline Chat, type `/fix`
- Show the proposed fix as a diff
- Point out that Copilot identifies *what* is wrong as well as *how* to fix it
- **Key message:** `/fix` is not just autocorrect — it reasons about the problem before proposing a solution
- Optionally run a second `/fix` on the `connect_to_database` function (missing error handling) to show it works on structural issues, not just syntax errors

---

## 0:30 – 0:42 | Live Demo: `/tests`

### `/tests` Demo
- Select the `calculate_percentage_change` function
- Open Chat panel, type `/tests`
- Walk through the generated test cases — happy path, edge cases, type handling
- **Key message:** Copilot scaffolds a starting point, not a finished test suite — always review for coverage gaps

- Show how to guide the output with combined natural language:
  - `/tests using pytest, include edge cases for zero and negative values`
  - Contrast with the plain `/tests` output to show the difference specificity makes
- **Key message:** Slash commands and natural language work best together — the slash command sets the intent, the natural language shapes the output

### What to look for when reviewing generated tests:
- Are the assertions meaningful or just checking that the function runs?
- Are edge cases (zero, None, empty string, negative numbers) covered?
- Does the test use the correct testing framework for your project?
- Would this test actually catch a bug if the logic changed?

---

## 0:42 – 0:52 | Structured Prompting Tips

**Combining slash commands with natural language:**
- Plain slash command: `/tests` → functional but generic
- Structured prompt: `/tests using pytest, cover edge cases for empty input and negative values` → targeted and immediately more useful
- The pattern is: **slash command + context + constraints**
- Works the same way for `/fix`: `/fix and explain why each change was made`

**Building richer prompts — the three-part structure:**

| Part | Purpose | Example |
|------|---------|---------|
| **Intent** | What you want Copilot to do | `/explain` |
| **Scope** | What it should focus on | `focusing on the error handling logic` |
| **Constraint** | How you want the output shaped | `in plain language suitable for a non-developer` |

**Full example:**
> `/explain focusing on the error handling logic in plain language suitable for a non-developer`

**When plain language beats a slash command:**
- For open-ended questions: *"What are the tradeoffs of this approach?"* — no slash command for that
- For multi-step reasoning: *"Review this function and suggest how it could be refactored for readability"*
- Rule of thumb: slash commands for well-defined tasks, natural language for exploratory ones

---

## 0:52 – 0:57 | Gotchas & Guardrails

**Version variability:**
- Always type `/` to check available commands before presenting or relying on a specific one
- If a command disappears after a Copilot update, natural language fallbacks always work
- Document which commands your team uses so there's a shared reference point

**Over-trusting generated tests:**
- `/tests` generates plausible tests, not necessarily correct or complete ones
- Generated tests can pass while still missing the actual failure mode you care about
- Treat generated tests as a first draft — review every assertion before committing

**When `/fix` misses the point:**
- `/fix` is good at surface-level bugs but can miss architectural or design problems
- If the fix looks right but something still feels off, ask a follow-up in natural language: *"Is there a deeper structural issue here?"*
- Never accept a `/fix` suggestion without understanding what it changed and why

**Premium request awareness:**
- Slash commands using advanced models still draw from your monthly premium quota
- For routine `/explain` tasks on simple code, consider switching to a lighter model to preserve quota for heavier work

---

## 0:57 – 1:00 | Q&A & Wrap-up

**Likely questions to prep for:**
- *"Can I create my own slash commands?"* — Not natively, but custom agent instructions (Session 6) achieve a similar outcome for project-specific tasks
- *"Does `/tests` know which testing framework we use?"* — Only if it's inferable from open files or context; guiding it with natural language is more reliable
- *"Can I use slash commands in Inline Chat?"* — Yes, `Ctrl+I` then `/` gives you the same options scoped to your selection

**Closing message:**
- Slash commands are the bridge between conversational Copilot and precise, repeatable workflows
- The real power is combining them with natural language to shape both intent and output
- Next session: Git Workflows — commit messages, PR descriptions, and diff reviews with AZDO in mind

---

## Out of Scope — What's Not Covered Today

| Topic | Brief Description |
|-------|------------------|
| **Git workflows** | Commit messages, PRs, diff reviews — covered in Session 4 |
| **Test generation deep dive** | Full test suite strategies and framework configuration — covered in Session 5 |
| **Custom agents & agent instructions** | Configuring Copilot behavior project-wide — covered in Session 6 |
| **MCP server integrations** | Extending Copilot with external tools — covered in Session 7 |

---

*Session 3 of 7 | Prerequisite: Sessions 1 & 2 — Chat Panel Fundamentals, Inline Suggestions & Editor Flow*
*Last updated: April 2026 | Based on GitHub Copilot for VS Code current release*
