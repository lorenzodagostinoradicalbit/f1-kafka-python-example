import functools
import logging
from typing import Any, Callable, Dict


def singleton(f: Callable) -> Callable:
    instances: Dict[Any, Any] = {}

    @functools.wraps(f)
    def return_instance(*args, **kwargs):
        if f not in instances:
            instances[f] = f(*args, **kwargs)
        return instances[f]

    return return_instance


@singleton
def get_logger() -> logging.Logger:
    """
    Creates a logger singleton.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(logging.Formatter("%(asctime)s [%(threadName)s] [%(levelname)s] - %(message)s"))
    # doing this avoid duplicates, not clear why
    logger.propagate = False
    logger.addHandler(ch)
    return logger


__all__ = ["get_logger"]