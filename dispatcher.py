
import os
import logging

from dotenv import load_dotenv
load_dotenv()

from aiogram import Bot
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher

from app.helper.db import DB

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    level=logging.INFO,
)

bot = Bot(token=os.environ['BOT_TOKEN'])
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

db = DB()
