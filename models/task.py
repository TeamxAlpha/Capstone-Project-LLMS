from __future__ import annotations
from typing import Iterator, List, Dict, Optional
from datetime import datetime

class Task:
    def __init__(self, task_id: int, title: str, description: str = "", due_date: Optional[str] = None):
        self.id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.now().isoformat()

    def to_dict(self) -> Dict:
        return vars(self)

    @classmethod
    def from_dict(cls, data: Dict) -> "Task":
        task = cls(data["id"], data["title"], data.get("description", ""), data.get("due_date"))
        task.completed = data.get("completed", False)
        task.created_at = data.get("created_at", datetime.now().isoformat())
        return task


class TaskCollection:
    """Implements iterator protocol for tasks"""
    def __init__(self, tasks: List[Task]):
        self._tasks = tasks
        self._index = 0

    def __iter__(self) -> Iterator[Task]:
        return self

    def __next__(self) -> Task:
        if self._index >= len(self._tasks):
            raise StopIteration
        task = self._tasks[self._index]
        self._index += 1
        return task
