from collections.abc import Iterable, Iterator
from itertools import islice

from stream_processor.models import StudentRecord


def batched_students(
    students: Iterable[StudentRecord],
    batch_size: int,
) -> Iterator[list[StudentRecord]]:
    """Yield lists of up to `batch_size` students.

    Uses itertools.islice so no full materialization occurs.
    """
    iterator = iter(students)
    while True:
        batch = list(islice(iterator, batch_size))
        if not batch:
            return
        yield batch