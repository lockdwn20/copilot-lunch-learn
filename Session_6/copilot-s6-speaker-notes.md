# GitHub Copilot in VS Code — Lunch & Learn
**Session 6: Custom Agents & Agent Instructions | Speaker Notes | 60 Minutes**

---

## 0:00 – 0:05 | Welcome & Session 5 Recap

**What to say:**
- Welcome back — today marks a shift in how we think about Copilot
- So far we have been *using* Copilot — asking it questions, generating code, running slash commands
- Today we start *configuring* Copilot — telling it how to behave before we even open a prompt
- Quick Session 5 recap: test generation with `/tests`, iterative coverage through conversation, validating assertions, virtual environment and pytest setup
- Today's focus: agent instructions — a project-level configuration file that shapes every Copilot interaction in your repo

---

## 0:05 – 0:15 | Agent Instructions Overview

**What agent instructions are:**
- A plain text markdown file that tells Copilot how to behave in the context of your specific project
- It sets the rules once so you don't have to repeat them in every prompt
- Think of it as a standing brief you hand Copilot at the start of every conversation

**Where it lives:**
- File path: `.github/copilot-instructions.md` in the root of your repo
- Copilot reads it automatically — no configuration required beyond creating the file
- It is committed to your repo in AZDO, so every team member benefits from the same instructions

**What it can contain:**
- Coding standards and style conventions
- Preferred libraries and frameworks
- What to avoid (patterns, anti-patterns, specific packages)
- Project context (what the repo does, who uses it, what environment it runs in)
- Tone and output format preferences for documentation or comments

**What it cannot do:**
- Override Copilot's built-in safety guardrails
- Force specific model behavior — it influences, it does not command
- Guarantee consistent output — treat it as strong guidance, not deterministic control

**Key message:** A well-written instructions file means less prompt repetition and more consistent output across your whole team.

---

## 0:15 – 0:28 | Live Demo: Project-Wide Instructions

**Setup:** Open `copilot-instructions.md` from the demo files in VS Code. Walk through it section by section before showing the behavioral difference.

**Demo flow:**
1. Open `copilot-instructions.md` and read through it with the audience — point out the structure: project context, coding standards, conventions, what to avoid
2. Open `copilot_demo_s5.py` and ask Copilot in Chat (without the instructions file active):
   > *"Add a new function that reads a list of users from a JSON file"*
   - Note the output style — generic, no project context
3. Ensure `.github/copilot-instructions.md` is in place in the repo root
4. Ask the exact same prompt again
   - Point out differences: error handling style, naming conventions, docstring format, any library preferences reflected in the output
5. **Key message:** Same prompt, different context — the instructions file is doing the work silently in the background

**What to highlight in the instructions file:**
- The project context block — tells Copilot what kind of codebase this is
- The coding standards block — enforces consistency without repeating it in every prompt
- The "avoid" block — prevents Copilot from suggesting patterns your team has ruled out

---

## 0:28 – 0:40 | Live Demo: Task-Specific Personas

**What task-specific personas are:**
- Beyond project-wide instructions, you can invoke focused personas in Chat for specific tasks
- A persona is a set of instructions you give Copilot at the start of a Chat session to shape how it responds for that task
- Not a separate file — delivered as the opening message in a Chat conversation

**Demo 1 — Documentation Agent:**
1. Open `copilot_demo_s5.py`, select the `get_overdue_items` function
2. Open a new Chat panel conversation and start with the documentation persona prompt from `persona-prompts.md`
3. Follow with: *"Document this function"*
4. Show the output — structured, audience-aware, matches the persona's defined style

**Demo 2 — Code Review Agent:**
1. Select the `read_config_value` function
2. Open a new Chat panel conversation and start with the code review persona prompt
3. Follow with: *"Review this function"*
4. Show the output — critical, structured, flags specific concerns
5. Compare the two persona outputs side by side — **same function, very different lenses**

