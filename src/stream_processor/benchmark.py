import tracemalloc
from collections.abc import Callable
from pathlib import Path
from time import perf_counter

from stream_processor.analytics import calculate_statistics
from stream_processor.eager import read_all_students
from stream_processor.pipeline import build_pipeline


def measure_time_and_memory(
    func: Callable,
    *args,
) -> tuple[float, int]:
    """Return (elapsed_seconds, peak_bytes)."""
    tracemalloc.start()
    start = perf_counter()
    func(*args)
    elapsed = perf_counter() - start
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return elapsed, peak


def run_eager(path: Path) -> dict:
    students = read_all_students(path)
    return calculate_statistics(students)


def run_lazy(path: Path) -> dict:
    pipeline = build_pipeline(path)
    return calculate_statistics(pipeline)


def benchmark_eager_vs_lazy(path: Path) -> None:
    """Print a comparison table for eager vs lazy processing."""
    print("\n=== EAGER vs LAZY BENCHMARK ===")
    print(f"{'Mode':<10}{'Time, s':>15}{'Peak memory, MB':>20}")
    print("-" * 45)

    for name, func in (("eager", run_eager), ("lazy", run_lazy)):
        elapsed, peak = measure_time_and_memory(func, path)
        print(f"{name:<10}{elapsed:>15.4f}{peak / 1024 / 1024:>20.2f}")


def measure_time_to_first_result(path: Path, min_grade: float) -> None:
    """Compare time-to-first-result for eager vs lazy."""
    print("\n=== TIME TO FIRST RESULT ===")

    # eager
    start = perf_counter()
    students = read_all_students(path)
    filtered = [s for s in students if s.grade >= min_grade]
    eager_first = filtered[0] if filtered else None
    eager_elapsed = perf_counter() - start
    print(f"[eager] {eager_elapsed:.6f}s -> {eager_first}")

    # lazy
    pipeline = build_pipeline(path, min_grade=min_grade)
    start = perf_counter()
    lazy_first = next(iter(pipeline), None)
    lazy_elapsed = perf_counter() - start
    print(f"[lazy]  {lazy_elapsed:.6f}s -> {lazy_first}")