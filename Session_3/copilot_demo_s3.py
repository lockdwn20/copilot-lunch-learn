# copilot_demo_s3.py
# GitHub Copilot Session 3 — Slash Commands & Structured Prompting
# Demo Script | Python
#
# PRESENTER GUIDE:
# Each section maps to a named demo moment in the speaker notes.
# Sections marked [DEMO TARGET] are the ones to select and run slash commands against.
# Sections marked [INTENTIONAL BUGS] contain deliberate errors for /fix demos.
# Work through the file top to bottom during the session.
# -----------------------------------------------------------------------

import re
from datetime import datetime


# -----------------------------------------------------------------------
# DEMO 1: /explain — Complex Function
# ACTION: Select the entire parse_log_entry function below.
#         In Chat panel type: /explain
#         Show Copilot's plain language breakdown of the logic.
#
# SECOND PASS: Select only the regex pattern line.
#              Type /explain again to show scoped explanation.
# -----------------------------------------------------------------------

# [DEMO TARGET]
def parse_log_entry(log_line: str) -> dict:
    pattern = r'^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(?P<level>\w+)\] (?P<source>[\w\.]+): (?P<message>.+)$'
    match = re.match(pattern, log_line)
    if not match:
        return {"error": "unrecognized format", "raw": log_line}
    result = match.groupdict()
    result["timestamp"] = datetime.strptime(result["timestamp"], "%Y-%m-%d %H:%M:%S")
    result["level"] = result["level"].upper()
    return result


# -----------------------------------------------------------------------
# DEMO 2: /fix — Logic Bugs
# ACTION: Select the entire calculate_discount function below.
#         In Chat panel or Inline Chat (Ctrl+I) type: /fix
#         Review the proposed diff and walk through what Copilot identified.
#
# INTENTIONAL BUGS:
#   - Discount is applied additively instead of multiplicatively
#   - No guard against price being zero or negative
#   - Returns None implicitly when discount_percent is 0
# -----------------------------------------------------------------------

# [INTENTIONAL BUGS]
def calculate_discount(price: float, discount_percent: float) -> float:
    if discount_percent > 0:
        discounted = price - discount_percent
        return discounted
    if discount_percent == 100:
        return 0.0


# -----------------------------------------------------------------------
# DEMO 3: /fix — Missing Error Handling
# ACTION: Select the entire connect_to_database function below.
#         Type: /fix and explain why each change was made
#         Show that /fix works on structural issues, not just syntax.
#
# INTENTIONAL BUGS:
#   - No error handling around the connection attempt
#   - Config keys accessed without validation
#   - No return value on failure
# -----------------------------------------------------------------------

# [INTENTIONAL BUGS]
def connect_to_database(config: dict):
    host = config["host"]
    port = config["port"]
    user = config["user"]
    password = config["password"]
    connection_string = f"postgresql://{user}:{password}@{host}:{port}/appdb"
    # Simulated connection — replace with real DB driver in production
    print(f"Connecting to {connection_string}")
    return connection_string


# -----------------------------------------------------------------------
# DEMO 4: /tests — Basic Test Generation
# ACTION: Select the entire calculate_percentage_change function below.
#         In Chat panel type: /tests
#         Walk through the generated test cases.
#
# SECOND PASS: Type the structured prompt version:
#   /tests using pytest, include edge cases for zero and negative values
#         Compare the two outputs to show how natural language shapes results.
# -----------------------------------------------------------------------

# [DEMO TARGET]
def calculate_percentage_change(old_value: float, new_value: float) -> float:
    if old_value == 0:
        raise ValueError("old_value cannot be zero.")
    change = ((new_value - old_value) / old_value) * 100
    return round(change, 2)


# -----------------------------------------------------------------------
# DEMO 5: /tests — More Complex Target (Bonus if time allows)
# ACTION: Select the entire celsius_to_fahrenheit_batch function below.
#         Type: /tests using pytest, include type validation and empty list handling
# -----------------------------------------------------------------------

# [DEMO TARGET — BONUS]
def celsius_to_fahrenheit_batch(temps: list) -> list:
    if not isinstance(temps, list):
        raise TypeError("Input must be a list.")
    return [round((c * 9 / 5) + 32, 2) for c in temps]


# -----------------------------------------------------------------------
# DEMO 6: Structured Prompting — Three-Part Pattern (Closer)
# ACTION: Select the get_overdue_items function below.
#         Use the three-part prompt pattern from the speaker notes:
#   /explain focusing on the filter logic in plain language suitable for a non-developer
#         Show how adding scope and constraint changes the quality of the output.
# -----------------------------------------------------------------------

# [DEMO TARGET]
def get_overdue_items(items: list, reference_date: str) -> list:
    ref = datetime.strptime(reference_date, "%Y-%m-%d")
    overdue = []
    for item in items:
        due = datetime.strptime(item["due_date"], "%Y-%m-%d")
        if due < ref and not item.get("completed", False):
            overdue.append(item)
    return sorted(overdue, key=lambda x: x["due_date"])
