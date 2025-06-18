

from io import BytesIO
from uuid import uuid4
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BufferedInputFile

from helpers import getenv

TELEGRAM_BOT_API_KEY = getenv("TELEGRAM_BOT_API_KEY")
OWNER_USER_ID = getenv("OWNER_USER_ID")

dp = Dispatcher()
bot = Bot(token=TELEGRAM_BOT_API_KEY, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

async def send_file(buffer: BytesIO, filename: str | None):
    buffer.seek(0)
    input_file = BufferedInputFile(buffer.read(), filename=filename if filename is not None else str(uuid4()) )
    await bot.send_document(chat_id=OWNER_USER_ID, document=input_file)

async def run_telegram_bot():
    await dp.start_polling(bot)
