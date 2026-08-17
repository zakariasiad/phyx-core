"""Core spatial models used by PHYX."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass(frozen=True)
class Vector3:
    """A point or vector in three-dimensional space."""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0


@dataclass(frozen=True)
class Pose:
    """A simplified pose representation.

    Orientation is intentionally omitted from v0.1. It will be introduced
    with a dedicated representation once the coordinate-frame conventions
    are finalized.
    """

    position: Vector3 = field(default_factory=Vector3)


@dataclass
class Environment:
    """A minimal world model containing named entities."""

    name: str
    entities: Dict[str, Pose] = field(default_factory=dict)

    def add_entity(self, entity_id: str, pose: Pose | None = None) -> None:
        """Add an entity to the environment."""
        if not entity_id:
            raise ValueError("entity_id must not be empty")
        if entity_id in self.entities:
            raise ValueError(f"Entity already exists: {entity_id}")
        self.entities[entity_id] = pose or Pose()

    def has_entity(self, entity_id: str) -> bool:
        """Return whether an entity exists in the environment."""
        return entity_id in self.entities
