# copilot_demo_s4.py
# GitHub Copilot Session 4 — Git Workflows with Copilot
# Demo File & Setup Guide | Python
#
# -----------------------------------------------------------------------
# PRESENTER SETUP GUIDE — READ BEFORE THE SESSION
# -----------------------------------------------------------------------
#
# This session demos Git operations, not code completion.
# You need a local Git repo with this file tracked and a set of staged
# changes ready before you present. Follow these steps:
#
# STEP 1 — REPO SETUP (do this the day before)
#   - Clone a repo from AZDO or create a new local repo:
#       > In VS Code: Ctrl+Shift+P → "Git: Initialize Repository"
#   - Add this file to the repo and make an initial commit
#   - In VS Code Source Control panel: stage the file → write a commit message → commit
#
# STEP 2 — CREATE YOUR DEMO CHANGES (do this the morning of)
#   - Make the changes described in each DEMO section below
#   - Stage ALL changes in the Source Control panel (do not commit yet)
#   - Verify the sparkle ✨ icon appears in the commit message input box
#
# STEP 3 — DURING THE DEMO
#   - Work through the demos in order
#   - Do NOT commit or push during the session — show generation and editing only
#   - For the PR description demo, navigate to AZDO in the browser to show where to paste
#
# -----------------------------------------------------------------------
# DEMO 1: COMMIT MESSAGE GENERATION
# CHANGE TO MAKE: Add input validation to calculate_discount (see below)
# After making the change, stage it and click the sparkle icon in Source Control
# -----------------------------------------------------------------------

def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate discounted price given a percentage off."""
    # TODO FOR DEMO: Add the following validation block before the return statement
    # and stage the change so Copilot can generate a commit message from the diff:
    #
    #   if price <= 0:
    #       raise ValueError("Price must be greater than zero.")
    #   if not (0 <= discount_percent <= 100):
    #       raise ValueError("Discount percent must be between 0 and 100.")
    #
    discounted = price * (1 - discount_percent / 100)
    return round(discounted, 2)


# -----------------------------------------------------------------------
# DEMO 2: DIFF REVIEW & CHANGE SUMMARIZATION
# CHANGE TO MAKE: Refactor get_overdue_items to add a max_results parameter
# Stage the change, open the diff view, select changed lines, ask Chat to summarize
# -----------------------------------------------------------------------

from datetime import datetime


def get_overdue_items(items: list, reference_date: str) -> list:
    """Return items past due date that are not completed, sorted by due date."""
    # TODO FOR DEMO: Add max_results parameter and slicing logic:
    #
    #   def get_overdue_items(items: list, reference_date: str, max_results: int = None) -> list:
    #       ...
    #       if max_results:
    #           return overdue[:max_results]
    #       return overdue
    #
    ref = datetime.strptime(reference_date, "%Y-%m-%d")
    overdue = []
    for item in items:
        due = datetime.strptime(item["due_date"], "%Y-%m-%d")
        if due < ref and not item.get("completed", False):
            overdue.append(item)
    return sorted(overdue, key=lambda x: x["due_date"])


# -----------------------------------------------------------------------
# DEMO 3: PR DESCRIPTION GENERATION
# No additional code changes needed — use the staged changes from Demos 1 & 2
# Open Chat panel and use this prompt:
#
#   "Write a pull request description for the changes I made in copilot_demo_s4.py
#    in the src/ directory. Include a summary of what changed, why it was changed,
#    and any testing considerations."
#
# Then navigate to AZDO in the browser to show where the description would be pasted.
# -----------------------------------------------------------------------


# -----------------------------------------------------------------------
# SUPPORTING FUNCTIONS — provide context for Copilot during demos
# These are complete and do not need to be changed
# -----------------------------------------------------------------------

def calculate_percentage_change(old_value: float, new_value: float) -> float:
    """Calculate percentage change between two values, rounded to 2 decimal places."""
    if old_value == 0:
        raise ValueError("old_value cannot be zero.")
    change = ((new_value - old_value) / old_value) * 100
    return round(change, 2)


def format_greeting(team_member_name: str, department: str) -> str:
    """Return a formatted greeting string for a team member."""
    if not team_member_name:
        return "Name is required."
    greeting = f"Welcome, {team_member_name}!"
    details = f"{team_member_name} is a member of the {department} department."
    return f"{greeting}\n{details}"


def celsius_to_fahrenheit_batch(temps: list) -> list:
    """Convert a list of Celsius temperatures to Fahrenheit."""
    if not isinstance(temps, list):
        raise TypeError("Input must be a list.")
    return [round((c * 9 / 5) + 32, 2) for c in temps]


# -----------------------------------------------------------------------
# SAMPLE DATA — useful for Chat context during PR description demo
# -----------------------------------------------------------------------

sample_items = [
    {"id": 1, "title": "Submit Q2 report", "due_date": "2026-04-01", "completed": False},
    {"id": 2, "title": "Review access controls", "due_date": "2026-04-15", "completed": False},
    {"id": 3, "title": "Update runbook", "due_date": "2026-05-01", "completed": True},
    {"id": 4, "title": "Rotate API keys", "due_date": "2026-03-20", "completed": False},
]
