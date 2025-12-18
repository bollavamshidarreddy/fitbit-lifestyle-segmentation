"""
test_connection.py
------------------
Purpose:
- To test whether Python can successfully connect to MySQL
- To validate SQLAlchemy engine configuration
- To ensure MySQL Workbench and Python are in sync

WHY THIS FILE IS IMPORTANT:
- Helps catch credential, port, or DB name errors early
- Prevents wasting time later during data loading or EDA
"""

# STAGE 1: Import the DB engine
from db_config import engine


# STAGE 2: Attempt database connection=

try:
    # Using context manager to safely open and close connection
    with engine.connect() as connection:
        print(" SUCCESS: Connected to MySQL database!")

except Exception as e:
    # If connection fails, print the exact error
    print(" ERROR: Failed to connect to the database")
    print("Reason:", e)


