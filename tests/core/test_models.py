from phyx.actions import Action
from phyx.environment import Environment, Pose, Vector3
from phyx.robot import Robot, RobotState
from phyx.safety import SafetyValidator
from phyx.tasks import Task, TaskStatus


def test_environment_adds_entity() -> None:
    environment = Environment("test-world")
    environment.add_entity("red-cup", Pose(Vector3(1.0, 2.0, 0.0)))

    assert environment.has_entity("red-cup")
    assert environment.entities["red-cup"].position.x == 1.0


def test_robot_state_changes() -> None:
    robot = Robot("robot-01")
    robot.set_state(RobotState.READY)

    assert robot.state is RobotState.READY


def test_task_validation() -> None:
    task = Task("Find the red cup")
    task.validate()

    assert task.status is TaskStatus.VALIDATED


def test_action_passes_safety_validation() -> None:
    action = Action("navigate_to", {"target": "red-cup"})

    assert SafetyValidator().validate(action)


def test_safety_validator_rejects_safety_bypass() -> None:
    action = Action("bypass_safety")

    assert not SafetyValidator().validate(action)
