
from aiogram import types
from aiogram.dispatcher.filters import Filter

from dispatcher import db


class IsSet(Filter):
    async def check(self, message: types.Message):
        chat_id = db.select(message.from_user.id)
        if not chat_id:
            await message.answer('Set chat first! Use command /set_chat')
            return False
        return True
