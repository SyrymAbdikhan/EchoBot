
from aiogram import types
from aiogram.utils.exceptions import MessageCantBeDeleted

from dispatcher import dp, db


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Hello! I\'m echo bot and I will send your messages to another chat. All you have to do is type /set_chat in any chat where I\'m a member and send message to me. And that\'s it. Enjoy!')


@dp.message_handler(commands=['set_chat'])
async def cmd_set_chat(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
        return await message.answer('You can\'t set private chat as dist chat!')

    user = db.select(message.from_user.id)
    if user:
        db.update(message.from_user.id, message.chat.id)
    else:
        db.insert(message.from_user.id, message.chat.id)

    try:
        await message.delete()
    except MessageCantBeDeleted:
        await message.answer('All set!')
