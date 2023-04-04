from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

dag_args = {
    'owner': 'da',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    dag_id='demo_dag',
    default_args=dag_args,
    schedule_interval='@daily',
)

task = BashOperator(
    task_id='my_task',
    bash_command='date',
    dag=dag
)

task
