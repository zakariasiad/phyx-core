import pytest

from core.environment import Pose, Vector3
from core.robot import Robot, RobotState


def make_robot() -> Robot:
    return Robot("robot-1", Pose(Vector3(0.0, 0.0, 0.0)))


def test_robot_identity_and_default_state():
    robot = make_robot()
    assert robot.robot_id == "robot-1"
    assert robot.state is RobotState.IDLE


def test_robot_state_lifecycle():
    robot = make_robot()
    robot.transition_to(RobotState.READY)
    robot.transition_to(RobotState.RUNNING)
    robot.transition_to(RobotState.PAUSED)
    robot.transition_to(RobotState.READY)
    assert robot.state is RobotState.READY


def test_invalid_state_transition_is_rejected():
    robot = make_robot()
    with pytest.raises(ValueError):
        robot.transition_to(RobotState.RUNNING)


def test_robot_identity_is_validated():
    with pytest.raises(ValueError):
        Robot("", Pose(Vector3(0.0, 0.0, 0.0)))


def test_robot_features_are_validated():
    with pytest.raises(ValueError):
        Robot("robot-1", Pose(Vector3(0.0, 0.0, 0.0)), capabilities={""})
