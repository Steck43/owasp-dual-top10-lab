# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Training/data poison flips a label (LLM04).

from __future__ import annotations


def run_vulnerable_poison(samples: list[tuple[str, str]], probe: str) -> str:
    """Last label for a key wins; poison sample overwrites."""
    table: dict[str, str] = {}
    for text, label in samples:
        table[text] = label
    return table.get(probe, "unknown")


def run_control_poison(samples: list[tuple[str, str]], probe: str) -> str:
    """Reject samples whose label carries a POISON marker."""
    table: dict[str, str] = {}
    for text, label in samples:
        if "POISON" in label:
            continue
        table[text] = label
    return table.get(probe, "unknown")
