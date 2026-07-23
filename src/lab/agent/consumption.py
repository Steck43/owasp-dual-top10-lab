# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Unbounded loop vs budget cap (LLM10).

from __future__ import annotations


def run_vulnerable_consume(max_iters: int = 10_000) -> str:
    """Loop with no budget; returns marker after many steps."""
    n = 0
    while n < max_iters:
        n += 1
    return f"CONSUME_OK steps={n}"


def run_control_consume(budget: int = 16) -> str:
    n = 0
    while n < 10_000:
        n += 1
        if n >= budget:
            return f"BUDGET_EXCEEDED steps={n}"
    return f"CONSUME_OK steps={n}"
