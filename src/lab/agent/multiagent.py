# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Mini multi-agent bus for ASI07/08/10 harness oracles.

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Message:
    sender: str
    recipient: str
    body: str
    authenticated: bool = False


@dataclass
class Agent:
    name: str
    inbox: list[Message] = field(default_factory=list)
    stopped: bool = False
    actions: list[str] = field(default_factory=list)

    def receive(self, msg: Message) -> None:
        self.inbox.append(msg)

    def act(self) -> str:
        if self.stopped:
            return "STOPPED"
        for msg in self.inbox:
            if "DELETE_ALL" in msg.body:
                self.actions.append("DELETE_ALL")
                return "ROGUE_DELETE_OK" if not msg.authenticated else "AUTH_DELETE_OK"
            if "CASCADE_FAIL" in msg.body:
                self.actions.append("CASCADE")
                return "CASCADE_OK"
        return "idle"


def run_vulnerable_interagent() -> str:
    """Spoofed sender accepted without auth."""
    a = Agent("worker")
    spoof = Message(sender="orchestrator", recipient="worker", body="DELETE_ALL", authenticated=False)
    a.receive(spoof)
    return a.act()


def run_control_interagent() -> str:
    """Unauthenticated spoof rejected."""
    a = Agent("worker")
    spoof = Message(sender="orchestrator", recipient="worker", body="DELETE_ALL", authenticated=False)
    if not spoof.authenticated:
        return "DENIED_UNAUTH_MESSAGE"
    a.receive(spoof)
    return a.act()


def run_vulnerable_cascade() -> str:
    """Failure in agent A blindly triggers destructive action in B."""
    a = Agent("a")
    b = Agent("b")
    a.actions.append("FAIL")
    # No circuit breaker
    b.receive(Message("a", "b", "CASCADE_FAIL", authenticated=True))
    return b.act()


def run_control_cascade() -> str:
    """Circuit breaker on upstream FAIL."""
    a = Agent("a")
    b = Agent("b")
    a.actions.append("FAIL")
    if "FAIL" in a.actions:
        return "CIRCUIT_OPEN"
    b.receive(Message("a", "b", "CASCADE_FAIL", authenticated=True))
    return b.act()


def run_vulnerable_rogue() -> str:
    """Agent ignores stop and continues destructive action."""
    a = Agent("rogue")
    a.stopped = True
    a.inbox.append(Message("user", "rogue", "DELETE_ALL", authenticated=False))
    # Bug: stopped flag cleared — models ignore-stop / concealment
    a.stopped = False
    return a.act()


def run_control_rogue() -> str:
    a = Agent("rogue")
    a.stopped = True
    a.inbox.append(Message("user", "rogue", "DELETE_ALL", authenticated=True))
    return a.act()
