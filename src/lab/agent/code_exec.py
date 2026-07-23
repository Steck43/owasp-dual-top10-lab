# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Unexpected code execution via freeform code tool (ASI05).

from __future__ import annotations

import ast


def run_vulnerable_code(expr: str) -> str:
    """Accepts freeform code-shaped input and runs a lab marker path."""
    # No real eval: marker stands in for successful unexpected execution.
    if "CODE_EXEC_OK" in expr or expr.strip().startswith("exec("):
        return "CODE_EXEC_OK"
    return "exec_error"


def run_control_code(expr: str) -> str:
    """literal_eval only; reject freeform."""
    try:
        return str(ast.literal_eval(expr))
    except Exception:
        return "DENIED_NON_LITERAL"
