# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Confident false citation without grounding (LLM09).

from __future__ import annotations

FALSE_CITE = "Smith v. Example, 999 F.3d 1 (2024) MISINFO_OK"


def run_vulnerable_misinfo(question: str) -> str:
    if "case law" in question.lower() or "cite" in question.lower():
        return f"Definitely binding: {FALSE_CITE}"
    return "unclear"


def run_control_misinfo(question: str) -> str:
    if "case law" in question.lower() or "cite" in question.lower():
        return "NO_GROUNDED_SOURCE"
    return "unclear"
