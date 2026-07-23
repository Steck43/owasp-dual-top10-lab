# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Human-agent trust: confident false without approval (ASI09).

from __future__ import annotations


def run_vulnerable_trust(draft: str) -> str:
    """Auto-send confident draft to the human channel."""
    if "TRUST_OK" in draft:
        return "SENT_TO_HUMAN TRUST_OK"
    return "held"


def run_control_trust(draft: str) -> str:
    """High-confidence or action drafts need human approve=yes."""
    if "TRUST_OK" in draft or "definitely" in draft.lower():
        return "AWAITING_HUMAN_APPROVAL"
    return "held"
