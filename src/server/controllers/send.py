from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from io import BytesIO
from bot import send_file

send_router = APIRouter(prefix="/send")


@send_router.post("/document")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        buffer = BytesIO(contents)
        await send_file(buffer, file.filename)
        return JSONResponse(status_code=200, content={"status": "ok"})
    except Exception as e:
        return HTTPException(500, e)
