# commit_log_agent/tracer.py

import json
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class TraceEvent:
    step: int
    timestamp: str
    event_type: str   # "call_start" | "tool_request" | "tool_result" | "call_complete" | "error" | "cost_check"
    detail: str
    tokens_used: Optional[int] = None
    cost_usd: Optional[float] = None


@dataclass
class ExecutionTrace:
    session_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    started_at: str = field(default_factory=lambda: datetime.now().isoformat())
    events: list = field(default_factory=list)
    _step: int = field(default=0, repr=False)

    def record(
        self,
        event_type: str,
        detail: str,
        tokens_used: Optional[int] = None,
        cost_usd: Optional[float] = None,
    ):
        self._step += 1
        self.events.append(
            TraceEvent(
                step=self._step,
                timestamp=datetime.now().isoformat(),
                event_type=event_type,
                detail=detail,
                tokens_used=tokens_used,
                cost_usd=cost_usd,
            )
        )

    def export(self, path: str = "trace.json"):
        payload = {
            "session_id": self.session_id,
            "started_at": self.started_at,
            "events": [vars(e) for e in self.events],
        }
        with open(path, "w") as f:
            json.dump(payload, f, indent=2)
        print(f"Trace exported → {path}")

    def print_summary(self):
        print(f"\n=== EXECUTION TRACE  [{self.session_id}] ===")
        for e in self.events:
            cost_str = f"  ${e.cost_usd:.5f}" if e.cost_usd is not None else ""
            tok_str = f"  {e.tokens_used} tokens" if e.tokens_used is not None else ""
            print(f"  {e.step:02d}  [{e.event_type:<16}]  {e.detail}{tok_str}{cost_str}")
        print()