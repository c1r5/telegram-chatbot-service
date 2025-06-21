from fastapi import APIRouter, Request, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from io import BytesIO

from modules.bot import send_file
from modules.server.rate_limiter import limiter

send_route = APIRouter(prefix="/send")

@send_route.post("/document")
@limiter.limit("5/minute")
async def upload_file(request: Request, file: UploadFile = File(...)):
    try:
        contents = await file.read()
        buffer = BytesIO(contents)
        await send_file(buffer, file.filename)
        return JSONResponse(status_code=200, content={"status": "ok"})
    except Exception as e:
        return HTTPException(500, e)
