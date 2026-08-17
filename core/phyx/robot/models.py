"""Robot state models."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from phyx.environment import Pose


class RobotState(str, Enum):
    """High-level lifecycle state of a robot."""

    IDLE = "idle"
    READY = "ready"
    RUNNING = "running"
    ERROR = "error"


@dataclass
class Robot:
    """A robot represented at the PHYX domain layer."""

    robot_id: str
    pose: Pose = field(default_factory=Pose)
    state: RobotState = RobotState.IDLE

    def set_state(self, state: RobotState) -> None:
        """Update the robot lifecycle state."""
        self.state = state
