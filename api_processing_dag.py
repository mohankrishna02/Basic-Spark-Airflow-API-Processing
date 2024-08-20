from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 11, 8),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

with DAG(
    "api_processing_dag",
    default_args=default_args,
    description="Spark Complex Data Processing through Airflow"
) as dag:
    run_api_process = BashOperator(
        task_id="open_spark_shell",
        bash_command="spark-submit --master local[*] /home/mohan/airflow/dags/api_processing.py"
    )


    run_api_process
