from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from .database import Base


class FileUpload(BaseModel):
    filename: str
    filepath: str


class File(FileUpload):
    id: int

    class Config:
        from_attributes = True


class FileDB(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(225))
    filepath = Column(String(225))
