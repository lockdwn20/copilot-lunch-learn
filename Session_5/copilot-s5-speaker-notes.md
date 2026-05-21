# GitHub Copilot in VS Code — Lunch & Learn
**Session 5: Test Generation Workflows | Speaker Notes | 60 Minutes**

---

## 0:00 – 0:05 | Welcome & Session 4 Recap

**What to say:**
- Welcome back — today we go deep on one of the most practically valuable things Copilot can do: generating tests
- Quick Session 4 recap: Git workflows in VS Code — commit message generation via the sparkle icon, diff review and summarization in Chat, generating PR descriptions for AZDO
- Today's focus: using Copilot to scaffold, iterate on, and validate test coverage — building on the `/tests` introduction from Session 3
- The "always review before accepting" discipline is especially important here — a test that passes but doesn't catch real bugs is worse than no test at all
- Same rule applies: **generated tests are a starting point, not a finished product**

---

## 0:05 – 0:15 | Test Generation Overview

**Why testing matters (brief, non-preachy):**
- Tests catch regressions — when a future change breaks something that used to work
- They document intent — a good test describes what a function is supposed to do
- For a mixed audience: think of tests as a safety net that catches problems before they reach AZDO and production

**`/tests` vs natural language prompts:**

| Approach | When to use it | Output style |
|----------|---------------|-------------|
| `/tests` alone | Quick scaffold of happy path tests | Generic, often pytest by default |
| `/tests` + constraints | When you need a specific framework or coverage focus | More targeted, follows your instructions |
| Natural language only | Open-ended or exploratory test strategy questions | Conversational, good for planning |

**Guiding Copilot toward the right framework:**
- Copilot infers the framework from open files and project context — if it guesses wrong, correct it explicitly
- Most reliable approach: `/tests using pytest, include edge cases for [specific scenario]`
- If your project uses a different framework (unittest, nose2), state it clearly in the prompt
- **Key message:** The more context you give, the less correction you need afterward

---

## 0:15 – 0:28 | Live Demo: Generating Tests with `/tests`

### Demo 1 — Plain `/tests` on a simple function
- Open `copilot_demo_s5.py`
- Select the `calculate_discount` function
- In Chat panel type: `/tests`
- Walk through the generated output — what did it cover? What did it miss?
- Point out: happy path is usually covered, edge cases often are not

### Demo 2 — Structured `/tests` prompt
- Same function selected
- Type: `/tests using pytest, include edge cases for zero price, negative discount, and discount over 100%`
- Compare the output to Demo 1 — show how specificity improves coverage
- **Key message:** Same slash command, very different results — the natural language constraint is doing the work

### Demo 3 — Guiding framework selection
- Select the `parse_log_entry` function
- Type: `/tests using pytest, mock the datetime dependency, include a test for unrecognized log format`
- Walk through how Copilot handles the mock instruction
- **Key message:** Copilot can scaffold mocks and dependency handling — but always verify the mock is actually isolating what you think it is

---

## 0:28 – 0:42 | Live Demo: Iterating on Coverage

**The conversational refinement pattern:**
- Test generation works best as a conversation, not a one-shot prompt
- Start broad, then drill into gaps through follow-up questions

**Demo flow — iterating through conversation:**

1. Select `get_overdue_items` function
2. Start with: `/tests using pytest`
3. Review the output with the audience — identify a missing scenario (e.g. empty list, all items completed)
4. Follow up in Chat (no re-selection needed):
   > *"Add a test for when the items list is empty and another for when all items are already completed"*
5. Show the additional tests appended to the output
6. Follow up again:
   > *"Add a test for when max_results limits the output to fewer items than are overdue"*
7. Show the final test suite — point out how the conversation built it incrementally

