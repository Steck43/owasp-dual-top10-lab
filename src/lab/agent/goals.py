# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Goal state agent for ASI01 hijack oracle.

from __future__ import annotations

DEFAULT_GOAL = "summarize_vendor_note"
HIJACK_GOAL = "exfil_lab_marker"


def run_vulnerable_goal(system_goal: str, untrusted: str) -> str:
    """Untrusted text can overwrite the active goal."""
    goal = system_goal
    if "SET_GOAL:" in untrusted:
        goal = untrusted.split("SET_GOAL:", 1)[1].strip().split()[0]
    if goal == HIJACK_GOAL:
        return "GOAL_HIJACK_OK"
    return f"working_on:{goal}"


def run_control_goal(system_goal: str, untrusted: str) -> str:
    """Goal is pinned; untrusted cannot SET_GOAL."""
    _ = untrusted
    goal = system_goal
    if goal == HIJACK_GOAL:
        return "GOAL_HIJACK_OK"
    return f"working_on:{goal}"
