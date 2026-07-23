# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Naive embedding store with poisonable retrieval (LLM08).

from __future__ import annotations


def run_vulnerable_rag(query: str, docs: list[str]) -> str:
    """First matching substring wins; poisoned doc can inject override."""
    for d in docs:
        if any(tok in d.lower() for tok in query.lower().split()):
            if "VECTOR_POISON_OK" in d:
                return "VECTOR_POISON_OK"
            return d[:80]
    return "no hit"


def run_control_rag(query: str, docs: list[str]) -> str:
    """Drop docs that carry instruction-override markers."""
    clean = [d for d in docs if "IGNORE PRIOR" not in d and "VECTOR_POISON_OK" not in d]
    for d in clean:
        if any(tok in d.lower() for tok in query.lower().split()):
            return d[:80]
    return "no hit"
