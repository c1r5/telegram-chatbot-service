from io import BytesIO
from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from fastapi.openapi.models import APIKey

from bot import send_file
from .auth import validate_api_key

app_instance = FastAPI()

@app_instance.post("/upload")
async def upload_file(file: UploadFile = File(...), _: APIKey = Depends(validate_api_key)):
    try:        
        contents = await file.read()
        buffer = BytesIO(contents)
        await send_file(buffer, file.filename)
    except Exception as e:
        return HTTPException(500, e)

@app_instance.get("/auth")
async def auth_test(api_key: APIKey = Depends(validate_api_key)):
    print(api_key)
    return {"mensagem": "Você está autenticado!"}

@app_instance.get("/health")
async def health_check():
    return {"status": "ok"}