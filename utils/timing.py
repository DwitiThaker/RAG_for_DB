import time
import functools
import logging

logging.basicConfig(
    level=logging.INFO,
    format="⏱️ %(message)s"
)


def log_time(step_name: str):
    """
    Decorator to log execution time of a function.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            logging.info(f"{step_name} took {(end - start):.3f} seconds")
            return result

        return wrapper

    return decorator
