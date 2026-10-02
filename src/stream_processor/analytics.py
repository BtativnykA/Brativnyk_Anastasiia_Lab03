from collections import Counter
from collections.abc import Iterable

from stream_processor.models import StudentRecord


def calculate_statistics(
    students: Iterable[StudentRecord],
) -> dict:
    """Compute count, average, min, max and group Counter.

    Peak memory is independent of dataset size — records
    are consumed one by one.
    """
    count = 0
    total = 0.0
    minimum: float | None = None
    maximum: float | None = None
    groups: Counter[str] = Counter()

    for student in students:
        grade = student.grade
        count += 1
        total += grade
        groups[student.group] += 1

        if minimum is None or grade < minimum:
            minimum = grade
        if maximum is None or grade > maximum:
            maximum = grade

    average = total / count if count else 0.0

    return {
        "count": count,
        "average": average,
        "minimum": minimum,
        "maximum": maximum,
        "groups": dict(groups),
    }