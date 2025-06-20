import json
import logging

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)


class APIKeyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, header_name="X-API-Key"):
        super().__init__(app)
        self.header_name = header_name

    async def dispatch(self, request: Request, call_next):
        public_paths = ["/health", "/docs", "/openapi.json"]
        if request.url.path in public_paths:
            return await call_next(request)
        api_key = request.headers.get(self.header_name)
        with open("data/authorized_keys.json", "r+") as f:
            authorized_keys = json.load(f)
        # Validação da chave
        if not api_key or api_key not in authorized_keys.keys():
            return JSONResponse(
                status_code=403, content={"detail": "API Key inválida ou ausente"}
            )

        request.state.key_info = authorized_keys[api_key]

        return await call_next(request)
