import json
import string

from aiogram import types, Dispatcher



async def cenz(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Нецензурный текст')
        await message.delete()


def register_handlers_commons(dp : Dispatcher):
    dp.register_message_handler(cenz)