# GitHub Copilot in VS Code — Lunch & Learn
**Session 7: MCP Integrations & Full Project Builds | Speaker Notes | 80 Minutes (Capstone)**

---

## ⚠️ PRESENTER CHECKLIST — Complete Before the Session

This session has more live-environment dependencies than any prior one. Work through this list at least a day ahead, not the morning of:

1. **Org policy check (critical):** If your organization has Copilot Business or Enterprise, the "MCP servers in Copilot" policy is **disabled by default**. Confirm with your Copilot admin that it's enabled — otherwise MCP tools will not appear at all, regardless of how correctly you configure things.
2. **VS Code version:** Confirm you're on a recent release (1.99 or later; ideally latest stable). MCP support has matured quickly and older versions may behave differently than these notes describe.
3. **Full dry run:** Configure and test the Azure DevOps MCP connection end-to-end at least once, including the Microsoft Entra ID browser sign-in, on the same machine and network you'll present from. Corporate proxies and SSL inspection can silently block the connection.
4. **Demo project selection:** Use a non-production or test Azure DevOps project for the live demo if one is available. Even with read-only mode configured, it's good practice not to point a live demo at real client/case data.
5. **Remote vs local server decision:** These notes default to the **remote** Azure DevOps MCP server (Microsoft's recommended path, no Node.js required, currently in public preview). The local alternative is documented in the setup guide if you'd rather avoid a preview feature — see `mcp-server-setup-guide.md`.

---

## 0:00 – 0:05 | Welcome & Session 6 Recap

**What to say:**
- Welcome back — this is it, the final session in the series
- Quick Session 6 recap: agent instructions in `.github/copilot-instructions.md` for project-wide behavior, task-specific personas for documentation and code review
- Today we tie everything together: connecting Copilot to live external systems via MCP, and watching Agent mode build something from a high-level goal
- This is the most "hands off the wheel" session yet — guardrails matter more here than anywhere else in the series

---

## 0:05 – 0:15 | What MCP Is & Why It Matters

**The progression so far:**
- Sessions 1–5: Copilot worked with what was visible — open files, selections, your prompts
- Session 6: Copilot worked with standing instructions you gave it — project-wide rules, personas
- Today: Copilot reaches **outward** — querying live systems, fetching real data, taking actions in tools you already use

**What MCP is:**
- Model Context Protocol — an open standard for connecting AI models to external tools and data sources
- An MCP server is a small program or hosted endpoint that exposes a set of "tools" Copilot can call mid-conversation
- Examples of what tools can do: search documentation, query a database, fetch a web page, read and create Azure DevOps work items

**Where configuration lives:**
- `.vscode/mcp.json` in your workspace root for project-specific servers, or your user profile for personal ones
- The root key is `"servers"` — a common mistake is copying a config from another tool (like Claude Desktop) which uses `"mcpServers"` instead
- VS Code provides a Start button once configured — servers don't run until you explicitly start them

**Critical requirement — Agent mode only:**
- MCP tools are only available in **Agent mode** — they do not appear in Ask or Plan mode
- This is intentional — MCP tools can take real actions, so VS Code scopes them to the mode designed for autonomous execution

---

## 0:15 – 0:32 | Live Demo: Connecting MCP Servers

### Warm-Up: Microsoft Learn MCP Server (zero risk)

**Why start here:** No authentication, no write access, nothing that can go wrong in front of an audience — a safe way to show the mechanic before raising the stakes.

**Demo flow:**
1. Show the configuration from `mcp-server-setup-guide.md` (Section 1)
2. Start the server, switch Chat to Agent mode
3. Ask a real question: *"How do I create a Microsoft Foundry instance using the Azure CLI?"*
4. Point out the tool confirmation dialog before Copilot calls `microsoft_docs_search`
5. Show the response — note that it's pulling current documentation, not relying on training data that might be stale

### Main Event: Azure DevOps MCP Server (read-only mode)

**Demo flow:**
1. Show the remote server configuration from `mcp-server-setup-guide.md` (Section 2) — point out how short it is compared to most setups
2. Walk through the Microsoft Entra ID browser sign-in (this should already be tested from your dry run)
3. Once connected, click the tools icon to show the available Azure DevOps tools
4. Run a read-only prompt: *"List my Azure DevOps projects"*
5. Run a second prompt: *"Show me work items in the current iteration for [test project/team]"*
6. **Key message:** Point out explicitly that read-only mode is active — even though Copilot could create or update work items with full access, it cannot here. This is a deliberate safety choice for live demos, not a default behavior.

---

## 0:32 – 0:55 | Live Demo: Full Project Build

**Setup:** Open `full-project-build-guide.md` for the exact prompts to use.

**The scenario:** Build a small Python CLI tool that reads a CSV of security alerts and prints a summary report grouped by severity — a project type your audience will immediately recognize.

### Step 1 — Plan Mode: Propose the Approach
1. Open Chat panel, switch to **Plan** mode
2. Use the high-level goal prompt from the guide
3. Let Plan mode propose a file structure and approach — it should ask clarifying questions
4. Answer them live, or use the suggested answers in the guide if you want to keep pace
5. **Key message:** This is the checkpoint — nothing has been written yet. If the plan looks wrong, this is where you redirect it, before any code exists.

### Step 2 — Handoff to Agent Mode: Execute
1. Once the plan looks reasonable, switch to **Agent** mode
2. Ask Copilot to execute the approved plan
3. Watch it create files — narrate what's happening as each file appears
4. Review the proposed diffs/new files before accepting each one
5. **Key message:** Agent mode is doing in minutes what would otherwise be 30+ minutes of scaffolding — but every file it creates still deserves the same review discipline from Sessions 4 and 5

### Step 3 — Verify the Output
1. Open the generated CLI tool
2. Run it against the sample CSV from the guide
3. Confirm the output matches expectations
4. **Optional, if time allows:** Ask Copilot to generate tests for the new tool using `/tests` from Session 3 — a nice full-circle moment for the series

---

## 0:55 – 1:05 | Guardrails at Scale

**Tool confirmation dialogs:**
- Every MCP tool call triggers a confirmation prompt before it runs
- Options typically include: confirm once, confirm for the current session, or always allow — choose deliberately, not by habit
- "Always allow" should be reserved for tools you've used repeatedly and trust completely

**Why read-only scoping matters:**
- Many MCP servers (including Azure DevOps) support a read-only restriction
- For exploratory work, demos, or anyone new to a server, read-only removes the risk of an unintended write
- Promote write access only once you're confident in how the tool behaves

**A built-in safety behavior worth knowing:**
- If an MCP server's tool list changes, VS Code resets any previously granted permissions and re-prompts for confirmation
- This protects against a scenario where a server is updated to do something different than what you originally approved — worth mentioning to a security-minded audience specifically

**Reviewing autonomous changes:**
- Treat every file Agent mode creates or modifies with the same scrutiny as a pull request from a teammate
- Multi-file changes deserve a full read-through before committing — don't just skim the file names
- If Agent mode's output touches something sensitive (credentials, infrastructure configs, production paths), slow down and review line by line

---

## 1:05 – 1:12 | Gotchas & Guardrails

**Org policy blocks (the one most likely to bite you):**
- Covered in the presenter checklist — if MCP tools don't appear at all, this is the first thing to check, not your `mcp.json` syntax

**Preview feature caveats:**
- The remote Azure DevOps MCP server is in public preview — behavior, URLs, or configuration options may change with little notice
- If something that worked last week stops working, check the official Azure DevOps MCP server documentation before assuming you misconfigured something

**Tool sprawl:**
- Azure DevOps exposes a large number of tools; loading all of them can hit client limits or make it harder for Copilot to pick the right one
- Use Domains (remote server) or Toolsets (local server) to scope to only what you need — for most CSIRT-adjacent work, this likely means work items and repositories, not the full surface area

**Authentication and network issues:**
- Corporate proxies and SSL inspection can prevent an MCP server from starting or authenticating
- If a server fails to start, check network/proxy settings before assuming the configuration is wrong

**The `"servers"` vs `"mcpServers"` mistake:**
- Configuration examples copied from other AI tools often use `"mcpServers"` as the root key — VS Code uses `"servers"`
- A single wrong key name will cause the entire file to fail silently

---

## 1:12 – 1:20 | Q&A & Series Wrap-Up

**Likely questions to prep for:**
- *"Can Copilot create work items automatically without me asking each time?"* — Only with write access granted and "always allow" set — not recommended as a default behavior
- *"Does this work the same way in Visual Studio, not just VS Code?"* — Yes, Visual Studio has equivalent MCP support, though the exact menu locations differ
- *"What happens if the MCP server goes down mid-conversation?"* — Copilot will report the tool call failed; it does not silently fall back to guessing

**Closing message — Series Wrap-Up:**
- Seven sessions ago we started with the Chat panel and model selection — today Copilot reaches into live systems and scaffolds entire projects from a single prompt
- The throughline across all seven sessions has been the same: Copilot accelerates the first draft, but review discipline is what makes the output trustworthy
- Thank attendees for sticking with the series — consider asking for feedback on which sessions were most useful for future iterations

---

## Beyond This Series — Continued Learning

These are natural next steps for anyone who wants to go further, outside the scope of this 7-session arc:

| Topic | Brief Description |
|-------|------------------|
| **GitHub Copilot CLI** | Using Copilot from the terminal for scripting and automation workflows |
| **Custom chat participant extensions** | Building your own `@agent` extensions via VS Code extension development |
| **Enterprise policy administration** | Managing org-wide Copilot policies, including the MCP access policy covered today |
| **Additional MCP servers** | Database connectors, browser automation (Playwright), and other servers in the MCP registry |

---

*Session 7 of 7 (Final/Capstone) | Prerequisite: Sessions 1–6*
*Last updated: June 2026 | Based on GitHub Copilot for VS Code current release*
