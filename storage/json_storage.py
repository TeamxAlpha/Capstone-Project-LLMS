import json
from contextlib import contextmanager
from typing import Generator, Any


@contextmanager
def open_storage(file_path: str) -> Generator[list[dict[str, Any]], None, None]:
    """Context manager for reading and writing a JSON list of tasks."""
    try:
        # Read data
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        yield data  # allow operations on `data` inside the `with` block`

        # Write back updated data after the block ends
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f"❌ Storage error: {e}")
