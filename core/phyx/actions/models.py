"""Atomic actions produced by PHYX planners."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict


class ActionStatus(str, Enum):
    """Lifecycle status of an action."""

    PENDING = "pending"
    APPROVED = "approved"
    EXECUTING = "executing"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Action:
    """A structured action that can be validated before execution."""

    name: str
    parameters: Dict[str, str] = field(default_factory=dict)
    status: ActionStatus = ActionStatus.PENDING

    def approve(self) -> None:
        """Mark an action as approved for execution."""
        if not self.name.strip():
            raise ValueError("Action name must not be empty")
        self.status = ActionStatus.APPROVED
