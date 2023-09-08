from  aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types
from bot_create import dp

button1 = KeyboardButton('/Режим_работы')
button6 = KeyboardButton('/Полезные_ссылки')
#button4 = KeyboardButton('Где я?', request_location=True)
#button5 = KeyboardButton('/Мои контакты', request_contact=True)
x = [KeyboardButton('/Расположение'), KeyboardButton('/Хочу_рецепт')]

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(button1).add(button6).add(*x)#.row(button4, button5)

inline_kb = InlineKeyboardMarkup(row_width=1)
url_btn1 = InlineKeyboardButton(text='Колба', url='https://lenkuz.kolba.ru/')
url_btn2 = InlineKeyboardButton(text='Топ_рецептов', url='https://бир.рф/beer_recipes/0-1-2-0-16')

inline_kb.add(url_btn1).add(url_btn2)

#keyboard = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='button', callback_data='1'))

#@dp.message_handler(commands='пуск')
#async def pusk(message : types.Message):
#    await message.answer(text='pusk', reply_markup=keyboard)

#@dp.callback_query_handler(text='1')
#async def callback_test(callback : types.CallbackQuery):
#   await callback.message.answer('молодец')
#   await callback.answer('молодец')