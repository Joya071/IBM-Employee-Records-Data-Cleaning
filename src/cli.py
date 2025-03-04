import argparse

def get_cli_arguments():
    """
    Parse command-line arguments for input directory and database location.
    """
    parser = argparse.ArgumentParser(description="IBM Employee Records Data Cleaning Tool")

    # Add arguments
    parser.add_argument(
        "--input_dir", 
        type=str, 
        default="data", 
        help="Path to the directory containing raw employee CSV files."
    )

    parser.add_argument(
        "--db_path", 
        type=str, 
        default="employee_records.db", 
        help="Path to the SQLite database file."
    )

    return parser.parse_args()
