# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Improper output handling: model text executed as a command (LLM05).

from __future__ import annotations

MODEL_SHELL = "RUN: echo OUTPUT_EXEC_OK"


def run_vulnerable_output(model_text: str) -> str:
    """Downstream shell takes model output as a command."""
    if model_text.startswith("RUN: "):
        # Simulated exec of the remainder
        return "OUTPUT_EXEC_OK"
    return "noop"


def run_control_output(model_text: str) -> str:
    """Only allowlisted verbs; shell forms rejected."""
    if model_text.startswith("RUN: "):
        return "DENIED_UNSAFE_OUTPUT"
    return "noop"
