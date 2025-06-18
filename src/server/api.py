from io import BytesIO
from fastapi import FastAPI, File, UploadFile

from bot import send_file


fastapi = FastAPI()

@fastapi.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    buffer = BytesIO(contents)
    await send_file(buffer, file.filename)
    
@fastapi.get("/health")
async def health_check():
    return {"status": "ok"}