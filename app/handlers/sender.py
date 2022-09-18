
from aiogram import types
from aiogram.types.message import ContentType

from dispatcher import bot, dp, db
from app.helper.filters import IsSet


async def aload(msg, cmd, *args, **kwargs):
    f: types.Message = await msg.answer('sending 🔄')
    await cmd(*args, **kwargs)
    await f.edit_text('sent ✅')


@dp.message_handler(
    IsSet(),
    chat_type=[types.ChatType.PRIVATE],
    content_types=[ContentType.TEXT]
)
async def message_text(message: types.Message):
    await aload(
        message,
        bot.send_message,
        db.select(message.from_user.id)[1],
        message.text
    )


@dp.message_handler(
    IsSet(),
    chat_type=[types.ChatType.PRIVATE],
    content_types=[ContentType.PHOTO]
)
async def message_photo(message: types.Message):
    await aload(
        message,
        bot.send_photo,
        db.select(message.from_user.id)[1],
        message.photo[-1].file_id,
        caption=message.caption
    )


@dp.message_handler(
    IsSet(),
    chat_type=[types.ChatType.PRIVATE],
    content_types=[ContentType.VIDEO]
)
async def message_video(message: types.Message):
    video = message.video
    await aload(
        message,
        bot.send_video,
        db.select(message.from_user.id)[1],
        video.file_id,
        caption=message.caption,
        duration=video.duration,
        width=video.width,
        height=video.height,
        thumb=(video.thumb.file_id if video.thumb else None)
    )


@dp.message_handler(
    IsSet(),
    chat_type=[types.ChatType.PRIVATE],
    content_types=[ContentType.VIDEO_NOTE]
)
async def message_video_note(message: types.Message):
    video_note = message.video_note
    await aload(
        message,
        bot.send_video_note,
        db.select(message.from_user.id)[1],
        video_note.file_id,
        duration=video_note.duration,
        length=video_note.length,
        thumb=(video_note.thumb.file_id if video_note.thumb else None)
    )


@dp.message_handler(
    IsSet(),
    chat_type=[types.ChatType.PRIVATE],
    content_types=[ContentType.ANIMATION]
)
async def message_animation(message: types.Message):
    await aload(
        message,
        bot.send_animation,
        db.select(message.from_user.id)[1],
        message.sticker.file_id,
        caption=message.caption
    )


@dp.message_handler(
    IsSet(),
    chat_type=[types.ChatType.PRIVATE],
    content_types=[ContentType.DOCUMENT]
)
async def message_document(message: types.Message):
    document = message.document
    await aload(
        message,
        bot.send_document,
        db.select(message.from_user.id)[1],
        message.document.file_id,
        caption=message.caption,
        thumb=(document.thumb.file_id if document.thumb else None)
    )


@dp.message_handler(
    IsSet(),
    chat_type=[types.ChatType.PRIVATE],
    content_types=[ContentType.STICKER]
)
async def message_sticker(message: types.Message):
    await aload(
        message,
        bot.send_sticker,
        db.select(message.from_user.id)[1],
        message.sticker.file_id
    )


@dp.message_handler(
    IsSet(),
    chat_type=[types.ChatType.PRIVATE],
    content_types=[ContentType.AUDIO]
)
async def message_audio(message: types.Message):
    audio = message.audio
    await aload(
        message,
        bot.send_audio,
        db.select(message.from_user.id)[1],
        audio.file_id,
        caption=message.caption,
        duration=audio.duration,
        performer=audio.performer,
        thumb=(audio.thumb.file_id if audio.thumb else None)
    )


@dp.message_handler(
    IsSet(),
    chat_type=[types.ChatType.PRIVATE],
    content_types=[ContentType.VOICE]
)
async def message_voice(message: types.Message):
    voice = message.voice
    await aload(
        message,
        bot.send_voice,
        db.select(message.from_user.id)[1],
        voice.file_id,
        caption=message.caption,
        duration=voice.duration
    )
