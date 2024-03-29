from airflow import DAG
from pendulum import datetime
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="simple_classic_dag",
    start_date=datetime(2023, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:  # assigning the context to an object is mandatory for using dag.test()

    t1 = EmptyOperator(task_id="t1")

if __name__ == "__main__":
    dag.test()