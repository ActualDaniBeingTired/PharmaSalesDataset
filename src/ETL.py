from Extract import extract_data
from Transform import transform_data
from Validate import validate_data
from Load import load_data


def run_pipeline():

    print("================================")
    print("PHARMA SALES ETL PIPELINE")
    print("================================")

    # 1. Extract
    df = extract_data()

    # 2. Transform
    df = transform_data(df)

    # 3. Validate
    validate_data(df)

    # 4. Load
    load_data(df)

    print("\nETL pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()