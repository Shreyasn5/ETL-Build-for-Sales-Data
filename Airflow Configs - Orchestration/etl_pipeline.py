from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import json

def transform_data():
    with open("sales_data.json", "r") as f:
        data = json.load(f)

    transformed_data = []
    for record in data:
        transformed_record = {
            'order_id': record['order_id'],
            'amount': round(record['amount'], 2),
            'date': datetime.strptime(record['date'], "%Y-%m-%d %H:%M:%S")
        }
        transformed_data.append(transformed_record)

    with open("transformed_sales_data.json", "w") as f:
        f.write(json.dumps(transformed_data, indent=4))

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG('etl_pipeline', default_args=default_args, schedule_interval='@daily') as dag:
    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    transform_task
