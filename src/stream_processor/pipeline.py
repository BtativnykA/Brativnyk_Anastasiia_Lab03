from collections.abc import Iterator
from pathlib import Path

from stream_processor.filters import (
    filter_by_group,
    filter_by_min_grade,
    validate_students,
)
from stream_processor.models import StudentRecord
from stream_processor.parsers import parse_csv_rows
from stream_processor.readers import read_lines
from stream_processor.transformations import normalize_names


def build_pipeline(
    path: Path,
    min_grade: float | None = None,
    group: str | None = None,
) -> Iterator[StudentRecord]:
    """Build a lazy pipeline from a CSV file.

    Stages:
        read_lines -> parse_csv_rows -> validate_students
                   -> normalize_names -> filter_by_group
                   -> filter_by_min_grade
    """
    lines = read_lines(path)
    rows = parse_csv_rows(lines)
    valid = validate_students(rows)
    normalized = normalize_names(valid)

    result: Iterator[StudentRecord] = normalized

    if group is not None:
        result = filter_by_group(result, group)
    if min_grade is not None:
        result = filter_by_min_grade(result, min_grade)

    return result