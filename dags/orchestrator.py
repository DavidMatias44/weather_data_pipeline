from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from src.main import main

with DAG(
	dag_id="wdp_orchestrator",
	start_date=datetime(year=2026, month=8, day=20),
	schedule=timedelta(hours=1)
) as dag:
	task1 = PythonOperator(
		task_id="ETL_process",
		python_callable=main
	)

	task1
