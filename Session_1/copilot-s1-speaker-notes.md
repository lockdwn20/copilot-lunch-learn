# GitHub Copilot in VS Code — Lunch & Learn
**Speaker Notes | 60 Minutes**

---

## 0:00 – 0:05 | Welcome & Housekeeping

**What to say:**
- Welcome everyone, today's goal is practical familiarity — not mastery
- Copilot is an AI pair programmer built into VS Code; it assists, it does not replace judgment
- We'll focus entirely on the Chat panel — no terminal required
- Key point upfront: **always review Copilot's output before using it**

**What it's not:**
- Not a search engine
- Not always right — it hallucinates, it makes assumptions
- Not a replacement for understanding your code

---

## 0:05 – 0:15 | Setup & Interface Orientation

**Extension & Auth:**
- Install "GitHub Copilot" from the VS Code Marketplace
- Sign in with your GitHub account (SSO if required by your org)
- Confirm the Copilot status indicator is active in the VS Code status bar (bottom)

**Finding the Chat Panel:**
- Open via `Ctrl+Alt+I` (Windows) / `Ctrl+Cmd+I` (Mac) or from the VS Code title bar Chat menu
- Chat panel lives in the Secondary Side Bar by default

**AZDO & Local Repos — Concept Only:**
- Most of your repos live in Azure DevOps — that's your **remote**
- To use Copilot effectively, you need a **local clone** — a copy on your machine that VS Code can read
- Copilot works against what's local; it can't reach into AZDO directly
- Good news: once signed in with your Microsoft account, VS Code can use AZDO remote indexes automatically to help Copilot understand your codebase faster
- Simple mental model: *AZDO is the source of truth, your local clone is your workspace*

---

## 0:15 – 0:25 | Model Selection & Chat Modes

**Switching Models:**
- Click the model picker in the Chat panel header
- Available models vary by subscription tier (Free / Pro / Business / Enterprise)
- Common options: GPT-4o, Claude Sonnet, o3-mini — each has different strengths and cost implications (more on this in Gotchas)

**Chat Modes — Ask vs Plan vs Agent:**

| Mode | What it does | When to use it |
|------|-------------|----------------|
| **Ask** | Answers questions, explains code, no changes made | Understanding, Q&A, exploration |
| **Plan** | Breaks a task into steps, asks clarifying questions, proposes an approach before acting | Before making changes to unfamiliar code |
| **Agent** | Autonomously executes multi-step tasks, edits files, runs commands | When you're confident in the goal and want Copilot to execute |

**Key message:** Start with Ask to understand, use Plan before you commit, use Agent when you're ready to execute.

---

## 0:25 – 0:40 | Live Demo: Chat Panel in Action

### Ask Mode
- Open a file in your repo
- Ask: *"Explain what this file does and what its dependencies are"*
- Show how Copilot uses the active file as implicit context
- Ask a follow-up question to show conversational flow

### Plan Mode
- Give a task: *"I need to add input validation to this function — walk me through how you'd approach it"*
- Show how Plan proposes steps and asks clarifying questions before touching anything
- Emphasize: this is the safe, reviewable path before committing to changes

### Agent Mode (keep controlled)
- Brief example: *"Add error handling to this function"*
- Show that Agent will propose file edits directly
- **Tip:** Rehearse this beforehand — Agent can be unpredictable in live demos. Consider showing a screenshot or recording if the demo environment is sensitive.

---

## 0:40 – 0:50 | Practical Tips

**Referencing Files — What Actually Works:**
- Natural language is the most reliable approach: *"Please review the filename.txt in the docs/ directory and summarize its contents"*
- `#file` syntax does exist (opens a file picker) but behavior can vary by version
- You can also **drag and drop** a file from the Explorer panel directly onto the Chat input — clean and visual
- Give Copilot enough context: file name, path, and what you want it to do

**Writing Good Prompts:**
- Be specific — vague prompts get vague answers
- Include intent: *"...so that I can understand how the authentication flow works"*
- Treat it like a conversation — follow up, correct it, ask it to try again
- Shorter focused prompts often outperform long complex ones

**Key reminder:** Copilot Chat is a conversation, not a command line. Plain, descriptive language works best.

---

## 0:50 – 0:57 | Gotchas & Guardrails

**Standard vs Premium Requests:**
- **Inline suggestions and basic Ask chat** = included in all plans, no quota
- **Premium models** (o3, Claude Sonnet, etc.) = draw from a **monthly allowance** based on your subscription tier
- Switching to a premium model in the model picker consumes premium quota — easy to burn through if you forget to switch back
- Check your usage in GitHub settings if you're unexpectedly hitting limits

**Hallucinations:**
- Copilot will confidently produce incorrect code, wrong function names, or nonexistent APIs
- Always verify output — especially for anything security-relevant
- The more specific your prompt and context, the less likely it hallucinates

**IP & Licensing:**
- Copilot is trained on public code — generated output may resemble open source with existing licenses
- Org policy may restrict what you can feed into Copilot (sensitive data, proprietary algorithms)
- When in doubt, check with your security or legal team before using Copilot on sensitive repos

**Privacy Basics:**
- Code snippets and prompts are sent to GitHub's servers for processing
- GitHub offers settings to opt out of code snippet telemetry — worth reviewing for sensitive work environments

---

## 0:57 – 1:00 | Q&A & Wrap-up

**Likely questions to prep for:**
- *"What tier do we have?"* — Know your org's subscription level before the session
- *"Can Copilot see our entire codebase?"* — Only what's locally cloned and indexed; with AZDO sign-in it can build a remote index
- *"Is it safe to use on client repos?"* — Defer to org/security policy, raise the telemetry opt-out option

**Closing message:**
- Best way to learn is to use it — start with Ask mode on code you already understand
- The tool gets better the more specific and conversational you are with it
- Questions welcome after the session

---

## Out of Scope — What's Not Covered Today

This session is intentionally focused on Chat panel fundamentals. The following topics exist within Copilot but are beyond the scope of this introduction:

| Topic | Brief Description |
|-------|------------------|
| **Inline ghost text suggestions** | AI completions that appear as you type in the editor — a separate interaction model from Chat |
| **Slash commands** | Shorthand prompts like `/explain`, `/fix`, `/tests` — powerful but version-dependent |
| **Custom agents & agent instructions** | Defining how Agent mode behaves, which tools it can use, and project-specific personas |
| **MCP server integrations** | Extending Copilot with external tools and data sources via Model Context Protocol |
| **Git workflows** | Commit message generation, branch management, pull requests, and diff reviews — broad enough to warrant its own dedicated Lunch & Learn |
| **Test generation workflows** | Using Copilot to scaffold and generate unit tests for existing functions |
| **Full project build from prompt** | Using Agent or Plan mode to generate an entire project structure from scratch |

**Suggested framing for attendees:** *"Today is your on-ramp. Each of these topics is a natural next step once you're comfortable with the Chat panel basics."*

---

*Last updated: March 2026 | Based on GitHub Copilot for VS Code current release*
