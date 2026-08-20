"""Hardware- and simulator-independent object domain model for PHYX."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .environment import Pose


class ObjectType(str, Enum):
    """Semantic object categories understood by the PHYX core domain."""

    UNKNOWN = "unknown"
    STATIC = "static"
    DYNAMIC = "dynamic"
    TARGET = "target"
    OBSTACLE = "obstacle"


@dataclass
class Object:
    """An identifiable physical-world object represented by a pose."""

    object_id: str
    pose: Pose
    object_type: ObjectType = ObjectType.UNKNOWN
    enabled: bool = True

    def __post_init__(self) -> None:
        self._validate_id(self.object_id)

    @staticmethod
    def _validate_id(object_id: str) -> None:
        if not isinstance(object_id, str) or not object_id.strip():
            raise ValueError("object identifiers must be non-empty strings")

    def update_pose(self, pose: Pose) -> None:
        self.pose = pose

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False