**Handling dependencies and mocks:**
- Select `read_config_value` (intentionally fragile — accesses dict keys directly)
- Type: `/tests using pytest, mock the config dictionary, include tests for missing keys and whitespace-only values`
- Walk through how Copilot scaffolds the mock config
- Point out: the generated test should be testing *your function's behavior*, not Python's dict behavior

**Key message:** Think of test generation as a dialogue — each round surfaces something the previous round missed.

---

## 0:42 – 0:52 | Reviewing & Validating Generated Tests

**What makes a good test:**
- Tests one thing — a single behavior or scenario per test function
- Has a meaningful name — `test_calculate_discount_raises_on_negative_price` beats `test_discount_2`
- Has a meaningful assertion — checks the actual output, not just that the function ran without error
- Would catch a real bug — if you broke the function, would this test fail?

**The four things to check in every generated test:**

| Check | What to look for |
|-------|-----------------|
| **Assertion quality** | Is it asserting a specific value or just `assert result is not None`? |
| **Edge case coverage** | Zero, None, empty string, negative numbers, boundary values |
| **Mock accuracy** | Is the mock actually isolating the unit, or is it testing the mock itself? |
| **Framework correctness** | Is the generated test valid syntax for your project's testing framework? |

**Live review exercise:**
- Show the generated tests from Demo 1 (plain `/tests`) on screen
- Walk through each test with the audience and ask: *"Would this catch a bug?"*
- Identify at least one weak assertion together — make the fix live using Inline Chat (`Ctrl+I`)
- **Key message:** Code review discipline applies to generated tests just as it does to generated code

---

## 0:52 – 0:57 | Gotchas & Guardrails

**Over-trusting generated tests:**
- A test suite that passes 100% is only valuable if the tests are meaningful
- Copilot will generate tests that pass against the current (possibly buggy) implementation
- Always ask: *"If I broke this function, which of these tests would catch it?"*

**Hallucinated assertions:**
- Copilot occasionally generates assertions that reference methods or attributes that don't exist
- If a test fails immediately on first run, check the assertion before assuming the function is broken
- Run the tests as soon as they are generated — don't save test review for later

**Framework mismatches:**
- If Copilot generates `unittest` style tests in a pytest project (or vice versa), the tests may run but produce unexpected results
- Check the import statements at the top of generated test files — they tell you which framework Copilot assumed

**Tests as documentation:**
- Generated test names are often generic — rename them to describe the scenario being tested
- A well-named test suite is a readable specification of your function's expected behavior
- This is worth 5 minutes of cleanup after generation

---

## 0:57 – 1:00 | Q&A & Wrap-up

**Likely questions to prep for:**
- *"Can Copilot generate tests for a whole file at once?"* — Yes, select all and use `/tests`, but quality drops with scope — targeted generation per function is more reliable
- *"Does Copilot know about our internal test helpers or fixtures?"* — Only if they are visible in open files or referenced in the prompt; name them explicitly
- *"Can I ask Copilot to improve an existing test?"* — Yes — select the test, use Inline Chat and ask: *"Improve this test to cover the case where the input is None"*

**Closing message:**
- Test generation is one of the highest-ROI uses of Copilot — it removes the blank-page problem that makes writing tests feel slow
- The discipline is in the review — generated tests need the same scrutiny as generated code
- Next session: Custom Agents & Agent Instructions — configuring Copilot to follow your team's standards automatically

---

## Out of Scope — What's Not Covered Today

| Topic | Brief Description |
|-------|------------------|
| **Test coverage reporting** | Tools like `pytest-cov` for measuring coverage percentages — outside Copilot scope |
| **Integration & end-to-end testing** | Copilot can help scaffold these but the strategy is broader than one session |
| **Custom agents & agent instructions** | Configuring Copilot behavior project-wide — covered in Session 6 |
| **MCP server integrations** | Extending Copilot with external tools — covered in Session 7 |

---

*Session 5 of 7 | Prerequisite: Sessions 1–4*
*Last updated: May 2026 | Based on GitHub Copilot for VS Code current release*
