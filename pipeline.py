import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

def extract():
    print("Extracting data...")
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    return df

def analyze_problems(df):
    print("\nAnalyzing data quality...")
    report = {}
    report["total_rows"] = len(df)
    report["duplicate_rows"] = df.duplicated().sum()
    report["missing_values"] = df.isnull().sum().to_dict()
    report["total_missing"] = df.isnull().sum().sum()
    return report

def transform(df):
    print("\nCleaning data...")
    df = df.drop_duplicates()
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    df = df.drop(columns=["Cabin"])
    df.columns = [col.lower().strip() for col in df.columns]
    return df

def generate_report(report, df_clean):
    print("\nGenerating report...")
    os.makedirs("output", exist_ok=True)
    
    missing = {k: v for k, v in report["missing_values"].items() if v > 0}
    if missing:
        plt.figure(figsize=(8, 4))
        plt.bar(missing.keys(), missing.values(), color="salmon")
        plt.title("Missing Values by Column (Before Cleaning)")
        plt.xlabel("Column")
        plt.ylabel("Missing Count")
        plt.tight_layout()
        plt.savefig("output/missing_values_chart.png")
        plt.close()

    with open("output/cleaning_report.txt", "w") as f:
        f.write("DATA CLEANING REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Total Rows: {report['total_rows']}\n")
        f.write(f"Duplicate Rows Found & Removed: {report['duplicate_rows']}\n")
        f.write(f"Total Missing Values Found: {report['total_missing']}\n\n")
        f.write("Missing Values Per Column:\n")
        for col, count in report["missing_values"].items():
            if count > 0:
                f.write(f"  {col}: {count} missing\n")
        f.write(f"\nClean Dataset Shape: {df_clean.shape[0]} rows x {df_clean.shape[1]} columns\n")

    df_clean.to_csv("output/titanic_clean.csv", index=False)
    print("Report saved to output/cleaning_report.txt")
    print("Clean data saved to output/titanic_clean.csv")
    print("Chart saved to output/missing_values_chart.png")

if __name__ == "__main__":
    df_raw = extract()
    report = analyze_problems(df_raw)
    df_clean = transform(df_raw)
    generate_report(report, df_clean)
    print("\nData Cleaning Pipeline completed successfully!")