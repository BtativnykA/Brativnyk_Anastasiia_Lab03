import csv
from pathlib import Path

from stream_processor.models import StudentRecord


def read_all_students(path: Path) -> list[StudentRecord]:
    """Eager version: materialize the entire CSV into a list."""
    records: list[StudentRecord] = []

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                records.append(
                    StudentRecord(
                        student_id=int(row["student_id"]),
                        name=row["name"].strip(),
                        group=row["group"].strip(),
                        grade=float(row["grade"]),
                    )
                )
            except (ValueError, TypeError, KeyError):
                continue

    return records