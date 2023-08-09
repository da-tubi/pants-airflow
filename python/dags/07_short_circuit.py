from __future__ import annotations

from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule
from airflow.exceptions import AirflowSkipException
from airflow.exceptions import AirflowFailException
import pprint


dag_args = {
    'owner': 'da',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'params': {
        "branch": "empty_task_2"
    },
}

def t1_callable(**context):
    if context["data_interval_start"].day % 2 == 0:
        raise AirflowFailException()

def t2_callable(**context):
    if context["data_interval_start"].day % 3 == 0:
        raise AirflowFailException()

def t3_callable(**context):
    if context["data_interval_start"].day % 4 == 0:
        raise AirflowFailException()

with DAG(dag_id="short_circuit", default_args=dag_args) as dag:
    t1 = PythonOperator(task_id="t1", python_callable=t1_callable)
    t2 = PythonOperator(task_id="t2", python_callable=t2_callable, trigger_rule=TriggerRule.ONE_FAILED)
    t3 = PythonOperator(task_id="t3", python_callable=t3_callable, trigger_rule=TriggerRule.ONE_FAILED)
    end = EmptyOperator(task_id="end", trigger_rule=TriggerRule.ONE_SUCCESS)
    t1 >> t2 >> t3
    t1 >> end
    t2 >> end
    t3 >> end

