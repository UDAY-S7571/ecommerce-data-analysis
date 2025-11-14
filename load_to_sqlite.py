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
