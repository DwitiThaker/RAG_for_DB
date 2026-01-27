import time
import logging

def retry_with_backoff(
    fn,
    *,
    retries: int = 3,
    delay: float = 5,
    exceptions: tuple = (Exception,),
    label: str = "operation",
):
    """
    Retries a function on failure with fixed backoff.
    """
    attempt = 0
    while True:
        try:
            return fn()
        except exceptions as e:
            attempt += 1
            if attempt > retries:
                logging.error(f"{label} failed after {retries + 1} attempts")
                raise
            logging.warning(
                f"{label} failed (attempt {attempt}/{retries}), retrying in {delay}s..."
            )
            time.sleep(delay)
