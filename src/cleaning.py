import pandas as pd
import logging
import re
from src.logger import setup_logger  # Logging system import



def standardize_date_format(df, column="Joining Date"):
    """
    Convert the Joining Date column to standardized format (YYYY-MM-DD).
    """
    try:
        df[column] = pd.to_datetime(df[column], errors='coerce').dt.strftime('%Y-%m-%d')
        logging.info(f"Converted {column} to standardized format.")
    except Exception as e:
        logging.error(f"Error converting {column}: {e}")
    
    return df

def remove_missing_rows(df):
    """
    Remove rows where Employee ID or Name is missing.
    """
    df = df.dropna(subset=["Employee ID", "Name"])
    logging.info("Removed rows with missing Employee ID or Name.")
    return df

def standardize_names(df, column="Name"):
    """
    Ensure Employee Names are properly capitalized (John Doe format).
    """
    df[column] = df[column].str.title()
    logging.info(f"Standardized {column} capitalization.")
    return df

def remove_blank_columns(df):
    """
    Remove completely blank (all null) columns.
    """
    df = df.dropna(axis=1, how="all")
    logging.info("Removed blank columns.")
    return df

def drop_irrelevant_columns(df, columns_to_drop=None):
    """
    Drop columns that are not needed for employee management.
    """
    if columns_to_drop:
        df = df.drop(columns=columns_to_drop, errors="ignore")
        logging.info(f"Dropped irrelevant columns: {columns_to_drop}")
    return df

def convert_numeric_columns(df, columns=["Salary", "Performance Rating"]):
    """
    Convert specified columns to numeric format.
    """
    for column in columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
        logging.info(f"Converted {column} to numeric format.")
    return df

def fill_missing_values(df, columns=["Salary", "Performance Rating"]):
    """
    Fill missing values in specified columns with median.
    """
    for column in columns:
        median_value = df[column].median()
        df[column] = df[column].fillna(median_value)
        logging.info(f"Filled missing values in {column} with median: {median_value}")
    return df



def save_cleaned_data(df, output_path="data/cleaned_employee_data.csv"):
    """
    Save the cleaned DataFrame to a CSV file.
    """
    df.to_csv(output_path, index=False)
    logging.info(f"Cleaned data saved to {output_path}")


def clean_text_columns(df, columns=["Name"]):
    """
    Remove unwanted characters from specified text columns.
    """
    for column in columns:
        df[column] = df[column].astype(str).str.replace(r"[;\"']", "", regex=True).str.strip()
        logging.info(f"Cleaned unwanted characters from {column}")
    return df

def clean_employee_data(df):
    """
    Perform all data cleaning operations on employee dataset.
    """
    df = standardize_date_format(df)
    df = remove_missing_rows(df)
    df = standardize_names(df)
    df = clean_text_columns(df, columns=["Name", "Department"])  
    df = remove_blank_columns(df)
    df = drop_irrelevant_columns(df, columns_to_drop=["Extra Notes", "Address"])
    df = convert_numeric_columns(df)
    df = fill_missing_values(df)
    
    logging.info("Data cleaning complete.")
    return df

