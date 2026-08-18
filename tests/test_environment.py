import pytest

from core.environment import Environment, Pose, Vector3


def test_environment_add_update_remove_entity():
    env = Environment("world")
    pose = Pose(Vector3(1.0, 2.0, 3.0))

    env.add_entity("robot-1", pose)
    assert env.get_pose("robot-1") == pose

    updated = Pose(Vector3(4.0, 5.0, 6.0))
    env.update_entity("robot-1", updated)
    assert env.get_pose("robot-1") == updated

    assert env.remove_entity("robot-1") == updated
    assert env.get_pose("robot-1") is None


def test_duplicate_entity_is_rejected():
    env = Environment("world")
    pose = Pose(Vector3(0.0, 0.0, 0.0))
    env.add_entity("box", pose)

    with pytest.raises(ValueError):
        env.add_entity("box", pose)


def test_invalid_identifier_is_rejected():
    with pytest.raises(ValueError):
        Environment("")

    env = Environment("world")
    with pytest.raises(ValueError):
        env.add_entity("   ", Pose(Vector3(0.0, 0.0, 0.0)))


def test_zero_quaternion_is_rejected():
    with pytest.raises(ValueError):
        Pose(Vector3(0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0))
