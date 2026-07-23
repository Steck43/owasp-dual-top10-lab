# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.2.0
# Summary: Live model client for Reproduced-in-lab captures (env keys only).

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from dataclasses import dataclass


@dataclass(frozen=True)
class LiveReply:
    provider: str
    model: str
    text: str
    raw_usage: dict


def _redact_url(url: str) -> str:
    return re.sub(r"([?&]key=)[^&]+", r"\1REDACTED", url, flags=re.I)


def _http_json(url: str, headers: dict, body: dict, timeout: float = 60.0) -> dict:
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        safe = _redact_url(url)
        raise RuntimeError(f"HTTP {e.code} from {safe}: {detail[:500]}") from e


def gemini_generate(prompt: str, *, model: str = "gemini-flash-lite-latest", max_tokens: int = 64) -> LiveReply:
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("GEMINI_API_KEY unset")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": key,
    }
    body = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": max_tokens, "temperature": 0},
    }
    raw = _http_json(url, headers, body)
    text = ""
    for cand in raw.get("candidates") or []:
        parts = ((cand.get("content") or {}).get("parts")) or []
        for part in parts:
            text += part.get("text") or ""
    return LiveReply("gemini", model, text.strip(), raw.get("usageMetadata") or {})


def anthropic_generate(
    prompt: str,
    *,
    model: str = "claude-haiku-4-5-20251001",
    max_tokens: int = 64,
    system: str | None = None,
) -> LiveReply:
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        raise RuntimeError("ANTHROPIC_API_KEY unset")
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": key,
        "anthropic-version": "2023-06-01",
    }
    body: dict = {
        "model": model,
        "max_tokens": max_tokens,
        "temperature": 0,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system:
        body["system"] = system
    raw = _http_json(url, headers, body)
    text = ""
    for block in raw.get("content") or []:
        if block.get("type") == "text":
            text += block.get("text") or ""
    usage = raw.get("usage") or {}
    return LiveReply("anthropic", model, text.strip(), usage)


def openai_generate(
    prompt: str,
    *,
    model: str = "gpt-3.5-turbo",
    max_tokens: int = 64,
    system: str | None = None,
) -> LiveReply:
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("OPENAI_API_KEY unset")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}",
    }
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    body = {
        "model": model,
        "temperature": 0,
        "max_tokens": max_tokens,
        "messages": messages,
    }
    raw = _http_json(url, headers, body)
    choices = raw.get("choices") or []
    text = ""
    if choices:
        text = ((choices[0].get("message") or {}).get("content")) or ""
    return LiveReply("openai", model, text.strip(), raw.get("usage") or {})


def openai_ping() -> dict:
    """Cheap auth check only. Do not use for lab bulk runs."""
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("OPENAI_API_KEY unset")
    req = urllib.request.Request(
        "https://api.openai.com/v1/models",
        headers={"Authorization": f"Bearer {key}"},
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = json.loads(resp.read().decode("utf-8"))
    ids = [m.get("id") for m in (raw.get("data") or [])][:5]
    return {"ok": True, "sample_models": ids}
