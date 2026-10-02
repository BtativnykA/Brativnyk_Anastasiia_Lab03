from collections.abc import Iterator
from pathlib import Path


def read_lines(path: Path) -> Iterator[str]:
    """Read a file line by line lazily using `yield from`.

    The file is opened lazily and closed automatically
    when the generator is exhausted or garbage-collected.
    """
    with path.open("r", encoding="utf-8") as file:
        yield from file