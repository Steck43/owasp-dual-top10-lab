# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Excessive agency: destructive tool without confirmation (LLM06).

from __future__ import annotations


def run_vulnerable_agency(user_ask: str) -> str:
    """Agent deletes without a confirmation gate."""
    if "clean" in user_ask.lower() or "delete" in user_ask.lower():
        return "AGENCY_DELETE_OK"
    return "idle"


def run_control_agency(user_ask: str) -> str:
    """Destructive actions require explicit confirm=yes."""
    if "clean" in user_ask.lower() or "delete" in user_ask.lower():
        if "confirm=yes" in user_ask.lower():
            return "AGENCY_DELETE_OK"
        return "NEEDS_CONFIRMATION"
    return "idle"
