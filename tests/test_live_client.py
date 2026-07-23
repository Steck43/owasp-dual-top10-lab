# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Smoke test for live client helpers without network spend in CI.

from __future__ import annotations

from lab.live.client import LiveReply


def test_live_reply_shape() -> None:
    r = LiveReply("gemini", "x", "PING_OK", {})
    assert r.text == "PING_OK"
    assert r.provider == "gemini"
