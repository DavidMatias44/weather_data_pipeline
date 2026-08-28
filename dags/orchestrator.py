from datetime import datetime, timedelta
from pathlib import Path

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping

from src.main import main

DBT_ROOT_PATH = Path("/opt/airflow/dbt/")
DBT_EXECUTABLE_PATH = "/home/airflow/.local/bin/dbt"

profile_config = ProfileConfig(
    profile_name="weather_profile",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="postgres_conn",
        profile_args={"dbname": "db", "schema": "wdp"}
    ),
)

with DAG(
    dag_id="wdp_orchestrator",
    start_date=datetime(year=2026, month=8, day=20),
    schedule=timedelta(hours=1),
) as dag:
    task1 = PythonOperator(task_id="ETL_process", python_callable=main)

    task2 = DbtTaskGroup(
        group_id="dbt_models",
        project_config=ProjectConfig(DBT_ROOT_PATH / "weather_data_pipeline"),
        profile_config=profile_config,
        execution_config=ExecutionConfig(dbt_executable_path=DBT_EXECUTABLE_PATH),
    )

    task1 >> task2
