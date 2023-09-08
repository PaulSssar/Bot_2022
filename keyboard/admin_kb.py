from  aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

button1 = KeyboardButton('/Рецепт')
button2 = KeyboardButton('/отмена')
button3 = KeyboardButton('/Удалить')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)

kb_admin.add(button1).add(button2).add(button3)