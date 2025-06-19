FROM python:3.13-alpine3.22

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

EXPOSE 8000

CMD ["uv", "run", "src/main.py"]
