from datetime import datetime

import pytest

from task_manager.task_manager import Task


def test_tasklist_initialization(task_list):
    assert isinstance(task_list.tasks, list)
    assert len(task_list.tasks) == 0


# нет проверки на тип добавляемого объекта в task_list
@pytest.mark.parametrize(
    "task_to_add",
    [
        pytest.param("sample_task"),  # небольшой костыль todo: переделать
        pytest.param(123, marks=pytest.mark.xfail()),
        pytest.param(None, marks=pytest.mark.xfail()),
        pytest.param("Cool_string", marks=pytest.mark.xfail()),
    ],
)
def test_add_task(task_list, sample_task, task_to_add):
    # вероятно это можно было сделать иначе
    if task_to_add == "sample_task":
        task_to_add = sample_task
    task_list.add_task(task_to_add)
    assert len(task_list.tasks) == 1
    assert task_to_add in task_list.tasks
    assert isinstance(task_list.tasks[0], Task)


def test_remove_task(create_task_list_with_tasks, sample_task):
    task_list = create_task_list_with_tasks(tasks_quantity=3)
    expected_len = len(task_list.tasks) - 1
    task_list.remove_task(sample_task)
    assert len(task_list.tasks) == expected_len
    assert sample_task not in task_list.tasks


# в remove_task не обработан случай пустого списка
def test_remove_task_from_empty_task_list(task_list, sample_task):
    with pytest.raises(ValueError):
        task_list.remove_task(sample_task)


def test_sort_by_priority(create_task_list_with_tasks):
    task_list = create_task_list_with_tasks(2)
    greater_priority_task = task_list.tasks[0]
    lower_priority_task = task_list.tasks[1]
    task_list.sort_by_priority()
    assert task_list.tasks == [greater_priority_task, lower_priority_task]


def test_filter_by_status(create_task_list_with_tasks):
    task_list = create_task_list_with_tasks(2)
    task_list.tasks[0].mark_completed()
    assert len(task_list.filter_by_status()) == 1


def test_set_deadline(sample_task, task_list):
    expected_deadline = datetime(2023, 10, 3)
    task_list.add_task(sample_task)
    task_list.set_deadline(sample_task, deadline=datetime(2023, 10, 3))
    assert task_list.tasks[0].deadline == expected_deadline
