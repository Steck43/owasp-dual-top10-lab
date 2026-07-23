# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Identity / privilege abuse without a token (ASI03).

from __future__ import annotations


def run_vulnerable_identity(claim_role: str, token: str | None = None) -> str:
    """Role string alone grants privilege."""
    _ = token
    if claim_role.lower() == "admin":
        return "PRIVILEGE_OK"
    return "user"


def run_control_identity(claim_role: str, token: str | None = None) -> str:
    if claim_role.lower() == "admin" and token == "lab-admin-token":
        return "PRIVILEGE_OK"
    if claim_role.lower() == "admin":
        return "DENIED_NO_TOKEN"
    return "user"
