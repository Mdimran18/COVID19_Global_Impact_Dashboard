# Preprocessing Script Example

import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.fillna(method='ffill')
    df = df.dropna()
    return df
