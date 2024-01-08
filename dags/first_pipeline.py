from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago 

with DAG(
        dag_id='...',
        start_date=days_ago(0),
        schedule_interval="@daily", #or use cron '0 0 * * *',
        tags=["..."]
) as dag:
    
    extract = BashOperator(
        task_id="extract_data",
        bash_command='python /opt/airflow/task/extract.py'
    )
    transforms = BashOperator(
        task_id="transform_data",
        bash_command='python /opt/airflow/task/transforms.py'
    )
    load = BashOperator(
        task_id="load_data",
        bash_command='python /opt/airflow/task/load.py'
    )

    extract >> transforms >> load
