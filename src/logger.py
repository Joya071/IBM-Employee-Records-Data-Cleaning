import logging
import os

def setup_logger(log_file="logs/processing.log"):
    """
    Setup logging configuration.
    """
    os.makedirs(os.path.dirname(log_file), exist_ok=True)  # Ensure logs folder exists

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,  # Set log level to INFO (Track normal execution)
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    return logging.getLogger(__name__)

logger = setup_logger()
