# IBM Employee Records Data Cleaning

## Project Overview

IBM's HR department maintains employee records that contain **inconsistent, missing, or incorrectly formatted data**.  
This tool automates the **data cleaning process** using Python, `pandas`, and `sqlite3` and stores the cleaned records in an **SQLite database**.

## 🎯 Features

Reads employee records from CSV files  
 Cleans & standardizes the data (fixes dates, removes blanks, fills missing values)  
 Stores cleaned data in an SQLite database  
 Implements logging to track execution & errors  
 Provides a CLI tool to specify input directory & database path

## Installation

```sh
git https://github.com/Joya071/IBM-Employee-Records-Data-Cleaning.git
cd ibm-employee-cleaning
pip install -r requirements.txt
c
```
