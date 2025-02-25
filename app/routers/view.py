from fastapi import APIRouter, Depends
from app.models import FileDB
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/files", tags=["View"])


@router.get("/files")
async def list_files(db: Session = Depends(get_db)):
    files = db.query(FileDB).all()
    return files
