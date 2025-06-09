# scripts/data_validation.py

import pandas as pd

def validate_data(file_path):
    df = pd.read_csv(file_path)
    # Check for missing values
    missing = df.isnull().sum()
    print("Missing values by column:\n", missing)
    # Basic stats
    print("\nData Summary:")
    print(df.describe())

if __name__ == "__main__":
    validate_data("../data/owid-covid-data.csv")
