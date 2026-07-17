import argparse
import time
import sys

from utils.config import load_config
from utils.data_loader import load_data
from utils.processing import process_data
from utils.logger import setup_logger
from utils.metrics import (
    write_success_metrics,
    write_error_metrics,
)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        required=True,
        help="Input CSV file"
    )

    parser.add_argument(
        "--config",
        required=True,
        help="Configuration YAML file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Output metrics JSON"
    )

    parser.add_argument(
        "--log-file",
        required=True,
        help="Log file"
    )

    args = parser.parse_args()

    logger = setup_logger(args.log_file)

    start = time.time()

    version = "v1"

    try:

        config = load_config(args.config)

        version = config["version"]

        logger.info("Configuration loaded.")

        df = load_data(args.input)

        logger.info(f"Loaded {len(df)} rows.")

        processed = process_data(
            df,
            config["window"]
        )

        signal_rate = processed["signal"].mean()

        latency_ms = (time.time() - start) * 1000

        metrics = write_success_metrics(
            args.output,
            version,
            len(processed),
            signal_rate,
            latency_ms,
            config["seed"]
        )

        logger.info("Processing completed successfully.")

        print(metrics)

    except Exception as e:

        logger.error(str(e))

        metrics = write_error_metrics(
            args.output,
            version,
            str(e)
        )

        print(metrics)

        sys.exit(1)


if __name__ == "__main__":
    main()