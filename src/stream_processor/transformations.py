from collections.abc import Iterable, Iterator
from stream_processor.models import StudentRecord


def normalize_names(
    students: Iterable[StudentRecord],
) -> Iterator[StudentRecord]:
    """Yield students with titles-cased names."""
    for student in students:
        yield student._replace(name=student.name.title())