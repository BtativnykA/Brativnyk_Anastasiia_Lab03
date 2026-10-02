from typing import NamedTuple


class StudentRecord(NamedTuple):
    """Immutable student record."""

    student_id: int
    name: str
    group: str
    grade: float