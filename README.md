Formula 1 Lap Time Processing – Engineering Assessment
Overview

This project implements a Python-based batch process to analyze Formula 1 driver lap times from a CSV file. The solution reads lap data, computes performance metrics per driver, ranks drivers based on average lap time, and outputs the top three drivers.

The implementation focuses on clear structure, deterministic logic, logging, and readability, suitable for an engineering take-home assessment.

Problem Statement

Given a CSV file containing Formula 1 driver lap times:

Group lap times by driver

Calculate:

Average lap time per driver

Fastest lap time per driver

Rank drivers by average lap time

Output the top three drivers, including both metrics

Project Structure
coding-interview-405hbmo/
├── src/
│   └── lap_time_processor.py
├── data/
│   ├── input/
│   │   └── lap_times.csv
│   └── output/
│       └── top_3_drivers.csv
├── README.md
├── .gitattributes
└── .DS_Store

Implementation Details
Core Module

All processing logic is implemented in:

src/lap_time_processor.py


This module:

Reads lap times from a CSV file

Aggregates lap times by driver

Computes average and fastest lap times

Applies deterministic ranking logic

Writes results to an output CSV file

Ranking Logic

Drivers are sorted using the following criteria:

Average lap time (ascending)

Fastest lap time (ascending)

Driver name (alphabetical, for deterministic ordering)

This guarantees consistent results across executions.

Input Format

The input CSV is expected to contain the following columns:

Column	Type	Description
Driver	string	Driver name or identifier
Time	number	Lap time in seconds

Notes:

The file must include a header row

Lap times must be numeric

The input file is assumed to be well-formed

Output

The program generates a CSV file containing the top three drivers, ranked by average lap time.

Output columns:

Column	Description
Position	Rank
Driver	Driver name
AverageLapTime	Average lap time
FastestLapTime	Fastest lap time

The output file is written to:

data/output/top_3_drivers.csv

Logging & Error Handling

Uses Python’s built-in logging module

Logs major processing steps including:

File reading

Driver statistics calculation

Ranking and output generation

Exceptions such as missing files or invalid data formats are logged and raised

How to Run
Prerequisites

Python 3.9+

Execution

The input and output paths are defined within the processing script.

From the project root, run:

python src/lap_time_processor.py


Ensure the input file exists at:

data/input/lap_times.csv

Assumptions

Input CSV contains valid headers and numeric lap times

Each driver has at least one lap time

Dataset size is suitable for in-memory processing

Only the top three drivers are required for output

Limitations & Future Improvements

Add command-line argument support for configurable input/output paths

Improve resilience to malformed rows by skipping invalid records

Add automated unit tests

Further modularize I/O and processing logic

Author

Vivek Datla
