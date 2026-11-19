def validate_data(df):

    print("\n===== DATA VALIDATION =====")

    # --------------------------------
    # 1. Check empty dataset
    # --------------------------------

    if df.empty:
        raise ValueError("Validation failed: dataset is empty.")

    # --------------------------------
    # 2. Check missing values
    # --------------------------------

    missing_values = df.isnull().sum()

    print("\nMissing values:")
    print(missing_values)

    if missing_values.sum() > 0:
        raise ValueError("Validation failed: missing values detected.")

    # --------------------------------
    # 3. Check duplicates
    # --------------------------------

    duplicate_count = df.duplicated().sum()

    print(f"\nDuplicate rows: {duplicate_count}")

    if duplicate_count > 0:
        raise ValueError("Validation failed: duplicate rows detected.")

    # --------------------------------
    # 4. Check sales values
    # --------------------------------

    negative_sales = (df["sales"] < 0).sum()

    print(f"\nNegative sales values: {negative_sales}")

    if negative_sales > 0:
        raise ValueError("Validation failed: negative sales detected.")

    # --------------------------------
    # 5. Check drug codes
    # --------------------------------

    print("\nDrug codes:")
    print(df["drug_code"].unique())

    # --------------------------------
    # 6. Check dates
    # --------------------------------

    print("\nDate range:")
    print(df["sale_date"].min(), "to", df["sale_date"].max())

    # --------------------------------
    # 7. Check sales statistics
    # --------------------------------

    print("\nSales statistics:")
    print(df["sales"].describe())

    print("\nValidation passed.")

    return True