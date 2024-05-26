from datetime import datetime, timedelta
import pandas as pd
from minio import Minio
from io import BytesIO
from airflow.decorators import dag, task
import os

# Constants and Configuration
MINIO_URL = os.getenv("MINIO_URL")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
MINIO_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME")
IMDB_DATA_PATH = "/opt/airflow/data/imdb_dataset.csv"

default_args = {
    'owner': 'yvoievid',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

@task
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

@task
def dump_data_to_bucket(dataset: pd.DataFrame):
    csv = dataset.to_csv(index=False).encode("utf-8")
    client = Minio(MINIO_URL, access_key=MINIO_ACCESS_KEY, secret_key=MINIO_SECRET_KEY, secure=False)

    if not client.bucket_exists(MINIO_BUCKET_NAME):
        client.make_bucket(MINIO_BUCKET_NAME)
    else:
        print(f"Bucket '{MINIO_BUCKET_NAME}' already exists!")

    client.put_object(
        MINIO_BUCKET_NAME, "imdb_dataset.csv", data=BytesIO(csv), length=len(csv), content_type="application/csv"
    )

@dag(
    schedule="0 */2 * * *",
    start_date=datetime(2022, 12, 26),
    catchup=False,
    tags=["imdb", "etl"],
    default_args=default_args,
)
def imdb_etl():
    data = load_data(IMDB_DATA_PATH)
    dump_data_to_bucket(data)

imdb_etl()
