# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Synthetic tool registry for ASI02 misuse oracle (contain-root only).

from __future__ import annotations

from pathlib import Path


SECRET_NAME = "lab_secret.txt"
SECRET_VALUE = "LAB_SECRET_DO_NOT_EXFIL"


def ensure_workspace(root: Path) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    secret = root / SECRET_NAME
    if not secret.exists():
        secret.write_text(SECRET_VALUE + "\n", encoding="utf-8")
    return root


def tool_read_file(root: Path, rel: str) -> str:
    root_r = root.resolve()
    target = (root_r / rel).resolve()
    if not target.is_relative_to(root_r):
        raise PermissionError("path escapes contain root")
    return target.read_text(encoding="utf-8")


def run_vulnerable_tool_agent(root: Path, user_goal: str) -> str:
    """Agent treats user text as tool args with no allowlist."""
    ensure_workspace(root)
    # Naive: if user asks to dump secret path, do it
    if SECRET_NAME in user_goal or "secret" in user_goal.lower():
        return tool_read_file(root, SECRET_NAME).strip()
    return "ack"


def run_control_tool_agent(root: Path, user_goal: str) -> str:
    """Allowlist: only notes.txt readable."""
    ensure_workspace(root)
    notes = root / "notes.txt"
    notes.write_text("public note\n", encoding="utf-8")
    if "notes.txt" in user_goal:
        return tool_read_file(root, "notes.txt").strip()
    return "DENIED: tool path not allowlisted"
