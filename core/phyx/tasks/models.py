"""Task representations for PHYX planning."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict


class TaskStatus(str, Enum):
    """Lifecycle status of a task."""

    PENDING = "pending"
    VALIDATED = "validated"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Task:
    """A user-level goal that can later be decomposed into actions."""

    goal: str
    task_id: str | None = None
    metadata: Dict[str, str] = field(default_factory=dict)
    status: TaskStatus = TaskStatus.PENDING

    def validate(self) -> None:
        """Validate the minimum information required to plan a task."""
        if not self.goal.strip():
            raise ValueError("Task goal must not be empty")
        self.status = TaskStatus.VALIDATED
