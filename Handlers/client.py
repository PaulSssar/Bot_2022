from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from bot_create import bot, dp

from keyboard import kb_client, inline_kb

from data_base import sqlite_db

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приветствую Вас! Я - бот магазина "Колба" в городе Ленинск-Кузнецкий.', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Давайте пообщаемся через личные сообщения:\nhttps://t.me/Kolba_lk_bot.')

async def when_open(message : types.Message):
    await bot.send_message(message.from_user.id, 'Мы работаем по будням: с 10-00 до 19-00. По выхлдным: с 10 до 16. Ждем вас!')


async def where_kolba(message : types.Message):
    await bot.send_message(message.from_user.id, 'Мы находимся по адресу: г.Ленинск-Кузнецкий пр. Ленина 41')

async def get_recipe(message : types.Message):
    await sqlite_db.sql_read(message)

async  def get_urls(message : types.Message):
    await message.answer('Ссылки', reply_markup=inline_kb)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_start, Text(equals='Привет', ignore_case=True), state = "*")
    dp.register_message_handler(when_open, commands=['Режим_работы'])
    dp.register_message_handler(where_kolba, commands=['Расположение'])
    dp.register_message_handler(get_recipe, commands=['Хочу_рецепт'])
    dp.register_message_handler(get_urls, commands=['Полезные_ссылки'])
