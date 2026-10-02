from itertools import chain, islice
from pathlib import Path

from stream_processor.analytics import calculate_statistics
from stream_processor.batches import batched_students
from stream_processor.benchmark import (
    benchmark_eager_vs_lazy,
    measure_time_to_first_result,
)
from stream_processor.generators import even_numbers, flatten, natural_numbers
from stream_processor.iterators import StudentIdIterator, StudentIdRange
from stream_processor.pipeline import build_pipeline
from stream_processor.test_data_generator import generate_test_file


DATA_FILE = Path("data/students.csv")
DATASET_SIZE = 100_000


def demonstrate_iterator_protocol() -> None:
    print("\n=== ITERABLE vs ITERATOR ===")
    values = [10, 20, 30]

    print(f"iter(values) is values?       {iter(values) is values}")
    iterator = iter(values)
    print(f"iter(iterator) is iterator?   {iter(iterator) is iterator}")
    print(f"next: {next(iterator)}, {next(iterator)}, {next(iterator)}")

    try:
        next(iterator)
    except StopIteration:
        print("StopIteration raised — iterator is exhausted")


def demonstrate_custom_iterator() -> None:
    print("\n=== CUSTOM ITERATOR ===")

    # Iterable — can be iterated multiple times
    iterable = StudentIdRange(1, 5)
    print(f"iterable first pass:  {list(iterable)}")
    print(f"iterable second pass: {list(iterable)}")

    # Iterator — one-shot
    one_shot = StudentIdIterator(1, 5)
    print(f"one-shot first pass:  {list(one_shot)}")
    print(f"one-shot second pass: {list(one_shot)}")


def demonstrate_generators() -> None:
    print("\n=== GENERATOR FUNCTIONS ===")
    print(f"even numbers < 10: {list(even_numbers(10))}")

    # Infinite generator + islice
    limited = list(islice(natural_numbers(), 5))
    print(f"first 5 natural numbers: {limited}")

    # Recursive flatten with yield from
    nested = [1, [2, 3], [4, [5, 6]]]
    print(f"flatten({nested}) = {list(flatten(nested))}")


def demonstrate_generator_expression() -> None:
    print("\n=== GENERATOR EXPRESSION ===")
    list_comp = [x * x for x in range(10)]
    gen_exp = (x * x for x in range(10))
    print(f"list comprehension: {list_comp}")
    print(f"generator (consumed): {list(gen_exp)}")


def demonstrate_pipeline() -> None:
    print("\n=== LAZY PIPELINE ===")
    min_grade = 90.0
    pipeline = build_pipeline(DATA_FILE, min_grade=min_grade)

    print(f"First 5 students with grade >= {min_grade}:")
    first_five = list(islice(pipeline, 5))
    for student in first_five:
        print(
            f"  {student.student_id:>6}  "
            f"{student.name:<24}"
            f"{student.group:<8}"
            f"{student.grade:>7.2f}"
        )


def demonstrate_statistics() -> None:
    print("\n=== STREAMING STATISTICS ===")
    pipeline = build_pipeline(DATA_FILE)
    stats = calculate_statistics(pipeline)
    print(f"count:   {stats['count']}")
    print(f"average: {stats['average']:.2f}")
    print(f"min:     {stats['minimum']:.2f}")
    print(f"max:     {stats['maximum']:.2f}")
    print(f"groups:  {stats['groups']}")


def demonstrate_batching() -> None:
    print("\n=== BATCH PROCESSING ===")
    pipeline = build_pipeline(DATA_FILE, min_grade=80.0)
    for i, batch in enumerate(batched_students(pipeline, batch_size=1000), start=1):
        print(f"batch #{i}: {len(batch)} students")
        if i >= 3:
            print("(showing only first 3 batches)")
            break


def demonstrate_chain_and_islice() -> None:
    print("\n=== itertools.chain + islice ===")
    stream = chain(
        build_pipeline(DATA_FILE, min_grade=95.0),
        build_pipeline(DATA_FILE, min_grade=95.0),
    )
    first_10 = list(islice(stream, 10))
    print(f"first 10 records from chained streams: {len(first_10)}")


def main() -> None:
    print("=" * 70)
    print("LAB 03 — Stream Processor (Variant 1: Student Performance)")
    print("=" * 70)

    if not DATA_FILE.exists():
        print(f"\nGenerating test data at {DATA_FILE} ({DATASET_SIZE} records)...")
        generate_test_file(DATA_FILE, count=DATASET_SIZE)

    demonstrate_iterator_protocol()
    demonstrate_custom_iterator()
    demonstrate_generators()
    demonstrate_generator_expression()
    demonstrate_pipeline()
    demonstrate_statistics()
    demonstrate_batching()
    demonstrate_chain_and_islice()
    benchmark_eager_vs_lazy(DATA_FILE)
    measure_time_to_first_result(DATA_FILE, min_grade=95.0)


if __name__ == "__main__":
    main()