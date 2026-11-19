import pandas as pd


def transform_data(df):

    print("\n===== TRANSFORMATION =====")

    # Make a copy
    df = df.copy()

    # --------------------------------
    # 1. Convert date
    # --------------------------------

    df["datum"] = pd.to_datetime(df["datum"])

    print("Date converted successfully.")

    # --------------------------------
    # 2. Identify drug columns
    # --------------------------------

    drug_columns = [
        "M01AB",
        "M01AE",
        "N02BA",
        "N02BE",
        "N05B",
        "N05C",
        "R03",
        "R06"
    ]

    # --------------------------------
    # 3. Convert wide format to long format
    # --------------------------------

    df = df.melt(
        id_vars=[
            "datum",
            "Year",
            "Month",
            "Hour",
            "Weekday Name"
        ],
        value_vars=drug_columns,
        var_name="drug_code",
        value_name="sales"
    )

    # --------------------------------
    # 4. Rename columns
    # --------------------------------

    df = df.rename(columns={
        "datum": "sale_date",
        "Year": "year",
        "Month": "month",
        "Hour": "hour",
        "Weekday Name": "weekday"
    })

    # --------------------------------
    # 5. Remove duplicate rows
    # --------------------------------

    df = df.drop_duplicates()

    # --------------------------------
    # 6. Sort data
    # --------------------------------

    df = df.sort_values(
        by=["sale_date", "drug_code"]
    ).reset_index(drop=True)

    print("Wide format converted to long format.")

    print("\nTransformed columns:")
    print(df.columns.tolist())

    print("\nTransformed shape:")
    print(df.shape)

    print("\nFirst 5 transformed rows:")
    print(df.head())

    return df