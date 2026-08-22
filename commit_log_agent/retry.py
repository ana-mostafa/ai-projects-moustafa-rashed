# commit_log_agent/retry.py

import time
import random
import logging
from functools import wraps
from typing import Tuple, Type

logger = logging.getLogger(__name__)


def with_retry(
    max_attempts: int = 4,
    base_delay_seconds: float = 1.0,
    retryable_exceptions: Tuple[Type[Exception], ...] = (Exception,),
):
    """
    Decorator that retries the wrapped function with exponential backoff
    and full jitter on any of the specified exceptions.

    Usage:
        @with_retry(max_attempts=4, retryable_exceptions=(RateLimitError, APIConnectionError))
        def call_llm(...):
            ...
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except retryable_exceptions as exc:
                    if attempt == max_attempts:
                        logger.error(
                            f"{func.__name__} failed after {max_attempts} attempts. "
                            f"Final error: {exc}"
                        )
                        raise

                    # Exponential backoff with full jitter
                    # Full jitter prevents thundering-herd: all retries would otherwise
                    # fire simultaneously after a burst failure.
                    ceiling = base_delay_seconds * (2 ** (attempt - 1))
                    delay = random.uniform(0, ceiling)

                    logger.warning(
                        f"{func.__name__} attempt {attempt}/{max_attempts} failed: {exc}. "
                        f"Retrying in {delay:.2f}s."
                    )
                    time.sleep(delay)

        return wrapper
    return decorator



# ---------------------------------------------------------
# TEMPORARY TEST — Retry behaviour
# ---------------------------------------------------------

# attempt_counter = 0

# @with_retry(
#     max_attempts=4,
#     base_delay_seconds=1.0,
#     retryable_exceptions=(Exception,),
# )
# def fake_api_call():

#     global attempt_counter
#     attempt_counter += 1

#     print(f"Running attempt {attempt_counter}")

#     if attempt_counter < 3:
#         raise Exception("Simulated API failure")

#     return "Success!"

# result = fake_api_call()
# print(result)