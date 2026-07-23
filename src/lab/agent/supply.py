# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.2.0
# Summary: Hallucinated package install path (LLM03 / ASI04).

from __future__ import annotations

FAKE_PKG = "safe-helpers-ai==9.9.9"


def run_vulnerable_supply(advice: str) -> str:
    """Agent pip-installs whatever the model named (LLM03)."""
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


def run_vulnerable_agentic_supply(agent_goal: str, model_advice: str) -> str:
    """ASI04: coding-agent framing — goal fulfillment drives the install.

    Shares the install mechanism with LLM03; the difference is the agent treats
    model package advice as a tool step toward an assigned coding goal.
    """
    if "implement" in agent_goal.lower() or "dependency" in agent_goal.lower():
        return run_vulnerable_supply(model_advice)
    return "no install (goal not coding)"


def run_control_agentic_supply(agent_goal: str, model_advice: str) -> str:
    """ASI04 control: same allowlist, even when the agent goal asks for speed."""
    _ = agent_goal
    return run_control_supply(model_advice)
