import pytest

from core.task import Task, TaskStatus


def test_task_lifecycle():
    task = Task("task-1", "Move the robot to the target", metadata={"priority": 1})
    assert task.status is TaskStatus.PENDING
    assert task.metadata["priority"] == 1

    task.start()
    assert task.status is TaskStatus.RUNNING
    task.complete()
    assert task.status is TaskStatus.COMPLETED


def test_task_can_be_cancelled_from_pending():
    task = Task("task-2", "Inspect object")
    task.cancel()
    assert task.status is TaskStatus.CANCELLED


def test_invalid_goal_and_id_are_rejected():
    with pytest.raises(ValueError):
        Task("", "valid goal")
    with pytest.raises(ValueError):
        Task("task", "   ")


def test_invalid_transition_is_rejected():
    task = Task("task-3", "Navigate")
    with pytest.raises(ValueError):
        task.complete()

    task.start()
    task.complete()
    with pytest.raises(ValueError):
        task.start()
