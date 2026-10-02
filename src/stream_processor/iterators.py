from collections.abc import Iterator


class StudentIdIterator(Iterator[int]):
    """One-shot iterator over a range of student IDs.

    This object *is* an iterator: calling iter(it) returns itself,
    and after exhaustion it yields nothing.
    """

    def __init__(self, start: int, stop: int) -> None:
        self.current = start
        self.stop = stop

    def __iter__(self) -> "StudentIdIterator":
        return self

    def __next__(self) -> int:
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


class StudentIdRange:
    """Iterable: each call to iter() creates a fresh iterator.

    This is the recommended pattern — a container can be
    iterated multiple times.
    """

    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop

    def __iter__(self) -> StudentIdIterator:
        return StudentIdIterator(self.start, self.stop)