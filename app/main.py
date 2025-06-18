import asyncio
import logging
import signal
import sys
from uvicorn import Config, Server

from dotenv import load_dotenv

from bot import run_telegram_bot
from server import fastapi

load_dotenv()

logging.basicConfig(level=logging.INFO, format="(%(asctime)s) %(levelname)s %(message)s", datefmt="%m/%d/%y - %H:%M:%S %Z")
logger = logging.getLogger(__name__)

# Function to run FastAPI server
async def run_fastapi():
    config = Config(app=fastapi, host="0.0.0.0", port=8000, loop="asyncio")
    server = Server(config)
    await server.serve()


async def main():
    loop = asyncio.get_running_loop()
    stop_event = asyncio.Event()

    def shutdown():
        print("Shutdown signal received.")
        stop_event.set()

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, shutdown)

    fastapi_task = asyncio.create_task(run_fastapi())
    bot_task = asyncio.create_task(run_telegram_bot())

    await stop_event.wait()

    print("Cancelando tarefas...")
    fastapi_task.cancel()
    bot_task.cancel()

    try:
        await asyncio.gather(fastapi_task, bot_task)
    except asyncio.CancelledError:
        print("Tarefas canceladas com sucesso.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Encerrado pelo usuário.")