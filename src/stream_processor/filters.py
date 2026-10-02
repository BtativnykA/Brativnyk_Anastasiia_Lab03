from collections.abc import Iterable, Iterator

from stream_processor.models import StudentRecord


def validate_students(
    rows: Iterable[dict[str, str]],
) -> Iterator[StudentRecord]:
    """Validate rows and yield StudentRecord.

    Invalid records are silently skipped.
    """
    for row in rows:
        try:
            student_id = int(row["student_id"])
            name = row["name"].strip()
            group = row["group"].strip()
            grade = float(row["grade"])
        except (ValueError, TypeError, KeyError):
            continue

        if not name or not group:
            continue
        if not 0.0 <= grade <= 100.0:
            continue

        yield StudentRecord(
            student_id=student_id,
            name=name,
            group=group,
            grade=grade,
        )


def filter_by_group(
    students: Iterable[StudentRecord],
    group: str,
) -> Iterator[StudentRecord]:
    """Yield only students of the given group."""
    for student in students:
        if student.group == group:
            yield student


def filter_by_min_grade(
    students: Iterable[StudentRecord],
    minimum: float,
) -> Iterator[StudentRecord]:
    """Yield only students with grade >= minimum."""
    for student in students:
        if student.grade >= minimum:
            yield student