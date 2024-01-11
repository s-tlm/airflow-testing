from airflow import DAG
from airflow.operators.dummy import DummyOperator

dag = DAG(
   dag_id="bad_dag_example",
   schedule_interval=None
)

t1 = DummyOperator(task_id='t1', dag=dag)
t2 = DummyOperator(task_id='t2', dag=dag)
t3 = DummyOperator(task_id='t3', dag=dag)

t1 >> t2 >> t3 >> t1
