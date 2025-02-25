from ..bucket import get_minio_client
from dotenv import load_dotenv
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(script_directory, "../envs/minio.env")
load_dotenv(dotenv_path)
try:
    client = get_minio_client()
    if client.bucket_exists(os.getenv("MINIO_BUCKET_NAME")):
        print(f"Bucket {os.getenv('MINIO_BUCKET_NAME')} already exists.")
    else:
        client.make_bucket(os.getenv("MINIO_BUCKET_NAME"))
        print(f"Bucket {os.getenv('MINIO_BUCKET_NAME')} created successfully.")
except Exception as e:
    print(f"Error: {e}")
