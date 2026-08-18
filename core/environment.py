"""Hardware- and simulator-independent environment domain model for PHYX."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass(frozen=True)
class Vector3:
    """Three-dimensional vector expressed in metres."""

    x: float
    y: float
    z: float


@dataclass(frozen=True)
class Pose:
    """Position and orientation in a right-handed Cartesian frame.

    Position is expressed in metres. Orientation is represented as a unit
    quaternion (x, y, z, w).
    """

    position: Vector3
    orientation: tuple[float, float, float, float] = (0.0, 0.0, 0.0, 1.0)

    def __post_init__(self) -> None:
        if len(self.orientation) != 4:
            raise ValueError("orientation must contain four quaternion values")
        norm = sum(value * value for value in self.orientation) ** 0.5
        if norm == 0.0:
            raise ValueError("orientation quaternion must not be zero")


@dataclass
class Environment:
    """Collection of uniquely identified entities and their poses."""

    environment_id: str
    entities: Dict[str, Pose] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self._validate_id(self.environment_id)
        for entity_id in self.entities:
            self._validate_id(entity_id)

    @staticmethod
    def _validate_id(entity_id: str) -> None:
        if not isinstance(entity_id, str) or not entity_id.strip():
            raise ValueError("entity identifiers must be non-empty strings")

    def add_entity(self, entity_id: str, pose: Pose) -> None:
        self._validate_id(entity_id)
        if entity_id in self.entities:
            raise ValueError(f"entity already exists: {entity_id}")
        self.entities[entity_id] = pose

    def update_entity(self, entity_id: str, pose: Pose) -> None:
        self._validate_id(entity_id)
        if entity_id not in self.entities:
            raise KeyError(entity_id)
        self.entities[entity_id] = pose

    def remove_entity(self, entity_id: str) -> Pose:
        self._validate_id(entity_id)
        try:
            return self.entities.pop(entity_id)
        except KeyError:
            raise KeyError(entity_id) from None

    def get_pose(self, entity_id: str) -> Optional[Pose]:
        self._validate_id(entity_id)
        return self.entities.get(entity_id)
