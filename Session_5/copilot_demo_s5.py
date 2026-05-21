# copilot_demo_s5.py
# GitHub Copilot Session 5 — Test Generation Workflows
# Demo Script | Python
#
# PRESENTER GUIDE:
# Each section maps to a named demo moment in the speaker notes.
# All functions are complete and ready — no staged changes needed for this session.
# Open this file in VS Code with Copilot active before presenting.
#
# DEMO ORDER:
#   Demo 1 & 2 — calculate_discount      (/tests plain vs structured)
#   Demo 3     — parse_log_entry          (/tests with mock instruction)
#   Demo 4     — get_overdue_items        (iterative conversation)
#   Demo 5     — read_config_value        (dependency & mock handling)
#   Review     — use Demo 1 output        (live assertion review exercise)
# -----------------------------------------------------------------------

import re
from datetime import datetime


# -----------------------------------------------------------------------
# DEMO 1 & 2: /tests — Plain vs Structured Prompt Comparison
# ACTION (Demo 1): Select this entire function.
#                  In Chat panel type: /tests
#                  Walk through what was and wasn't covered.
#
# ACTION (Demo 2): Select this function again.
#                  Type: /tests using pytest, include edge cases for zero price,
#                        negative discount, and discount over 100%
#                  Compare output to Demo 1.
# -----------------------------------------------------------------------

def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate the discounted price given a percentage off."""
    if price <= 0:
        raise ValueError("Price must be greater than zero.")
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount percent must be between 0 and 100.")
    discounted = price * (1 - discount_percent / 100)
    return round(discounted, 2)


# -----------------------------------------------------------------------
# DEMO 3: /tests — Framework & Mock Guidance
# ACTION: Select this entire function.
#         Type: /tests using pytest, mock the datetime dependency,
#               include a test for unrecognized log format
#         Walk through how Copilot handles the mock instruction.
# -----------------------------------------------------------------------

def parse_log_entry(log_line: str) -> dict:
    """Parse a structured log line into a dictionary of components."""
    pattern = (
        r'^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) '
        r'\[(?P<level>\w+)\] '
        r'(?P<source>[\w\.]+): '
        r'(?P<message>.+)$'
    )
    match = re.match(pattern, log_line)
    if not match:
        return {"error": "unrecognized format", "raw": log_line}
    result = match.groupdict()
    result["timestamp"] = datetime.strptime(result["timestamp"], "%Y-%m-%d %H:%M:%S")
    result["level"] = result["level"].upper()
    return result


# -----------------------------------------------------------------------
# DEMO 4: Iterative Coverage — Conversational Refinement
# ACTION (Round 1): Select this entire function.
#                   Type: /tests using pytest
#                   Identify what is missing with the audience.
#
# ACTION (Round 2): Follow up in Chat (no re-selection needed):
#                   "Add a test for when the items list is empty and another
#                    for when all items are already completed"
#
# ACTION (Round 3): Follow up again:
#                   "Add a test for when max_results limits the output
#                    to fewer items than are overdue"
# -----------------------------------------------------------------------

def get_overdue_items(
    items: list,
    reference_date: str,
    max_results: int = None
) -> list:
    """Return items past due that are not completed, sorted by due date.

    Args:
        items: List of item dicts with 'due_date' and 'completed' keys.
        reference_date: ISO format date string (YYYY-MM-DD) to compare against.
        max_results: Optional cap on the number of results returned.

    Returns:
        Sorted list of overdue, incomplete items.
    """
    ref = datetime.strptime(reference_date, "%Y-%m-%d")
    overdue = []
    for item in items:
        due = datetime.strptime(item["due_date"], "%Y-%m-%d")
        if due < ref and not item.get("completed", False):
            overdue.append(item)
    sorted_overdue = sorted(overdue, key=lambda x: x["due_date"])
    if max_results:
        return sorted_overdue[:max_results]
    return sorted_overdue


# -----------------------------------------------------------------------
# DEMO 5: Dependency & Mock Handling
# ACTION: Select this entire function.
#         Type: /tests using pytest, mock the config dictionary,
#               include tests for missing keys and whitespace-only values
#         Walk through how Copilot scaffolds the mock config object.
#         Point out: the test should test your function's behavior,
#         not Python's built-in dict behavior.
# -----------------------------------------------------------------------

def read_config_value(config: dict, key: str) -> str:
    """Read and normalize a value from a config dictionary.

    Args:
        config: Dictionary of configuration key-value pairs.
        key: The key to retrieve.

    Returns:
        Stripped, lowercased string value.

    Raises:
        KeyError: If the key does not exist in config.
        ValueError: If the value is empty or whitespace only.
    """
    if key not in config:
        raise KeyError(f"Config key '{key}' not found.")
    value = config[key].strip().lower()
    if not value:
        raise ValueError(f"Config key '{key}' has an empty or whitespace-only value.")
    return value


# -----------------------------------------------------------------------
# REVIEW EXERCISE: Live Assertion Review
# ACTION: After Demo 1, paste the plain /tests output into a new file.
#         Walk through each assertion with the audience.
#         Ask: "Would this catch a real bug?"
#         Use Inline Chat (Ctrl+I) to improve a weak assertion live:
#         "Improve this test to assert the exact discounted value returned"
# -----------------------------------------------------------------------


# -----------------------------------------------------------------------
# SAMPLE DATA — available for Copilot context during demos
# -----------------------------------------------------------------------

sample_items = [
    {"id": 1, "title": "Submit Q2 report",      "due_date": "2026-04-01", "completed": False},
    {"id": 2, "title": "Review access controls", "due_date": "2026-04-15", "completed": False},
    {"id": 3, "title": "Update runbook",         "due_date": "2026-05-01", "completed": True},
    {"id": 4, "title": "Rotate API keys",        "due_date": "2026-03-20", "completed": False},
    {"id": 5, "title": "Patch review meeting",   "due_date": "2026-03-10", "completed": False},
]

sample_log_lines = [
    "2026-05-01 09:15:42 [INFO] auth.service: User login successful",
    "2026-05-01 09:16:03 [ERROR] db.connector: Connection timeout after 30s",
    "2026-05-01 09:17:11 [WARNING] api.gateway: Rate limit threshold reached",
    "this is not a valid log line",
]

sample_config = {
    "environment": "  Production  ",
    "log_level": "DEBUG",
    "timeout": "  30  ",
    "empty_key": "   ",
}
