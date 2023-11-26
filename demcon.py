from functools import reduce
from operator import add
from typing import Callable


def filtered_fibonacci(filter: Callable[[int], bool], limit: int = 4_000_000) -> int:
    """Generator implementation for Fibonacci sequence, implementing upper limit
    and element filter. Elements are returned that satisfy the filter and do not
    exceed the upper limit.
    """
    a = 0                   # start value 1
    b = 1                   # start value 2
    while (b <= limit):     # generator continues until limit exceeded
        if filter(b):       # only return elements satisfying filter
            yield b
        a, b = b, a + b     # setup for next loop


if __name__ == "__main__":
    print("Solution: ",
          reduce(add, filtered_fibonacci(filter=lambda x: x % 2 == 0), 0))
