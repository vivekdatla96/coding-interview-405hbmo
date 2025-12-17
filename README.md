Formula 1 Lap Time Processing – Coding Assessment
Overview

This project implements a Python batch process to analyze Formula 1 driver lap times from a CSV file. The program reads lap time data, computes performance statistics per driver, ranks drivers based on average lap time, and outputs the top three drivers.

The solution focuses on clarity, deterministic logic, logging, and correctness, suitable for an engineering take-home assessment.

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

All processing logic is implemented in:

src/lap_time_processor.py


The script performs the following steps:

Reads lap time data from a CSV file

Aggregates lap times by driver

Calculates average and fastest lap times

Applies deterministic ranking logic

Writes the top three drivers to an output CSV file

Input Format

The input CSV file must contain the following columns:

Column	Type	Description
Driver	string	Driver name or identifier
Time	number	Lap time in seconds

Notes:

The CSV file must include a header row

Lap times must be numeric

The input file is assumed to be well-formed

Input file location:

data/input/lap_times.csv

Output

The program generates a CSV file containing the top three drivers, ranked by average lap time.

Output columns:

Column	Description
Position	Driver rank
Driver	Driver name
AverageLapTime	Average lap time
FastestLapTime	Fastest lap time

Output file location:

data/output/top_3_drivers.csv

Ranking Logic

Drivers are ranked using the following deterministic criteria:

Average lap time (ascending)

Fastest lap time (ascending)

Driver name (alphabetical order)

This ensures consistent and reproducible results.

Logging & Error Handling

Uses Python’s built-in logging module

Logs key execution steps including:

File reading

Statistics calculation

Driver ranking

Output generation

Errors such as missing files or invalid data formats are logged and raised

How to Run
Prerequisites

Python 3.9 or higher

Execution

From the project root directory, run:

python src/lap_time_processor.py


Ensure the input file exists at:

data/input/lap_times.csv


The output file will be created at:

data/output/top_3_drivers.csv

Assumptions

Each driver has at least one lap time

Input data fits in memory

Lap times are measured in seconds

Only the top three drivers are required

Limitations & Future Improvements

Add command-line arguments for configurable input/output paths

Improve resilience by skipping malformed rows instead of failing

Add automated unit tests

Further modularize I/O and processing logic

Author

Vivek Datla
