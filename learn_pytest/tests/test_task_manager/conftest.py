from datetime import datetime

import pytest

from task_manager.task_manager import Task, TaskList

from faker import Faker

fake = Faker("ru_RU")


@pytest.fixture(scope="function")
def sample_task():
    return Task("Sample Task", 1, None)


@pytest.fixture(scope="function")
def create_sample_task():
    def task(description, priority, deadline):
        return Task(description, priority, deadline)

    return task


@pytest.fixture(scope="function")
def task_list():
    return TaskList()


@pytest.fixture(scope="function")
def create_task_list_with_tasks(task_list, sample_task):
    def create_multi_task_list(tasks_quantity):
        # [task_list.add_task(sample_task) for i in range(tasks_quantity)]
        for i in range(tasks_quantity - 1):
            task = Task(
                description=fake.sentence(),
                priority=i + 3,
                deadline=datetime(2023, 10, i + 3),
            )
            task_list.add_task(task)
        task_list.add_task(sample_task)
        return task_list

    return create_multi_task_list
