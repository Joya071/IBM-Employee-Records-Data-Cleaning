from src.data_processor import process_csv_file
from src.cleaning import clean_employee_data, save_cleaned_data
from src.database import store_cleaned_data
from src.logger import logger
from src.cli import get_cli_arguments

input_directory = "data"  
df = process_csv_file(input_directory)


if df is not None:
    df = clean_employee_data(df)
    save_cleaned_data(df)  # Save cleaned data to CSV
    print("Data cleaning complete. Cleaned file saved.")

if df is not None:
    df = clean_employee_data(df)  # Clean Data
    store_cleaned_data(df)  # Store in Database
    print("Data successfully stored in the database.")
else:
    logger.warning("No valid data found.")
    print("No valid data found.")
    
    # Get CLI arguments
args = get_cli_arguments()

# Use CLI arguments
input_directory = args.input_dir
database_path = args.db_path

# Process CSV Files
df = process_csv_file(input_directory)

if df is not None:
    df = clean_employee_data(df)  # Data Cleaning
    store_cleaned_data(df, database_path)  # Store in Database
    print(f" Data successfully stored in database: {database_path}")
else:
    print("No valid data found.")