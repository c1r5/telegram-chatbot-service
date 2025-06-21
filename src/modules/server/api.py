from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi.middleware import SlowAPIMiddleware

from modules.server.rate_limiter import limiter
from modules.server.middlewares.api_key_middleware import APIKeyMiddleware
from modules.server.controllers.send import send_route


app_instance = FastAPI()

app_instance.state.limiter = limiter
app_instance.add_middleware(SlowAPIMiddleware)
app_instance.add_middleware(APIKeyMiddleware)
app_instance.include_router(send_route)

@app_instance.get("/auth")
async def auth_test():
    return {"mensagem": "Você está autenticado!"}


@app_instance.get("/health")
@limiter.limit("10/minute")
async def health_check(request: Request):
    return {"status": "ok"}

@app_instance.exception_handler(429)
async def rate_limit_exceeded(request: Request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded. Try again later."},
    )