**Key message:** Personas let one tool serve multiple roles — you configure the lens, Copilot applies it consistently for that session.

---

## 0:40 – 0:50 | Team-Shared Instructions

**Committing to AZDO:**
- The `.github/copilot-instructions.md` file is just another file in your repo — commit it like anything else
- Once committed and pushed, every team member who clones or pulls the repo gets the same Copilot behavior automatically
- No individual VS Code configuration required

**Keeping instructions maintained:**
- Instructions should evolve with the project — treat them like documentation, not a set-and-forget config
- Review them when onboarding new frameworks, changing coding standards, or after major refactors
- Assign ownership — someone on the team should be responsible for keeping them current

**Consistency across contributors:**
- The biggest value of shared instructions is reducing the variance in Copilot output across team members
- A junior developer and a senior developer asking the same question get responses shaped by the same standards
- This is especially valuable for teams adopting Copilot at different paces

**Suggested workflow for introducing instructions to a team:**
1. Draft the initial file collaboratively — get input on standards from the team
2. Commit to a feature branch and open a PR for review (practice what you preach)
3. Iterate based on feedback — what did Copilot do differently? Was it helpful?
4. Treat updates to the instructions file like any other code change — reviewed, approved, merged

---

## 0:50 – 0:57 | Gotchas & Guardrails

**Instruction bloat:**
- Longer is not better — an instructions file with 50 rules dilutes the signal
- Copilot applies instructions with decreasing reliability as the file grows
- Aim for focused, high-value rules — 10 clear instructions outperform 40 vague ones

**Conflicting rules:**
- If your instructions file says "always use f-strings" and your prompt says "use .format()", Copilot has to make a judgment call
- Keep instructions non-contradictory and review them periodically for rules that have become outdated

**Over-constraining Copilot:**
- Too many restrictions can make Copilot less useful for exploratory tasks
- Consider scoping strict instructions to specific file types or directories if your repo has mixed contexts
- Leave room for Copilot to suggest — the goal is guidance, not a straitjacket

**Version behavior differences:**
- How Copilot interprets instructions can vary between model versions and Copilot updates
- If behavior changes after a Copilot update, check whether your instructions file still reads clearly
- Test the instructions file on a new prompt after any significant Copilot version change

**Persona prompts are session-scoped:**
- Persona prompts given at the start of a Chat session only apply to that session — they are not persistent
- If you close and reopen Chat, the persona is gone
- For persistent behavior, encode it in `copilot-instructions.md` instead

---

## 0:57 – 1:00 | Q&A & Wrap-up

**Likely questions to prep for:**
- *"Can we have multiple instructions files for different parts of the repo?"* — Currently one file per repo; scope specificity through clear language within the file rather than multiple files
- *"Can Copilot edit its own instructions file?"* — Yes, but treat any AI-generated changes to it with extra scrutiny — it is your governance document
- *"Do persona prompts work in Inline Chat too?"* — Less reliably; inline chat context is shorter and the persona may not carry through — Chat panel is more consistent for persona-driven tasks

**Closing message:**
- Today's session is the foundation for everything in Session 7 — MCP integrations and full project builds work best when Copilot already has strong project context via instructions
- If you do one thing after today: create a `.github/copilot-instructions.md` in your most active repo and commit it — even a basic version improves consistency immediately
- Final session next: MCP Integrations & Full Project Builds — the capstone

---

## Out of Scope — What's Not Covered Today

| Topic | Brief Description |
|-------|------------------|
| **VS Code workspace settings** | Per-user Copilot configuration separate from shared repo instructions |
| **Custom chat participants** | Building your own `@agent` extensions — requires VS Code extension development |
| **MCP server integrations** | Extending Copilot with external tools and data sources — covered in Session 7 |
| **Full project builds** | Autonomous multi-step Agent mode execution at scale — covered in Session 7 |

---

*Session 6 of 7 | Prerequisite: Sessions 1–5*
*Last updated: June 2026 | Based on GitHub Copilot for VS Code current release*
