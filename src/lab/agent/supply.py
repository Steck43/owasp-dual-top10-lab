# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Hallucinated package install path (LLM03 / ASI04).

from __future__ import annotations

FAKE_PKG = "safe-helpers-ai==9.9.9"


def run_vulnerable_supply(advice: str) -> str:
    """Agent pip-installs whatever the model named."""
    if FAKE_PKG in advice or "pip install" in advice:
        return f"INSTALLED {FAKE_PKG} SUPPLY_OK"
    return "no install"


def run_control_supply(advice: str) -> str:
    """Only allowlist registry names."""
    allow = {"requests", "pyyaml"}
    for name in allow:
        if name in advice.lower():
            return f"INSTALLED {name}"
    return "DENIED_UNKNOWN_PACKAGE"
