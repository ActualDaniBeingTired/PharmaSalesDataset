import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


def load_data(df):

    print("\n===== LOADING DATA =====")

    # Load environment variables
    load_dotenv()

    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    # PostgreSQL connection
    connection_string = (
        f"postgresql+psycopg2://"
        f"{db_user}:{db_password}@"
        f"{db_host}:{db_port}/{db_name}"
    )

    engine = create_engine(connection_string)

    # --------------------------------
    # 1. Load staging table
    # --------------------------------

    df.to_sql(
        "fact_sales",
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{len(df)} rows loaded into staging table.")

    # --------------------------------
    # 2. Populate dim_drug
    # --------------------------------

    with engine.begin() as connection:

        connection.execute(text("""
            INSERT INTO dim_drug (drug_code)
            SELECT DISTINCT drug_code
            FROM fact_sales
            ON CONFLICT (drug_code)
            DO NOTHING;
        """))

    print("dim_drug updated.")

    # --------------------------------
    # 3. Populate dim_date
    # --------------------------------

    with engine.begin() as connection:

        connection.execute(text("""
            INSERT INTO dim_date (
                date,
                year,
                month,
                weekday
            )
            SELECT DISTINCT
                sale_date,
                year,
                month,
                weekday
            FROM fact_sales
            ON CONFLICT (date)
            DO NOTHING;
        """))

    print("dim_date updated.")

    # --------------------------------
    # 4. Rebuild fact_sales_dw
    # --------------------------------

    with engine.begin() as connection:

        connection.execute(text("""
            DELETE FROM fact_sales_dw;
        """))

        connection.execute(text("""
            INSERT INTO fact_sales_dw (
                date_id,
                drug_id,
                hour,
                sales
            )
            SELECT
                d.date_id,
                dr.drug_id,
                f.hour,
                f.sales
            FROM fact_sales f
            JOIN dim_date d
                ON f.sale_date = d.date
            JOIN dim_drug dr
                ON f.drug_code = dr.drug_code;
        """))

    print("fact_sales_dw rebuilt.")

    print(f"{len(df)} rows loaded into data warehouse.")