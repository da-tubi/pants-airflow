from airflow import Dag

def test_airflow_import():
    dag = Dag(dag_id="dag_id")
    print(dag.dag_id)
