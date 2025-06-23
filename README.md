# Telegram Chatbot Service

A FastAPI application with an integrated Telegram bot. It exposes HTTP endpoints to send messages or documents to a predefined Telegram user and provides a WebSocket interface for real time chat forwarding.

## Requirements

- **Python**: The project currently targets Python `3.13` in `pyproject.toml`, but it also works on Python `3.12`. Use the latest `3.12` release if `3.13` is not available.
- **Telegram bot token** and owner identifier.

Create a `.env` file in the project root containing the following variables:

```env
TELEGRAM_BOT_API_KEY=YOUR_TELEGRAM_BOT_TOKEN
OWNER_ID=YOUR_TELEGRAM_USER_ID
# optional, defines log file name (dev.log or prod.log)
ENVIRONMENT_MODE=dev
```

The application expects a file `data/authorized_keys.json` with the API keys allowed to call the HTTP endpoints. Example:

```json
{
    "your-secret-key": {"name": "default"}
}
```

Make sure the directories `data/` and `logs/` exist before starting the service. Log files will be written to `logs/dev.log` or `logs/prod.log` according to `ENVIRONMENT_MODE`.

## Running with Docker

You can build and run the Telegram Chatbot Service using Docker for easy deployment.

### Build and run with docker compose

```bash
docker compose -f docker-compose.yml up --build
```

## API Usage

Requests must include the header `X-API-Key` with one of the keys from `authorized_keys.json`.

### Send a message

```bash
curl -X POST http://localhost:8000/send/message \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: your-secret-key' \
  -d '{"message": "Hello"}'
```

### Send a document

```bash
curl -X POST http://localhost:8000/send/document \
  -H 'X-API-Key: your-secret-key' \
  -F 'file=@/path/to/file.pdf'
```

The endpoint `/health` can be used for health checks and `/ws` provides a WebSocket channel to forward bot messages.

## Tests

The repository currently contains a basic HTTP example in `tests/send.http`. Additional automated tests can be added using frameworks such as `pytest`.
