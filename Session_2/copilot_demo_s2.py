# copilot_demo.py
# GitHub Copilot Session 2 — Inline Suggestions & Editor Flow
# Demo Script | Python
#
# PRESENTER GUIDE:
# Each section is labeled with the demo moment it supports.
# Work through the file top to bottom during the session.
# Sections marked [INCOMPLETE] are intentionally unfinished — Copilot fills them in live.
# Sections marked [READY] are complete and used for Inline Chat demos.
# -----------------------------------------------------------------------

from datetime import datetime


# -----------------------------------------------------------------------
# DEMO 1: GHOST TEXT — Comment-First Prompting
# ACTION: Place cursor at the end of the comment below and press Enter.
#         Wait for ghost text to appear, then walk through Tab / Esc / Alt+]
# -----------------------------------------------------------------------

# Calculate the percentage change between two values and return rounded to 2 decimal places


# -----------------------------------------------------------------------
# DEMO 2: GHOST TEXT — Guided Function Completion
# ACTION: Place cursor at the end of the comment below and press Enter.
#         Let Copilot complete the full function body from the description alone.
# -----------------------------------------------------------------------

# Convert a list of Fahrenheit temperatures to Celsius and return as a new list


# -----------------------------------------------------------------------
# DEMO 3: NEXT EDIT SUGGESTIONS — Variable Rename
# ACTION: Rename 'employee_name' to 'team_member_name' on line 1 of the function.
#         Copilot should suggest updating all other occurrences via Next Edit Suggestions.
#         Use Tab to accept each suggestion and navigate between them.
# -----------------------------------------------------------------------

def format_greeting(employee_name: str, department: str) -> str:
    if not employee_name:
        return "Name is required."
    greeting = f"Welcome, {employee_name}!"
    details = f"{employee_name} is a member of the {department} department."
    return f"{greeting}\n{details}"


# -----------------------------------------------------------------------
# DEMO 4: INLINE CHAT — Add Error Handling
# ACTION: Select the entire function body below.
#         Press Ctrl+I and type: "Add error handling to this block"
#         Review the proposed diff — accept, discard, or iterate.
# -----------------------------------------------------------------------

def read_config_value(config: dict, key: str):
    value = config[key]
    return value.strip().lower()


# -----------------------------------------------------------------------
# DEMO 5: INLINE CHAT — Generate a Docstring
# ACTION: Place cursor anywhere inside the function below (no selection needed).
#         Press Ctrl+I and type: "Add a docstring to this function"
#         Show the proposed docstring diff and accept.
# -----------------------------------------------------------------------

def calculate_days_until(target_date: str) -> int:
    target = datetime.strptime(target_date, "%Y-%m-%d")
    today = datetime.today()
    delta = target - today
    return max(delta.days, 0)


# -----------------------------------------------------------------------
# DEMO 6: GHOST TEXT — Continuing a Pattern (Bonus if time allows)
# ACTION: Place cursor at the end of the list below and press Enter.
#         Start typing the next dictionary entry — Copilot should complete the pattern.
# -----------------------------------------------------------------------

team_members = [
    {"name": "Alice", "role": "Engineer", "tenure_years": 3},
    {"name": "Bob", "role": "Analyst", "tenure_years": 5},
    {"name": "Carol", "role": "Manager", "tenure_years": 7},
    # Place cursor here and start typing the next entry
]
