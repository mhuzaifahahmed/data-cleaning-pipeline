# Automated Data Cleaning Pipeline

A Python pipeline that automatically detects and fixes data quality issues in raw datasets, then generates a cleaning report with visualizations and outputs a clean CSV file.

## Tech Stack
Python, Pandas, Matplotlib, CSV

## What it does
- **Extract:** Loads raw Titanic dataset directly from URL
- **Analyze:** Detects missing values, duplicates, and data quality issues before cleaning
- **Transform:** Fills missing values, removes duplicates, drops unusable columns, standardizes column names
- **Report:** Auto-generates a text report, missing values bar chart, and cleaned CSV file

## Output
- `output/cleaning_report.txt` — full summary of issues found and fixed
- `output/missing_values_chart.png` — bar chart of missing values before cleaning
- `output/titanic_clean.csv` — final cleaned dataset ready for analysis

## How to run
1. Install dependencies: `pip install pandas matplotlib`
2. Run the pipeline: `python pipeline.py`

## Results
- Removed duplicate rows automatically
- Fixed 177 missing Age values using median imputation
- Fixed 2 missing Embarked values using mode imputation
- Dropped Cabin column (77% missing — not recoverable)
- Standardized all column names to lowercase
