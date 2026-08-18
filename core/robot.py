"""Hardware-independent robot domain model for PHYX."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import FrozenSet

from .environment import Pose


class RobotState(str, Enum):
    IDLE = "idle"
    READY = "ready"
    RUNNING = "running"
    PAUSED = "paused"
    ERROR = "error"


_ALLOWED_TRANSITIONS: dict[RobotState, FrozenSet[RobotState]] = {
    RobotState.IDLE: frozenset({RobotState.READY, RobotState.ERROR}),
    RobotState.READY: frozenset({RobotState.RUNNING, RobotState.IDLE, RobotState.ERROR}),
    RobotState.RUNNING: frozenset({RobotState.PAUSED, RobotState.READY, RobotState.ERROR}),
    RobotState.PAUSED: frozenset({RobotState.RUNNING, RobotState.READY, RobotState.ERROR}),
    RobotState.ERROR: frozenset({RobotState.IDLE}),
}


@dataclass
class Robot:
    """Identity, state and capabilities of a PHYX robot.

    Hardware drivers, middleware and transport details intentionally remain
    outside this domain object.
    """

    robot_id: str
    pose: Pose
    capabilities: set[str] = field(default_factory=set)
    sensors: set[str] = field(default_factory=set)
    actuators: set[str] = field(default_factory=set)
    state: RobotState = RobotState.IDLE

    def __post_init__(self) -> None:
        if not isinstance(self.robot_id, str) or not self.robot_id.strip():
            raise ValueError("robot_id must be a non-empty string")
        self.capabilities = self._validate_features(self.capabilities, "capabilities")
        self.sensors = self._validate_features(self.sensors, "sensors")
        self.actuators = self._validate_features(self.actuators, "actuators")

    @staticmethod
    def _validate_features(values: set[str], name: str) -> set[str]:
        if not isinstance(values, set):
            raise TypeError(f"{name} must be a set of strings")
        if any(not isinstance(value, str) or not value.strip() for value in values):
            raise ValueError(f"{name} must contain only non-empty strings")
        return set(values)

    def transition_to(self, new_state: RobotState) -> None:
        if not isinstance(new_state, RobotState):
            raise ValueError("new_state must be a RobotState")
        if new_state == self.state:
            return
        if new_state not in _ALLOWED_TRANSITIONS[self.state]:
            raise ValueError(f"invalid robot state transition: {self.state.value} -> {new_state.value}")
        self.state = new_state
