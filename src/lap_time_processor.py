import csv
import logging
from collections import defaultdict
from typing import Dict, List, TypedDict

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger(__name__)

# Static Type Safety
class DriverStats(TypedDict):
    driver: str
    average_time: float
    fastest_time: float


def read_lap_data(file_path: str) -> Dict[str, List[float]]:
    """ Read lap times from a CSV file and group them by driver. 
    Args: file_path (str): Path to the input CSV file. 
    Returns: Dict[str, List[float]]: Mapping of driver name to list of lap times. """    
    logger.info("Reading lap data from file: %s", file_path)

    lap_times = defaultdict(list)

    try:
        with open(file_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                lap_times[row["Driver"]].append(float(row["Time"]))

        logger.info(
            "Successfully read lap data for %d drivers",
            len(lap_times)
        )

    except FileNotFoundError:
        logger.exception("Input file not found: %s", file_path)
        raise
    except (KeyError, ValueError) as e:
        logger.exception("Invalid data format in input file")
        raise

    return lap_times


def calculate_driver_statistics(
    lap_times: Dict[str, List[float]]
) -> List[DriverStats]:
    """ Calculate average and fastest lap time for each driver. 
    Args: lap_times (Dict[str, List[float]]): Driver lap times. 
    Returns: List[dict]: List of driver statistics. """    
    logger.info("Calculating driver statistics")

    stats: List[DriverStats] = []

    for driver, times in lap_times.items():
        stats.append({
            "driver": driver,
            "average_time": round(sum(times) / len(times), 3),
            "fastest_time": round(min(times), 3)
        })

    logger.info(
        "Calculated statistics for %d drivers",
        len(stats)
    )

    return stats
    
def get_top_drivers(
    driver_stats: List[DriverStats],
    top_n: int = 3
) -> List[DriverStats]:
    """ Gives the Top N drivers based on average_time
    Takes care of ties based on on fastest lap. 
    Args: lap_times (Dict[str, List[float]]): Driver lap times. 
    Returns: List[dict]: List of driver statistics. """       
    logger.info(
        "Selecting top %d drivers with tie-breaking rules",
        top_n
    )

    sorted_drivers = sorted(
        driver_stats,
        key=lambda x: (
            x["average_time"],
            x["fastest_time"],
            x["driver"]
        )
    )

    top_drivers = sorted_drivers[:top_n]

    for idx, driver in enumerate(top_drivers, start=1):
        logger.info(
            "Position %d: %s (Avg: %.3f, Fastest: %.3f)",
            idx,
            driver["driver"],
            driver["average_time"],
            driver["fastest_time"]
        )

    return top_drivers



def write_data_to_csv(
    drivers: List[DriverStats],
    output_file: str
) -> None:
    logger.info("Writing top drivers to output file: %s", output_file)

    try:
        with open(output_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Position", "Driver", "AverageLapTime", "FastestLapTime"]
            )

            for position, driver in enumerate(drivers, start=1):
                writer.writerow([
                    position,
                    driver["driver"],
                    driver["average_time"],
                    driver["fastest_time"]
                ])

        logger.info(
            "Successfully wrote %d records to output file",
            len(drivers)
        )

    except Exception:
        logger.exception("Failed to write output CSV file")
        raise


def main() -> None:
    logger.info("Starting Formula 1 lap time batch processor")

    input_file = "data/input/lap_times.csv"
    output_file = "data/output/top_3_drivers.csv"

    lap_times = read_lap_data(input_file)
    driver_stats = calculate_driver_statistics(lap_times)
    top_drivers = get_top_drivers(driver_stats)
    write_data_to_csv(top_drivers, output_file)

    logger.info("Batch processing completed successfully")


if __name__ == "__main__":
    main()