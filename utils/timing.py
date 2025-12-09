import time
from typing import Tuple, Callable

from utils.types import Solution


def runtime(f: Callable[[], Solution]) -> Callable[[], Solution]:
    def t() -> Solution:
        start = time.time()
        parts: Solution = f()
        end = time.time()
        print(f"Completed in {(end - start):.8f} seconds.")
        return parts
    return t