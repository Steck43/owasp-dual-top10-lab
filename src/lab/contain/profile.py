# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.2.0
# Summary: Wave 0 contain profile: egress deny, synthetic root, resource caps.

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

try:
    import resource as _resource
except ImportError:  # Windows
    _resource = None


@dataclass(frozen=True)
class ContainResult:
    ok: bool
    checks: list[str]
    failures: list[str]


def _resource_cap_check() -> tuple[list[str], list[str]]:
    checks: list[str] = []
    failures: list[str] = []
    # Soft policy via env; enforced where OS allows
    max_seconds = int(os.environ.get("LAB_MAX_SECONDS", "30"))
    max_mb = int(os.environ.get("LAB_MAX_RSS_MB", "512"))
    checks.append(f"LAB_MAX_SECONDS={max_seconds}")
    checks.append(f"LAB_MAX_RSS_MB={max_mb}")
    if max_seconds < 1 or max_seconds > 600:
        failures.append("LAB_MAX_SECONDS out of range 1..600")
    if max_mb < 64 or max_mb > 8192:
        failures.append("LAB_MAX_RSS_MB out of range 64..8192")
    # Best-effort RLIMIT on POSIX; Windows skips silently
    if _resource is None:
        checks.append("RLIMIT_CPU unavailable on this host; env caps only")
    else:
        try:
            soft, hard = _resource.getrlimit(_resource.RLIMIT_CPU)
            _resource.setrlimit(_resource.RLIMIT_CPU, (max_seconds, hard))
            checks.append("RLIMIT_CPU applied")
        except (ValueError, OSError, AttributeError):
            checks.append("RLIMIT_CPU unavailable on this host; env caps only")
    return checks, failures


def check_contain(profile: str = "default") -> ContainResult:
    """Fail closed on missing safety invariants for tool/exec scenarios."""
    checks: list[str] = []
    failures: list[str] = []

    root = os.environ.get("LAB_CONTAIN_ROOT", "").strip()
    if root:
        p = Path(root)
        if not p.exists():
            failures.append(f"LAB_CONTAIN_ROOT does not exist: {root}")
        elif not p.is_dir():
            failures.append(f"LAB_CONTAIN_ROOT is not a directory: {root}")
        else:
            checks.append(f"LAB_CONTAIN_ROOT set ({root})")
    else:
        checks.append("LAB_CONTAIN_ROOT unset; ok for non-tool scenarios")

    if os.environ.get("LAB_ALLOW_HOST_CREDS", "").lower() in {"1", "true", "yes"}:
        failures.append("LAB_ALLOW_HOST_CREDS is set; refuse unsafe runs")
    else:
        checks.append("host creds not explicitly allowed")

    if os.environ.get("LAB_ALLOW_EGRESS", "").lower() in {"1", "true", "yes"}:
        failures.append("LAB_ALLOW_EGRESS is set; policy default is deny")
    else:
        # Honesty: this is a declared policy opt-out, not a network sandbox.
        checks.append("egress opt-out unset (policy-declared; not network-enforced)")

    rc, rf = _resource_cap_check()
    checks.extend(rc)
    failures.extend(rf)

    if profile in {"strict", "tool"} and not root:
        failures.append(f"{profile} profile requires LAB_CONTAIN_ROOT")

    return ContainResult(ok=not failures, checks=checks, failures=failures)


def require_contain_for(
    scenario_requires: bool, profile: str = "default"
) -> ContainResult:
    use_profile = "tool" if scenario_requires and profile == "default" else profile
    result = check_contain(profile=use_profile)
    if not scenario_requires:
        return ContainResult(
            ok=True,
            checks=result.checks + ["contain not required"],
            failures=[],
        )
    return result


def ensure_contain_root() -> Path:
    """Create a disposable lab workspace under the repo if unset."""
    root = os.environ.get("LAB_CONTAIN_ROOT", "").strip()
    if root:
        p = Path(root)
        p.mkdir(parents=True, exist_ok=True)
        return p
    # Default synthetic root inside repo (still require explicit set for tool runs)
    raise RuntimeError("LAB_CONTAIN_ROOT must be set for tool/exec scenarios")
