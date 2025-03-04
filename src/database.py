import sqlite3
import pandas as pd
import logging
from src.logger import logger


def create_database(db_path="employee_records.db"):
    """
    Create SQLite database and define the schema for employee records.
    """
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table schema
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            Employee_ID TEXT PRIMARY KEY,
            Name TEXT NOT NULL,
            Department TEXT NOT NULL,
            Salary REAL,
            Joining_Date TEXT NOT NULL,
            Performance_Rating REAL
        )
    """)

    conn.commit()
    conn.close()
    logging.info("Database and table created successfully.") 
    
 
def insert_data_into_db(df, db_path="employee_records.db"):
    """
    Insert cleaned employee data into SQLite database.
    """
    conn = sqlite3.connect(db_path)
    
    df.to_sql("employees", conn, if_exists="replace", index=False)
    
    conn.commit()
    conn.close()
    logging.info("Cleaned data inserted into database successfully.")

def store_cleaned_data(df, db_path="employee_records.db"):
    """
    Create database, define schema, and insert cleaned data.
    """
    create_database(db_path)  # Step 1: Database & Table Create
    insert_data_into_db(df, db_path)  # Step 2: Data Insert

    logging.info("Data storage process completed.")
