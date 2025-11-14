# Synthetic E-Commerce Data Project

This project demonstrates how to work with synthetic e-commerce datasets, load them into an SQLite database using Python, and perform multi-table JOIN operations.  
It includes synthetic CSV data, a Python loader script, SQL queries, and required metadata files.
---

## 📁 Project Structure

ecom-project/  
│  
├── data/  
│   ├── customers.csv  
│   ├── products.csv  
│   ├── orders.csv  
│   ├── order_items.csv  
│   └── payments.csv  
│  
├── load_to_sqlite.py  
├── join_report.sql  
├── requirements.txt  
├── .gitignore  
└── README.md  

---

## 📊 Files Description

### **1. CSV Files (Synthetic E-commerce Data)**
Located in the `data/` directory:
- **customers.csv** – customer details  
- **products.csv** – product catalog  
- **orders.csv** – order transactions  
- **order_items.csv** – item-level order breakdown  
- **payments.csv** – payment status for each order  

These datasets maintain proper foreign key relationships.

---

### **2. load_to_sqlite.py**
This Python script:
- Creates an SQLite database `ecom.db`
- Loads all 5 CSV files into tables
- Uses `pandas` + `sqlite3`
- Replaces tables if they already exist

---

### **3. join_report.sql**
SQL script that:
- Joins customers, orders, order_items, and products
- Produces a detailed purchase report
- Sorts results by order date (DESC)

---

### **4. requirements.txt**
Contains required dependencies:
- `pandas`

---

### **5. .gitignore**
Excludes generated or unnecessary files:
- `__pycache__/`
- `ecom.db`
- `.env`

---

## 🚀 How to Run This Project

### **1. Install Dependencies**
Make sure Python is installed, then run: pip install -r requirements.txt

---

### **2. Load CSV Files into SQLite**
Run the loader script : python load_to_sqlite.py

This will generate `ecom.db` with 5 tables:
- customers  
- products  
- orders  
- order_items  
- payments  

---

### **3. Run the JOIN Query**
To execute the join report:sqlite3 ecom.db < join_report.sql

Or open `ecom.db` using:
- **DB Browser for SQLite**
- **VS Code SQLite extension**

---

## 🎯 Purpose of This Project

This project is ideal for:
- Learning SQL joins  
- Understanding relational database design  
- Practicing SQLite + Python integration  
- Building sample projects for portfolios  
- Data engineering fundamentals  

---

