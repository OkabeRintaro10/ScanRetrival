import io
from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from app.database import get_db
from app.bucket import get_minio_client
from app.models import FileDB

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/Upload")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    file_size = len(contents)

    if file_size == 0:
        raise ValueError("File is empty")
    try:
        key = f"upload/{file.filename}"
        file_stream = io.BytesIO(contents)
        minio_client = get_minio_client()
        minio_client.put_object(
            "test", key, file_stream, file_size, content_type=file.content_type
        )

        file_db = FileDB(filename=file.filename, filepath=key)
        db.add(file_db)
        db.commit()
        db.refresh(file_db)
        return {"message": "File uploaded successfully", "file_id": file_db.id}

    except Exception as e:
        return {"message": str(e)}
