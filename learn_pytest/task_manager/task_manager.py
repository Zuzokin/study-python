import datetime


class Task:
    def __init__(self, description: str, priority: int = 1, deadline=None):
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Completed" if self.is_completed else "Not Completed"
        deadline_info = f"Deadline: {self.deadline}" if self.deadline else "No Deadline"
        return f"Description: {self.description}\nPriority: {self.priority}\nStatus: {status}\n{deadline_info}\n"


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, task: Task):
        self.tasks.remove(task)

    def update_task(self, task: Task, new_description: str):
        if task in self.tasks:
            task.description = new_description

    def sort_by_priority(self):
        self.tasks.sort(key=lambda x: x.priority, reverse=True)

    def filter_by_status(self, completed: bool = False):
        return [task for task in self.tasks if task.is_completed == completed]

    def set_deadline(self, task: Task, deadline: datetime):
        task.deadline = deadline


# Пример использования
if __name__ == "__main__":
    task_list = TaskList()

    task1 = Task("Write report", priority=2)
    task_list.add_task(task1)
    task2 = Task("Buy groceries", priority=1)
    task_list.add_task(task2)
    task3 = Task("Call client", priority=3, deadline=datetime.datetime(2023, 10, 1))
    task_list.add_task(task3)

    task_list.sort_by_priority()

    print("All Tasks:")
    for task in task_list.tasks:
        print(task)

    completed_tasks = task_list.filter_by_status(completed=True)
    print("Completed Tasks:")
    for task in completed_tasks:
        print(task)

    task2.mark_completed()

    print("Updated Task List:")
    for task in task_list.tasks:
        print(task)
