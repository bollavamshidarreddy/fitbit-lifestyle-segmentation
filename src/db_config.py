"""
db_config.py
-------------
This module creates a reusable SQLAlchemy engine to connect
Python with the MySQL database.

WHY THIS FILE EXISTS:
- To centralize database connection logic
- To avoid hardcoding credentials
- To allow all team members to run the project locally
- To keep SQL execution consistent across the project
"""
# STAGE 1: Import required modules

# SQLAlchemy is used as the database abstraction layer
# It allows Python to communicate with MySQL using SQL
from sqlalchemy import create_engine

# os is used to read environment variables securely
import os

# load_dotenv loads variables from .env file into the system environment
from dotenv import load_dotenv


# STAGE 2: Load environment variables (.env)

# This reads the .env file present in the project root
# Without this, os.getenv() will return None
load_dotenv()



# STAGE 3: Read database credentials

# Each variable is fetched from .env
# This avoids exposing credentials in the source code

DB_USER = os.getenv("DB_USER")        # MySQL username
DB_PASSWORD = os.getenv("DB_PASSWORD")  # MySQL password
DB_HOST = os.getenv("DB_HOST")        # Host (usually localhost)
DB_PORT = os.getenv("DB_PORT")        # Port (default 3306)
DB_NAME = os.getenv("DB_NAME")        # Database name


# STAGE 4: Create SQLAlchemy engine (Core Component)

# This engine is the bridge between Python and MySQL
# Format:
# mysql+pymysql://username:password@host:port/database

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    echo=False  # Set to True only if you want to see SQL logs
)


# STAGE 5: Why we STOP here

#  We do NOT connect here
#  We do NOT execute SQL here
# We do NOT load data here
#
# This file only DEFINES the engine.
# Other files will IMPORT and USE this engine.
