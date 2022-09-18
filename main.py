
import asyncio

from aiogram import types

import app
from dispatcher import bot, dp


async def main():
    await bot.set_my_commands([
        types.BotCommand('/set_chat', 'set dist chat')
    ])
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
