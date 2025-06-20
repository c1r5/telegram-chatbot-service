from fastapi import FastAPI
from auth import APIKeyMiddleware
from controllers import send_router

app_instance = FastAPI()

app_instance.add_middleware(APIKeyMiddleware)
app_instance.include_router(send_router)


@app_instance.get("/auth")
async def auth_test():
    return {"mensagem": "Você está autenticado!"}


@app_instance.get("/health")
async def health_check():
    return {"status": "ok"}
