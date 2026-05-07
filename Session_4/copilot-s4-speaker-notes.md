# GitHub Copilot in VS Code — Lunch & Learn
**Session 4: Git Workflows with Copilot | Speaker Notes | 60 Minutes**

---

## 0:00 – 0:05 | Welcome & Session 3 Recap

**What to say:**
- Welcome back — today we move outside the editor and into source control
- Quick Session 3 recap: slash commands (`/explain`, `/fix`, `/tests`), combining slash commands with natural language for structured prompts
- Today's focus: using Copilot to reduce the friction of everyday Git tasks — commit messages, diff reviews, and pull request descriptions
- This session is especially relevant for anyone who finds Git intimidating or time-consuming
- Same rule applies: **always review output before committing or submitting**

---

## 0:05 – 0:15 | Git in VS Code Overview

**Source Control Panel:**
- Open with `Ctrl+Shift+G` or click the branch icon in the Activity Bar
- Shows staged changes, unstaged changes, and untracked files
- All the Git operations most people need are available here — no terminal required

**Quick concept refresh — local vs AZDO remote:**
- Your local clone is where you make changes
- AZDO is the remote — where your team's shared code lives
- The workflow is: make changes locally → stage → commit → push to AZDO → open a PR

**Staging changes in VS Code:**
- Hover over a changed file in the Source Control panel → click the `+` icon to stage
- Or stage all changes at once using the `+` next to the Changes header
- Staged changes are what Copilot uses when generating commit messages

**Key message:** Everything we do today happens in the Source Control panel and Chat — no terminal commands needed.

---

## 0:15 – 0:28 | Live Demo: Commit Message Generation

**Setup:** Have `copilot_demo_s4.py` open with a set of staged changes ready (see demo setup guide).

**How Copilot commit message generation works:**
- Once changes are staged, a small sparkle ✨ icon appears in the commit message input box at the top of the Source Control panel
- Click it — Copilot reads your staged diff and generates a commit message
- The message follows conventional commit format by default (e.g. `fix:`, `feat:`, `refactor:`)

**Demo flow:**
1. Show the staged changes in the Source Control panel
2. Click the sparkle icon — let Copilot generate the message
3. Read it aloud and evaluate it with the audience — is it accurate? Is it specific enough?
4. Edit it to demonstrate that generated messages are a starting point, not final output
5. **Do not actually commit** — just show the generation and editing step

**What makes a good commit message:**
- Describes *what* changed and *why*, not just *how*
- Short subject line (under 72 characters) + optional body for context
- Specific enough that someone reading the log 6 months later understands it

**Good vs weak commit message examples:**

| Weak | Strong |
|------|--------|
| `fix bug` | `fix: guard against zero division in calculate_percentage_change` |
| `updates` | `refactor: extract config validation into separate helper function` |
| `wip` | `feat: add overdue item filtering with sort by due date` |

**Key message:** Copilot gets you 80% of the way there — your job is to review and tighten it.

---

## 0:28 – 0:40 | Live Demo: Diff Review & Change Summarization

**Why this matters:**
- Before pushing or opening a PR, reviewing your own diff is good practice
- Copilot Chat can summarize what changed across multiple files in plain language — useful for self-review and for explaining changes to non-technical stakeholders

**Demo flow — using Chat to review a diff:**
1. In the Source Control panel, click on a changed file to open the diff view
2. Select all the changed lines (the green/red highlighted sections)
3. Open Chat panel and type:
   > *"Summarize what changed in this diff and explain the intent behind each change"*
4. Show the plain language summary — point out how useful this is for writing PR descriptions

**Second demo — multi-file summary:**
1. Open Chat panel (no selection needed)
2. Reference the changed files by name and path:
   > *"I have made changes to copilot_demo_s4.py in the src/ directory — can you summarize what was changed based on what you can see in the file?"*
3. Show how natural language file references (from Session 1) carry forward into Git workflows

**Key message:** Copilot Chat is not just for writing code — it can explain and document changes you have already made.

---

## 0:40 – 0:50 | Live Demo: PR Descriptions

**Context — AZDO PR workflow:**
- After pushing your branch to AZDO, you open a Pull Request in the AZDO portal
- PR descriptions are often written quickly and lack context — Copilot can help generate a thorough description before you open the PR
- Generate the description in VS Code Chat, then paste it into AZDO

**Demo flow:**
1. Open Chat panel
2. Use the structured prompt:
   > *"Write a pull request description for the changes I made in copilot_demo_s4.py. Include a summary of what changed, why it was changed, and any testing considerations."*
3. Walk through the generated description — sections typically include Summary, Changes Made, Testing Notes
4. Edit it to match your actual changes
5. Show where to paste it in AZDO (navigate to Repos → Pull Requests → New PR → Description field)

**PR description structure Copilot tends to generate:**
```
## Summary
Brief description of what this PR does and why.

## Changes Made
- Change 1 and its purpose
- Change 2 and its purpose

## Testing Considerations
- What was tested
- Edge cases covered
- Any known limitations
```

**Key message:** A good PR description saves your reviewers time and creates a record of intent — Copilot removes the excuse not to write one.

---

## 0:50 – 0:57 | Gotchas & Guardrails

**Vague commit messages:**
- Copilot sometimes generates messages that are accurate but too generic — e.g. `refactor: update function` tells you nothing useful
- Always ask: *"Would I understand this in 6 months without reading the code?"*
- If not, edit before committing — it takes 30 seconds and saves hours later

**Over-relying on generated PR descriptions:**
- Copilot writes based on what it can see in the file — it cannot know your business context, the ticket it relates to, or the risk level of the change
- Always add: AZDO work item / ticket reference, any deployment considerations, reviewer callouts
- Treat the generated description as a scaffold, not a finished document

**Branch hygiene:**
- Copilot cannot enforce branch naming conventions — that is a team agreement
- Short-lived feature branches with clear names keep PR reviews focused
- Consider including your AZDO work item number in the branch name: `feature/12345-add-discount-validation`

**Pushing vs PRs:**
- Copilot has no awareness of whether you have pushed yet — it works against local state
- Generate your commit message and PR description before pushing, while the changes are fresh in context

---

## 0:57 – 1:00 | Q&A & Wrap-up

**Likely questions to prep for:**
- *"Can Copilot create the PR in AZDO directly?"* — Not natively without an MCP integration (covered in Session 7); today we generate the description and paste it manually
- *"Does the sparkle icon always appear?"* — Only when changes are staged; if it's not showing, check that files are staged not just saved
- *"Can Copilot review someone else's PR?"* — Yes — paste the diff into Chat and ask it to review; useful for code review prep

**Closing message:**
- Git workflows are where consistent habits pay off — Copilot lowers the effort bar for commit messages and PR descriptions so there is less reason to skip them
- Next session: Test Generation Workflows — building on `/tests` from Session 3 into a full testing strategy

---

## Out of Scope — What's Not Covered Today

| Topic | Brief Description |
|-------|------------------|
| **Direct AZDO integration via MCP** | Automating PR creation, work item linking — covered in Session 7 |
| **Test generation workflows** | Full test suite strategies — covered in Session 5 |
| **Custom agents & agent instructions** | Project-wide Copilot configuration — covered in Session 6 |
| **Merge conflict resolution with Copilot** | Using Chat to reason through conflicts — adjacent topic, not in this series |

---

*Session 4 of 7 | Prerequisite: Sessions 1–3*
*Last updated: May 2026 | Based on GitHub Copilot for VS Code current release*
