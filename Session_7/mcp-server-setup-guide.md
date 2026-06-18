# MCP Server Setup Guide
# GitHub Copilot Session 7 — Connecting MCP Servers
# Demo Setup Guide
#
# -----------------------------------------------------------------------
# PRESENTER NOTE ON ACCURACY
# MCP support in VS Code and the Azure DevOps MCP server are both evolving
# quickly. The configuration below reflects documentation current as of
# June 2026. Before presenting, verify against:
#   - https://code.visualstudio.com/docs/agent-customization/mcp-servers
#   - https://github.com/microsoft/azure-devops-mcp
# -----------------------------------------------------------------------


## SECTION 1: Microsoft Learn MCP Server (Warm-Up Demo)

**Why this one first:** No authentication required, read-only by nature,
nothing to misconfigure that would cause a visible failure in front of
the audience.

### Setup

Create or open `.vscode/mcp.json` in your demo workspace and add:

```json
{
  "servers": {
    "microsoft-learn": {
      "type": "http",
      "url": "https://learn.microsoft.com/api/mcp"
    }
  }
}
```

Save the file. VS Code will show a "Start" button above the server entry —
click it to start the server.

### Demo Prompts

Switch Copilot Chat to **Agent** mode, then try:

- "How do I create a Microsoft Foundry instance using the Azure CLI?"
- "What's the current recommended way to authenticate to Azure DevOps from a script?"

Point out the confirmation dialog that appears before Copilot calls the
`microsoft_docs_search` tool — this is the same confirmation pattern you'll
see with every MCP server, including Azure DevOps next.

---

## SECTION 2: Azure DevOps MCP Server (Main Demo)

### Option A — Remote Server (Recommended Default)

This is Microsoft's recommended starting point: no local installation,
no Node.js requirement. Currently in public preview.

**Setup:**

Add to `.vscode/mcp.json`:

```json
{
  "servers": {
    "ado-remote-mcp": {
      "url": "https://mcp.dev.azure.com/{organization}",
      "type": "http",
      "headers": {
        "X-MCP-Readonly": "true"
      }
    }
  },
  "inputs": []
}
```

Replace `{organization}` with your Azure DevOps organization name.

**The `X-MCP-Readonly: true` header is the safety switch for this demo** —
it restricts the server to read-only operations regardless of what your
account is permitted to do. Do not remove this header for a live audience
demo unless you specifically intend to show write operations and have
a test project set up for it.

**Optional — scope to fewer tools** (recommended if you want a cleaner
tool list to show the audience):

```json
{
  "servers": {
    "ado-remote-mcp": {
      "url": "https://mcp.dev.azure.com/{organization}",
      "type": "http",
      "headers": {
        "X-MCP-Toolsets": "core,work,repos",
        "X-MCP-Readonly": "true"
      }
    }
  },
  "inputs": []
}
```

**First connection:**
1. Save the file, click "Start" on the server entry
2. Open Copilot Chat, switch to Agent mode
3. You'll be prompted to authenticate via Microsoft Entra ID — this opens
   a browser window; sign in with the account that has access to your
   Azure DevOps organization
4. Once authenticated, click the tools icon in the Chat input to confirm
   the Azure DevOps tools are listed

### Option B — Local Server (Alternative)

Use this if your organization's network blocks the remote preview endpoint,
or if you specifically need local stdio behavior. Requires Node.js 20+.

**Setup:**

```json
{
  "inputs": [
    {
      "id": "ado_org",
      "type": "promptString",
      "description": "Azure DevOps organization name (e.g. 'contoso')"
    }
  ],
  "servers": {
    "ado": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@azure-devops/mcp", "${input:ado_org}"]
    }
  }
}
```

This defaults to browser-based Microsoft account sign-in. To use an
existing Azure CLI session instead, add `"--authentication", "azcli"`
to the args array (requires Azure CLI installed and signed in beforehand).

### Demo Prompts (either option)

- "List my Azure DevOps projects"
- "Show me work items in the current iteration for [your test team]"
- "Summarize the open pull requests in [test repo]"

**Do not run write-style prompts** (creating or updating work items) during
the live demo unless you have removed the read-only header AND are pointed
at a test/sandbox project. Narrate that these capabilities exist rather
than demonstrating them live, to keep the session safely read-only throughout.

---

## Quick Troubleshooting Reference

| Symptom | Likely Cause |
|---------|-------------|
| No MCP tools appear at all in Agent mode | Org's "MCP servers in Copilot" policy is disabled — check with your Copilot admin |
| Server fails to start | Check `.vscode/mcp.json` for valid JSON; confirm root key is `"servers"` not `"mcpServers"` |
| Authentication window never appears | Check corporate proxy/SSL inspection settings; try on a different network if testing |
| Tools listed but every call fails | Confirm you're in Agent mode — MCP tools do not work in Ask or Plan mode |
| Suddenly asked to re-confirm tools you'd already allowed | Expected behavior — VS Code resets permissions when a server's tool list changes |
