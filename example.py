import datetime

from airflow  import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
  dag_id="young_example_dag",
  start_date=datetime.datetime(2023, 12, 5),
  schedule="@daily"
):
  EmptyOperator(task_id="example_task")
