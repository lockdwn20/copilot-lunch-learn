# Full Project Build Demo Guide
# GitHub Copilot Session 7 — Plan to Agent Handoff
# Demo Script
#
# SCENARIO: Build a small Python CLI tool that reads a CSV of security
# alerts and prints a summary report grouped by severity. 
----------------------


## Step 1 — Plan Mode: Propose the Approach

Open a new, empty folder in VS Code (or an empty subfolder in your demo
repo) so the audience sees this built from nothing. Switch Chat to
**Plan** mode and use this opening prompt:

> "I want to build a small Python CLI tool that reads a CSV file of
> security alerts and prints a summary report counting alerts by
> severity level (Critical, High, Medium, Low). Walk me through how
> you'd approach building this before writing any code."

**What should happen:** Plan mode proposes a file structure and approach,
and likely asks one or two clarifying questions. Typical questions to
expect, with suggested answers if you want to keep pace rather than
improvise live:

| Likely Question | Suggested Answer |
|-----------------|------------------|
| "What should the CSV column names be assumed as?" | "Assume columns: alert_id, severity, source, timestamp" |
| "Should this use argparse for command-line arguments?" | "Yes, accept the CSV file path as a command-line argument" |
| "Should invalid severity values be handled?" | "Yes, group anything unrecognized under an 'Unknown' category" |

**Narration point for the audience:** Nothing has been written to disk
yet. This is the checkpoint — if the proposed approach looks wrong, this
is where you'd redirect it, before any files exist.

---

## Step 2 — Handoff to Agent Mode: Execute

Once the plan looks reasonable, switch Chat to **Agent** mode and use:

> "That approach looks good — go ahead and build it."

**What should happen:** Agent mode begins creating files — typically a
main script, possibly a sample CSV, and depending on how it interpreted
the plan, maybe a short README. Watch for:

- Each file proposed as a diff/creation before it's committed to disk
- Narrate what's happening as each file appears — this is the moment
  that differentiates Agent mode from everything earlier in the series
- Review each file before accepting — don't auto-accept everything just
  because the demo is moving quickly

**If Agent mode asks for permission to run a terminal command** (for
example, to create a test CSV or run the script), this is expected —
confirm it, and use it as a teaching moment: Agent mode can take actions
beyond just writing files when needed to complete a task.

---

## Step 3 — Verify the Output

If Agent mode didn't generate one, create a sample CSV manually for
testing. Sample data to use:

```csv
alert_id,severity,source,timestamp
A001,Critical,Suricata,2026-06-01 08:15:00
A002,High,Splunk,2026-06-01 08:22:00
A003,Medium,Suricata,2026-06-01 09:05:00
A004,Critical,TheHive,2026-06-01 09:40:00
A005,Low,Splunk,2026-06-01 10:12:00
A006,High,Suricata,2026-06-01 10:30:00
A007,Unknown,Splunk,2026-06-01 11:00:00
```

Run the generated tool against this file and confirm the output groups
and counts alerts correctly, including the "Unknown" severity row if
the plan included that handling.

**Expected output shape (approximate):**
```
Severity Summary Report
------------------------
Critical: 2
High: 2
Medium: 1
Low: 1
Unknown: 1
```

---

## Optional Closer — Full Circle Moment

If time allows, bring back a tool from Session 3:

> Select the generated function. In Chat panel type:
> /tests using pytest, include edge cases for an empty CSV and an
> unrecognized severity value

This closes the loop on the series — the same `/tests` slash command from
Session 3, applied to code that Agent mode just built, generating test
coverage for output that didn't exist ten minutes earlier. It's a strong
note to end the demo portion of the final session on.

---

## Fallback If Agent Mode Behaves Unexpectedly

Live demos of autonomous execution carry more variance than the scripted
demos from earlier sessions. If Agent mode produces something noticeably
off-track:

- Don't troubleshoot live for more than a minute or two — narrate what
  you expected vs. what happened, and move on
- Have a pre-built version of the working CLI tool ready as a backup to
  show "here's what a completed version looks like" if the live build
  stalls
- This is itself a valid teaching moment: Agent mode output still needs
  review, and sometimes a second, more specific prompt gets better
  results than troubleshooting the first attempt
