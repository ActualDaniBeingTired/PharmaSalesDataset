from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

import sys

sys.path.append("/opt/airflow/src")

from ETL import run_pipeline


with DAG(
    dag_id="pharma_sales_etl",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    max_active_runs=1,
    tags=["pharma", "etl", "data-engineering"],
) as dag:

    run_etl = PythonOperator(
        task_id="run_pharma_etl",
        python_callable=run_pipeline,
    )