#  Lakehouse Data Pipeline (Fabric-Inspired)

##  Overview

This project demonstrates an **end-to-end data pipeline** implementing a **Lakehouse architecture (Bronze–Silver–Gold layers)**.
It simulates real-world data engineering workflows inspired by Microsoft Fabric, including data ingestion, transformation, and SQL-based analytics.

---

## Architecture

* **Bronze Layer** → Raw data ingestion
* **Silver Layer** → Data cleaning and transformation
* **Gold Layer** → Data warehouse and analytics

Pipeline Flow:
Raw CSV → Ingestion → Transformation → Warehouse → SQL Analysis

---

## Tech Stack

* Python (Pandas)
* SQL (SQLite)
* Logging
* File-based data storage

---

## Project Structure

```
FabricProject_pipeline/
│
├── data/
│   ├── raw.csv
│   ├── clean.csv
│   ├── warehouse.db
│
├── scripts/
│   ├── ingestion.py
│   ├── transform.py
│   ├── load.py
│   ├── run_pipeline.py
│
├── logs/
│   ├── pipeline.log
│
├── sql/
│   ├── DB_test_SQL.py
│
├── Titanic-Dataset.csv
└── README.md
```

---

##  Pipeline Steps

### 1. Ingestion

* Reads raw dataset
* Stores it in Bronze layer (`data/raw.csv`)

### 2. Transformation

* Handles missing values
* Performs feature engineering
* Encodes categorical variables
* Outputs cleaned data (`data/clean.csv`)

### 3. Loading

* Loads transformed data into SQLite database
* Creates table `titanic_clean`

### 4. Validation

* SQL queries executed to verify data integrity and outputs

---

##  How to Run

### Step 1: Install dependencies

```
pip install pandas
```

### Step 2: Run full pipeline

```
python scripts/run_pipeline.py
```

### Step 3: Verify data

Run SQL test script:

```
python sql/DB_test_SQL.py
```

---

##  Key Learnings

* Built a structured data pipeline using modular scripts
* Implemented Bronze–Silver–Gold architecture
* Performed data transformation and validation
* Handled real-world issues like file path errors and debugging
* Simulated pipeline orchestration similar to enterprise tools

---

##  Future Improvements

* Integrate PySpark for large-scale data processing
* Add incremental data loading
* Deploy pipeline using cloud services
* Integrate with visualization tools (Power BI)

---

##  Summary

This project showcases core **data engineering concepts** including pipeline design, data transformation, and warehouse loading, making it relevant for roles involving modern data platforms and analytics systems.
