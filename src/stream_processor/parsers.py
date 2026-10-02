import csv
from collections.abc import Iterable, Iterator


def parse_csv_rows(lines: Iterable[str]) -> Iterator[dict[str, str]]:
    """Parse CSV lines into dict rows lazily."""
    reader = csv.DictReader(lines)
    yield from reader