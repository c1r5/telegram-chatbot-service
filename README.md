# Telegram Chatbot Service

## Running with Docker

You can build and run the Telegram Chatbot Service using Docker for easy deployment.

### Build the Docker image

```bash
docker build -t telegram-chatbot-service .
```

### Run the Docker container

```bash
docker run -d \
    --name telegram-chatbot-service \
    --env-file .env \
    -p 8000:8000 \
    telegram-chatbot-service
```
