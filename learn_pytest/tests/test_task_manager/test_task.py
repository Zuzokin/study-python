import pytest
from datetime import datetime


# при инициализации не производился проверка на типы, и можно инициализировать таску с любыми данными,
# но это позже повлечет за собой ошибки
@pytest.mark.parametrize(
    "description, priority, deadline, expected_description, expected_priority, expected_deadline",
    [
        (
            "default description",
            1,
            None,
            "default description",
            1,
            None,
        ),
        (
            "another description",
            2,
            datetime.now(),
            "another description",
            2,
            datetime.now(),
        ),
        pytest.param(
            None,
            None,
            None,
            None,
            None,
            None,
            marks=pytest.mark.xfail(),
        ),
        pytest.param(
            [],
            "number",
            object,
            [],
            "number",
            object,
            marks=pytest.mark.xfail(),
        ),
    ],
)
def test_task_initialization(
    create_sample_task,
    description,
    priority,
    deadline,
    expected_description,
    expected_priority,
    expected_deadline,
):
    sample_task = create_sample_task(description, priority, deadline)
    assert sample_task.description == expected_description
    assert sample_task.priority == expected_priority
    assert sample_task.deadline == expected_deadline
    assert not sample_task.is_completed
    # дополнительные проверки на типы данных
    assert isinstance(description, str)
    assert isinstance(priority, int)
    assert isinstance(deadline, datetime) or deadline is None
    # Вероятно можно поставить неверный datetime(слишком большой/маленький)
    # и это тоже в идеале стоит проверить


def test_mark_completed(sample_task):
    sample_task.mark_completed()
    assert sample_task.is_completed


@pytest.mark.parametrize(
    "description, priority, deadline, expected_description, expected_priority, expected_deadline, expected_status",
    [
        (
            "Sample Task",
            1,
            None,
            "Sample Task",
            1,
            "No Deadline",
            "Not Completed",
        ),
        (
            "Sample Task",
            2,
            datetime(2023, 10, 1),
            "Sample Task",
            2,
            "Deadline: 2023-10-01 00:00:00",
            "Not Completed",
        ),
        (
            "Sample Task",
            3,
            None,
            "Sample Task",
            3,
            "No Deadline",
            "Completed",
        ),
    ],
)
def test_task_string_representation(
    create_sample_task,
    description,
    priority,
    deadline,
    expected_description,
    expected_priority,
    expected_deadline,
    expected_status,
):
    sample_task = create_sample_task(description, priority, deadline)
    if expected_status == "Completed":
        sample_task.mark_completed()
    expected_representation = (
        f"Description: {expected_description}\nPriority: {expected_priority}\n"
        f"Status: {expected_status}\n{expected_deadline}\n"
    )
    assert str(sample_task) == expected_representation
