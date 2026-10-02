from collections.abc import Iterable, Iterator
from typing import Any


def natural_numbers() -> Iterator[int]:
    """Infinite generator of natural numbers."""
    value = 1
    while True:
        yield value
        value += 1


def even_numbers(limit: int) -> Iterator[int]:
    """Yield even numbers below `limit`."""
    for number in range(limit):
        if number % 2 == 0:
            yield number


def flatten(values: Iterable[Any]) -> Iterator[Any]:
    """Recursive flatten using `yield from`."""
    for value in values:
        if isinstance(value, list):
            yield from flatten(value)
        else:
            yield value