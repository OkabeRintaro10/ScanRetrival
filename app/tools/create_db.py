from app.models import Base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(script_directory, "../envs/db.env")
load_dotenv(dotenv_path)

Base.metadata.create_all(
    bind=create_engine(
        "mysql+pymysql://{}:{}@172.19.0.2:3306/{}".format(
            os.getenv("MYSQL_USER"),
            os.getenv("MYSQL_PASSWORD"),
            os.getenv("MYSQL_DATABASE"),
        ),
        pool_pre_ping=True,
        echo=True,
    )
)
