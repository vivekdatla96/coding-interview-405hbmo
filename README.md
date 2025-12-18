# Formula 1 Lap Time Analysis

## Overview

This project implements a Python-based batch process to analyze Formula 1 driver lap times from a CSV file. The program reads lap time data, computes key performance metrics per driver, ranks drivers based on average lap time, and outputs the top three drivers.

The solution emphasizes clear structure, deterministic logic, logging, and correctness, making it suitable for an engineering take-home assessment.

---

## Problem Statement

Given a CSV file containing Formula 1 driver lap times, the program must:

* Calculate the **average lap time** for each driver
* Identify the **fastest lap time** per driver
* Rank drivers by:

  1. Average lap time (ascending)
  2. Fastest lap time (ascending)
  3. Driver name (alphabetical order, for deterministic results)
* Output the **top three drivers** with their ranking, average lap time, and fastest lap time

---

## Project Structure

```text
coding-interview-405hbmo/
├── data/
│   ├── input/
│   │   └── lap_times.csv
│   └── output/
│       └── top_3_drivers.csv
├── src/
│   └── lap_time_processor.py
└── README.md
```

---

## Implementation Details

### Core Module

All processing logic is implemented in:

```text
src/lap_time_processor.py
```

### Processing Steps

The script performs the following steps:

1. Reads lap time data from a CSV file
2. Aggregates lap times by driver
3. Calculates average and fastest lap times per driver
4. Applies deterministic ranking logic
5. Writes the top three drivers to an output CSV file

---

## Ranking Logic

Drivers are ranked using the following criteria (in order):

1. Average lap time (ascending)
2. Fastest lap time (ascending)
3. Driver name (alphabetical order)

This ensures consistent and reproducible results across executions.

---

## Input Format

The input CSV file must contain the following columns:

| Column | Type   | Description               |
| ------ | ------ | ------------------------- |
| Driver | string | Driver name or identifier |
| Time   | number | Lap time in seconds       |

### Notes

* The CSV file must include a header row
* Lap times must be numeric
* The input file is assumed to be well-formed

**Input file location:**

```text
data/input/lap_times.csv
```

---

## Output

The program generates a CSV file containing the top three drivers ranked by average lap time.

### Output Columns

| Column         | Description      |
| -------------- | ---------------- |
| Position       | Driver rank      |
| Driver         | Driver name      |
| AverageLapTime | Average lap time |
| FastestLapTime | Fastest lap time |

**Output file location:**

```text
data/output/top_3_drivers.csv
```

---

## Logging & Error Handling

* Uses Python’s built-in `logging` module
* Logs key execution steps, including:

  * File reading
  * Statistics calculation
  * Driver ranking
  * Output generation
* Errors such as missing files or invalid data formats are logged and raised

---

## How to Run

### Prerequisites

* Python 3.9 or higher

### Execution

From the project root directory, run:

```bash
python src/lap_time_processor.py
```

Ensure the input file exists at:

```text
data/input/lap_times.csv
```

---

## Assumptions

* Each driver has at least one lap time
* Input data fits in memory
* Lap times are measured in seconds
* Only the top three drivers are required for output


---

**Author:** Vivek Datla
