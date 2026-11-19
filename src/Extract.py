import pandas as pd


def extract_data():

    file_path = "/opt/airflow/data/raw/salesdaily.csv"

    df = pd.read_csv(file_path)

    print("Data successfully extracted.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    return df