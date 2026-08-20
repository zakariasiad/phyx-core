"""Hardware- and provider-independent task domain model for PHYX."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class Task:
    """A goal with an explicit lifecycle and extensible metadata."""

    task_id: str
    goal: str
    status: TaskStatus = TaskStatus.PENDING
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self._validate_id(self.task_id)
        if not isinstance(self.goal, str) or not self.goal.strip():
            raise ValueError("task goals must be non-empty strings")

    @staticmethod
    def _validate_id(task_id: str) -> None:
        if not isinstance(task_id, str) or not task_id.strip():
            raise ValueError("task identifiers must be non-empty strings")

    def start(self) -> None:
        self._transition(TaskStatus.RUNNING)

    def complete(self) -> None:
        self._transition(TaskStatus.COMPLETED)

    def fail(self) -> None:
        self._transition(TaskStatus.FAILED)

    def cancel(self) -> None:
        self._transition(TaskStatus.CANCELLED)

    def _transition(self, target: TaskStatus) -> None:
        allowed = {
            TaskStatus.PENDING: {TaskStatus.RUNNING, TaskStatus.CANCELLED},
            TaskStatus.RUNNING: {
                TaskStatus.COMPLETED,
                TaskStatus.FAILED,
                TaskStatus.CANCELLED,
            },
            TaskStatus.COMPLETED: set(),
            TaskStatus.FAILED: set(),
            TaskStatus.CANCELLED: set(),
        }
        if target not in allowed[self.status]:
            raise ValueError(f"invalid task transition: {self.status.value} -> {target.value}")
        self.status = target
