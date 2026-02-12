import logging
import os


def setup_logger():
    """
    Configure and return a logger instance.
    Logs will be written to trading.log file.
    """

    log_file = "trading.log"

    # Create logger
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if logger.hasHandlers():
        return logger

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger