import os
import pandas as pd
import logging
from src.logger import logger
from src.logger import setup_logger  # Logging system import

# Logger setup
logger = setup_logger()

def read_csv_file(file_path):
    """
    Read a single CSV file and return a DataFrame.
    """
    if not os.path.exists(file_path):
        logger.error(f"File {file_path} does not exist.")
        return None

    try:
        df = pd.read_csv(file_path)
        logger.info(f"Successfully read file: {file_path}")
        return df
    except Exception as e:
        logger.error(f"Error reading {file_path}: {e}")
        return None

def process_csv_file(directory, filename="employee_data_raw.csv"):
    """
    Process a single CSV file from the given directory.
    """
    file_path = os.path.join(directory, filename)
    df = read_csv_file(file_path)

    if df is not None:
        logger.info(f"Dataset contains {len(df)} records.")
    return df
