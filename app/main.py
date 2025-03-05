from fastapi import FastAPI
from app.routers.upload import router as upload_router
from app.routers.view import router as view_router

app = FastAPI()

app.include_router(upload_router)
app.include_router(view_router)


@app.get("/")
def home() -> dict:
    return {"message": "Welcome to the FastAPI application!"}
