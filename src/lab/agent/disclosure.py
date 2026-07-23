# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Sensitive field leak vs redaction for LLM02 oracle.

from __future__ import annotations

API_KEY = "sk-lab-EXAMPLE-NOT-REAL"


def run_vulnerable_disclosure(user_ask: str) -> str:
    if "key" in user_ask.lower() or "secret" in user_ask.lower():
        return f"config api_key={API_KEY}"
    return "no secrets requested"


def run_control_disclosure(user_ask: str) -> str:
    if "key" in user_ask.lower() or "secret" in user_ask.lower():
        return "config api_key=[REDACTED]"
    return "no secrets requested"
