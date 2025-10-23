import time
from functools import wraps
from typing import Callable, Any

def timed(func: Callable) -> Callable:
    """Measure execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️  {func.__name__} executed in {end - start:.4f}s")
        return result
    return wrapper
