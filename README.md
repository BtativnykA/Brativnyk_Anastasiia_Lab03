# Stream Processor

Лабораторна робота №3 з курсу «Професійний Python».
Варіант №1 — «Потокова обробка результатів студентів».

## Description

Lazy pipeline для потокової обробки великих CSV-файлів:
read → parse → validate → filter → aggregate.
Без повної матеріалізації даних у пам'яті.

## Features

- власний iterator class (`StudentIdIterator`, `StudentIdRange`);
- generator functions + `yield` + `yield from`;
- generator expressions;
- lazy pipeline з `itertools.islice`, `chain`;
- batch processing через `islice`;
- streaming statistics (Counter, streaming average, min/max);
- eager vs lazy benchmark через `tracemalloc`;
- time-to-first-result experiment.

## Requirements

Python 3.11+

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .

Run
python -m stream_processor.main

Project structure

src/stream_processor/
├── main.py                 — точка входу
├── readers.py              — streaming file reader (yield from)
├── parsers.py              — CSV parser
├── models.py               — StudentRecord (NamedTuple)
├── filters.py              — validation + filtering
├── transformations.py      — lazy transformations
├── batches.py              — batch processing
├── analytics.py            — streaming statistics
├── pipeline.py             — збірка lazy pipeline
├── iterators.py            — власний iterator class
├── generators.py           — generator functions
├── eager.py                — eager implementation
├── benchmark.py            — eager vs lazy
└── test_data_generator.py  — генерація CSV

Author
Student: Anastasiia Brativnyk
Group: ФеП-32
Lab: №3, Variant 1



## 🐍 Крок 20. Запуск

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m stream_processor.main