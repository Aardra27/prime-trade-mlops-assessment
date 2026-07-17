import logging


def setup_logger(log_file):
    """
    Configure application logger.
    """

    logger = logging.getLogger("mlops_logger")
    logger.setLevel(logging.INFO)

    # Remove existing handlers to avoid duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger