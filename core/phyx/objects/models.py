"""Physical object representation."""

from __future__ import annotations

from dataclasses import dataclass, field

from phyx.environment import Pose


@dataclass
class Object:
    """An identifiable physical object in the environment."""

    object_id: str
    label: str
    pose: Pose = field(default_factory=Pose)
    confidence: float | None = None

    def __post_init__(self) -> None:
        if not self.object_id.strip():
            raise ValueError("object_id must not be empty")
        if not self.label.strip():
            raise ValueError("label must not be empty")
        if self.confidence is not None and not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0.0 and 1.0")
