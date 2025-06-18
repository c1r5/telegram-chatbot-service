FROM python:3.13-alpine3.22

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY . /app


EXPOSE 8000

RUN uv sync --locked
CMD ["uv", "run", "src/main.py"]
