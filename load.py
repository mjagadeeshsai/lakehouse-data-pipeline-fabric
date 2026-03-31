import sqlite3
import pandas as pd
import logging

logging.basicConfig(filename='logs/pipeline.log', level=logging.INFO)

try:
    logging.info("Loading started")

    # Connect to database (creates if not exists)
    conn = sqlite3.connect("data/warehouse.db")

    df = pd.read_csv("data/clean.csv")

    # Load into table
    df.to_sql("titanic_clean", conn, if_exists="replace", index=False)

    conn.close()

    print("Data loaded into warehouse")

    logging.info("Load successful")

except Exception as e:
    print("Error:", e)
    logging.error(str(e))