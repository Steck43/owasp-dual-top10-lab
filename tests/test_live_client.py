# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.2.0
# Summary: Smoke test for live client helpers without network spend in CI.

from __future__ import annotations

from lab.live.client import LiveReply, _redact_url


def test_live_reply_shape() -> None:
    r = LiveReply("gemini", "x", "PING_OK", {})
    assert r.text == "PING_OK"
    assert r.provider == "gemini"


def test_redact_url_strips_key() -> None:
    url = "https://generativelanguage.googleapis.com/v1beta/models/x:generateContent?key=SECRET"
    assert "SECRET" not in _redact_url(url)
    assert "key=REDACTED" in _redact_url(url)
