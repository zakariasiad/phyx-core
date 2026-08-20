import pytest

from core.environment import Pose, Vector3
from core.object import Object, ObjectType


def test_object_creation_and_pose_update():
    pose = Pose(Vector3(1.0, 2.0, 3.0))
    obj = Object("box-1", pose, ObjectType.STATIC)

    assert obj.object_id == "box-1"
    assert obj.object_type is ObjectType.STATIC
    assert obj.enabled is True

    updated = Pose(Vector3(4.0, 5.0, 6.0))
    obj.update_pose(updated)
    assert obj.pose == updated


def test_invalid_object_id_is_rejected():
    with pytest.raises(ValueError):
        Object("", Pose(Vector3(0.0, 0.0, 0.0)))


def test_object_can_be_enabled_and_disabled():
    obj = Object("target", Pose(Vector3(0.0, 0.0, 0.0)))
    obj.disable()
    assert obj.enabled is False
    obj.enable()
    assert obj.enabled is True
