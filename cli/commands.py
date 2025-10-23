from models.task import Task, TaskCollection
from storage.json_storage import open_storage
from utils.decorators import timed

FILE_PATH = "data.json"


@timed
def add_task(title: str, description: str = "", due_date: str = "") -> None:
    """Add a new task."""
    with open_storage(FILE_PATH) as data:
        new_id = len(data) + 1
        task = Task(new_id, title, description, due_date)
        data.append(task.to_dict())
        print(f"✅ Task '{title}' added.")


def list_tasks(show_completed: bool = False) -> None:
    """List all tasks (pending or completed)."""
    with open_storage(FILE_PATH) as data:
        if not data:
            print("📭 No tasks found yet.")
            return

        tasks = [Task.from_dict(t) for t in data if t["completed"] == show_completed]
        if not tasks:
            print("📭 No matching tasks (try listing the other category).")
            return

        print("\n=== Task List ===")
        for task in TaskCollection(tasks):
            status = "✅ Completed" if task.completed else "❌"
            print(f"{task.id}. {task.title} — {status}")


def mark_task_completed(task_id: int) -> None:
    """Mark a specific task as completed."""
    with open_storage(FILE_PATH) as data:
        for task in data:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"🎉 Task {task_id} marked as completed.")
                break
        else:
            print(f"⚠️ Task with ID {task_id} not found.")


def remove_task(task_id: int) -> None:
    """Remove a task by its ID."""
    with open_storage(FILE_PATH) as data:
        for task in data:
            if task["id"] == task_id:
                data.remove(task)
                print(f"🗑️ Task {task_id} removed.")
                break
        else:
            print(f"⚠️ Task with ID {task_id} not found.")
