import csv
import random
from pathlib import Path


def generate_test_file(path: Path, count: int) -> None:
    """Create a CSV file with `count` student records (~2% invalid)."""
    groups = ("PI-21", "PI-22", "PI-23", "PI-24")

    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["student_id", "name", "group", "grade"])

        for index in range(1, count + 1):
            # ~2% invalid records — to exercise the validation stage
            if index % 50 == 0:
                writer.writerow([index, f"Student {index}", random.choice(groups), "error"])
                continue

            writer.writerow([
                index,
                f"Student {index}",
                random.choice(groups),
                round(random.uniform(40.0, 100.0), 2),
            ])