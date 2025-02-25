from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(script_directory, "./envs/minio.env")
load_dotenv(dotenv_path)
minio_client = None


def get_minio_client():
    try:
        global minio_client
        if minio_client is None:
            minio_client = Minio(
                "minio:9000",
                access_key=os.getenv("MINIO_ACCESS_KEY"),
                secret_key=os.getenv("MINIO_SECRET_KEY"),
                secure=False,
            )
        return minio_client
    except S3Error as err:
        print(err)
