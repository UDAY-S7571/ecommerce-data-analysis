"""
load_to_sqlite.py

This script loads synthetic e-commerce CSV datasets into an SQLite database (ecom.db).
It performs the following operations:

1. Connects to SQLite (creates ecom.db if it doesn't exist)
2. Reads 5 CSV files from the 'data' folder:
      - customers.csv
      - products.csv
      - orders.csv
      - order_items.csv
      - payments.csv
3. Creates/overwrites SQLite tables with the same names
4. Uses pandas for CSV reading and sqlite3 for database operations
5. Prints status messages for each loaded table

After execution, ecom.db will contain 5 fully populated tables ready for SQL analysis.
"""


import sqlite3
import pandas as pd

# Connect to SQLite DB
conn = sqlite3.connect("ecom.db")
cursor = conn.cursor()

print("Creating tables and loading data...")

tables = {
    "customers": "customers.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "payments": "payments.csv",
}

for table, filename in tables.items():
    df = pd.read_csv(f"data/{filename}")
    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"Loaded {table}")

print("\nData Loaded Successfully into ecom.db")
conn.close()

