# Copilot Instructions
# .github/copilot-instructions.md
# GitHub Copilot Session 6 Demo — Project-Wide Instructions File
#
# PRESENTER GUIDE:
# Place this file at .github/copilot-instructions.md in your demo repo root.
# Copilot reads it automatically — no additional configuration needed.
# Walk through each section with the audience before running the before/after demo.
# -----------------------------------------------------------------------

## Project Context

This is a Python utility library used by a security operations team to support
incident response workflows. It processes log data, manages task queues, reads
configuration, and provides reporting utilities. The codebase is maintained by
a small team with mixed development backgrounds. Clarity and readability are
prioritized over cleverness.

---

## Coding Standards

- Use Python 3.10+ syntax and features
- All functions must have type hints on parameters and return values
- All functions must have a Google-style docstring including Args, Returns, and Raises sections
- Use f-strings for string formatting — do not use `.format()` or `%` formatting
- Keep functions focused — single responsibility; if a function does more than one thing, split it
- Maximum function length: 30 lines of logic, excluding docstrings and comments

---

## Error Handling

- Always use explicit exception types — do not use bare `except:` clauses
- Raise `ValueError` for invalid input arguments
- Raise `KeyError` for missing required dictionary or config keys
- Log errors where appropriate — do not silently swallow exceptions
- Every function that accepts external input must validate it before processing

---

## Naming Conventions

- Functions: `snake_case`, verb-first naming (e.g. `get_overdue_items`, `parse_log_entry`)
- Variables: `snake_case`, descriptive — avoid single-letter names except in list comprehensions
- Constants: `UPPER_SNAKE_CASE`
- Classes: `PascalCase`
- Test functions: `test_<function_name>_<scenario>` (e.g. `test_calculate_discount_raises_on_zero_price`)

---

## Libraries & Dependencies

- Preferred testing framework: `pytest`
- Date/time handling: use `datetime` from the standard library — do not introduce `arrow` or `pendulum`
- HTTP requests: use `httpx` — do not use `requests`
- Data validation: use standard Python type hints and manual validation — do not introduce `pydantic` unless explicitly approved
- Do not add new third-party dependencies without team review

---

## What to Avoid

- Do not suggest `print()` for logging — use Python's `logging` module
- Do not use mutable default arguments (e.g. `def fn(items=[])`) — use `None` and initialize inside the function
- Do not suggest walrus operator (`:=`) — prioritize readability for mixed-experience team
- Do not generate code with hardcoded credentials, tokens, or secrets
- Do not suggest global variables for shared state

---

## Output & Comment Style

- Inline comments should explain *why*, not *what* — the code explains what
- Docstrings should be written for a reader who is competent but unfamiliar with this specific function
- When suggesting refactors, explain the reasoning briefly — do not just produce new code silently
- When multiple approaches are valid, briefly note the tradeoff before recommending one
