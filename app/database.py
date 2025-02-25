from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(script_directory, "./envs/db.env")
load_dotenv(dotenv_path)

dbUrl = "mysql+pymysql://{}:{}@{}/{}".format(
    os.getenv("MYSQL_USER"),
    os.getenv("MYSQL_PASSWORD"),
    os.getenv("DB_HOST"),
    os.getenv("MYSQL_DATABASE"),
)

engine = create_engine(dbUrl, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
