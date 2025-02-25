import io
from fastapi import FastAPI
from app.routers.upload import router as upload_router
from app.routers.view import router as view_router

app = FastAPI()

app.include_router(upload_router)
app.include_router(view_router)


@app.get("/")
def home() -> dict:
    return {"message": "Welcome to the FastAPI application!"}


# def setup_logging():
#     """Sets up logging to a file in the logs/ directory."""
#     log_dir = "logs"
#     if not os.path.exists(log_dir):
#         os.makedirs(log_dir)

#     logging.basicConfig(
#         filename=os.path.join(log_dir, "app.log"),
#         level=logging.INFO,
#         format="%(asctime)s - %(levelname)s - %(message)s",
#         datefmt="%Y-%m-%d %H:%M:%S",
#     )


# setup_logging()


# @app.get("/test_db")
# async def test_db(db: Session = Depends(get_db)):
#     return {"message": "Database connection successful"}


# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
#     try:
#         logging.info(f"Uploading file: {file.filename}")

#         # Read file content into memory
#         contents = await file.read()
#         file_size = len(contents)

#         if file_size == 0:
#             raise ValueError("File is empty")

#         # Upload to MinIO
#         bucket_name = "test"
#         key = f"upload/{file.filename}"
#         file_stream = io.BytesIO(contents)  # Wrap bytes in a file-like object

#         minio_client.put_object(
#             bucket_name, key, file_stream, file_size, content_type=file.content_type
#         )

#         logging.info(f"File uploaded to MinIO: {bucket_name}/{key}, Size: {file_size}")

#         # Save file details to DB
#         file_db = FileDB(filename=file.filename, filepath=key)
#         db.add(file_db)
#         db.commit()
#         db.refresh(file_db)

#         logging.info(f"File entry saved to DB: ID {file_db.id}")
#         return {"message": "File uploaded successfully", "file_id": file_db.id}

#     except Exception as e:
#         logging.error(f"Error uploading file: {e}", exc_info=True)
#         return {"message": str(e)}
