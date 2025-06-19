from fastapi.security import APIKeyHeader
from fastapi import HTTPException, Depends

API_KEY_NAME = "X-API-Key"
API_KEY_HEADER = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def validate_api_key(api_key_header: str = Depends(API_KEY_HEADER)):
    if api_key_header == "84a31499-0294-4706-aca0-e707d1e91f7c":
        return api_key_header
    raise HTTPException(status_code=403, detail="Chave inválida")