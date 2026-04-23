# GitHub Copilot in VS Code — Lunch & Learn
**Session 2: Inline Suggestions & Editor Flow | Speaker Notes | 60 Minutes**

---

## 0:00 – 0:05 | Welcome & Session 1 Recap

**What to say:**
- Welcome back — today we move from the Chat panel into the editor itself
- Quick Session 1 recap: Chat panel, Ask/Plan/Agent modes, model selection, natural language file references
- Today's focus is the inline experience — Copilot working alongside you as you type, without switching context to the Chat panel
- Same rule applies: **always review output before accepting**

---

## 0:05 – 0:15 | Inline Suggestions Overview

**What ghost text is:**
- As you type, Copilot predicts what comes next and displays it as greyed-out ghost text directly in the editor
- It is not a search result — it is a generated prediction based on your current file, open tabs, and typing context
- It appears automatically; no prompt required

**How it differs from Chat:**
- Chat is conversational and deliberate — you ask, it responds
- Inline is ambient and continuous — it watches and suggests as you work
- Both complement each other; they are not competing features

**Key controls:**
| Action | Shortcut |
|--------|----------|
| Accept suggestion | `Tab` |
| Dismiss suggestion | `Esc` |
| Cycle to next suggestion | `Alt+]` |
| Cycle to previous suggestion | `Alt+[` |
| Accept word by word | `Ctrl+Right Arrow` |

---

## 0:15 – 0:30 | Live Demo: Ghost Text & Next Edit Suggestions

### Ghost Text Demo
- Open a file with a function or class already defined
- Start typing a new function name or a comment describing intent — let ghost text appear
- Show `Tab` to accept, `Esc` to dismiss, `Alt+]` to cycle alternatives
- **Tip:** Writing a descriptive comment on the line above is one of the most reliable ways to guide ghost text toward useful output

**Example prompt pattern to demonstrate:**
```
# Calculate the percentage change between two values and return rounded to 2 decimal places
```
Let Copilot complete the function from the comment alone.

### Next Edit Suggestions
- Next Edit Suggestions (NES) go beyond completing the current line — Copilot predicts your *next logical change* elsewhere in the file
- Example: rename a variable in one place and Copilot will suggest updating it in related locations
- Accept with `Tab`, navigate suggested edits with `Tab` to move between them
- **Key message:** This is Copilot anticipating intent, not just completing syntax — it rewards attendees who have started thinking in terms of what they want to accomplish rather than what they want to type

---

## 0:30 – 0:42 | Live Demo: Inline Chat

**What Inline Chat is:**
- A focused chat prompt that opens directly in the editor at your cursor position — `Ctrl+I`
- Changes are proposed as a diff in place, not in a separate panel
- Keeps you in the flow of coding without switching context

**Demo flow:**
- Select a block of code
- Press `Ctrl+I` and type: *"Add error handling to this block"*
- Show the proposed diff — accept, discard, or iterate
- Show a second example without a selection: *"Add a docstring to this function"* with cursor inside the function

**Inline Chat vs Chat Panel — when to use which:**

| Use Inline Chat when... | Use Chat Panel when... |
|------------------------|----------------------|
| You have a specific, targeted edit in mind | You want to explore, ask questions, or plan |
| You want to stay in the editor flow | You need multi-file context or a longer conversation |
| The change is localized to a few lines | The task spans multiple files or requires Agent mode |

---

## 0:42 – 0:52 | Practical Tips

**Comment-first prompting:**
- Writing a comment describing intent before the code is one of the most effective ways to guide inline suggestions
- Be specific: *"# Parse ISO 8601 date string and return as UTC datetime object"* outperforms *"# parse date"*
- Works well for functions, classes, and configuration blocks

**Keep context focused:**
- Copilot uses open editor tabs as implicit context — close tabs you don't need
- The active file and current selection carry the most weight
- For large files, position your cursor near the relevant code before triggering suggestions

**When to use inline vs Chat panel:**
- Inline is best for fast, surgical edits where you know what you want
- Chat panel is better when you need to think through an approach first — use Plan mode, then switch to inline for execution
- There is no wrong answer — the two modes are designed to work together

---

## 0:52 – 0:57 | Gotchas & Guardrails

**Over-reliance on ghost text:**
- It is easy to fall into a pattern of accepting suggestions without reading them — especially under time pressure
- Ghost text can introduce subtle bugs: wrong variable names, incorrect logic, outdated patterns
- Discipline: read every suggestion before pressing `Tab`, even for short completions

**Reviewing before accepting:**
- For multi-line completions, scroll through the full suggestion before accepting
- Use `Ctrl+Right Arrow` to accept word by word when you want partial acceptance
- If a suggestion looks almost right but not quite, accept it and then correct — that is often faster than dismissing and reprompting

**Performance in large files:**
- In very large files Copilot suggestions may be slower or less accurate due to context window limits
- If suggestions are consistently poor, try splitting the file or narrowing your open tabs
- Inline Chat tends to perform better than ghost text in large files because it uses your explicit selection as focused context

---

## 0:57 – 1:00 | Q&A & Wrap-up

**Likely questions to prep for:**
- *"Can I turn off ghost text but keep Chat?"* — Yes, inline suggestions can be disabled independently in VS Code Copilot settings without affecting Chat
- *"Does Copilot learn from what I accept?"* — At the individual level, no persistent learning occurs per session; accepted suggestions do not fine-tune the model in real time
- *"Is Inline Chat the same as Edit mode in Chat?"* — They serve similar purposes but Inline Chat is scoped to your cursor/selection in the editor, while Chat panel Edit mode can target files more broadly

**Closing message:**
- Today's session gives you two new tools: ghost text for ambient assistance and Inline Chat for focused in-editor edits
- Combined with the Chat panel from Session 1, you now have the full core Copilot interaction model
- Next session: Slash Commands & Structured Prompting — taking precision to the next level

---

## Out of Scope — What's Not Covered Today

| Topic | Brief Description |
|-------|------------------|
| **Slash commands** | `/explain`, `/fix`, `/tests` — covered in Session 3 |
| **Git workflows** | Commit messages, PRs, diff reviews — covered in Session 4 |
| **Test generation** | Scaffolding unit tests — covered in Session 5 |
| **Custom agents & agent instructions** | Configuring how Agent mode behaves — covered in Session 6 |
| **MCP server integrations** | Extending Copilot with external tools — covered in Session 7 |

---

*Session 2 of 7 | Prerequisite: Session 1 — Chat Panel Fundamentals*
*Last updated: April 2026 | Based on GitHub Copilot for VS Code current release*
