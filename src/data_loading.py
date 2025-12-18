import os
import pandas as pd
from db_config import engine

DATA_DIR = "data"

def load_all_csvs():
    for file in os.listdir(DATA_DIR):
        if file.endswith(".csv"):
            table_name = file.replace(".csv", "").lower()
            file_path = os.path.join(DATA_DIR, file)

            df = pd.read_csv(file_path)
            df.to_sql(table_name, engine, if_exists="replace", index=False)

            print(f"Loaded {file} into table {table_name}")

# Run ingestion only when executed directly, not on import
if __name__ == "__main__":
    load_all_csvs()
    print("All CSV files loaded successfully")
