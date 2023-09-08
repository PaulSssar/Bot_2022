
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from bot_create import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, callback_query
from keyboard import kb_admin
from data_base import sqlite_db
from data_base.sqlite_db import sql_add

#ID ='1151845150'

class FSM_admin(StatesGroup):
    photo = State()
    description = State()
    recipe = State()

async def make_changes (message : types.Message):
    #if ID == message.from_user.id:
        await bot.send_message(message.from_user.id, 'Пиши', reply_markup=kb_admin)
        await message.delete()

async def where_ba(message : types.Message):
    #if message.from_user.id == ID or ID == '1151845150':
        await bot.send_message(message.from_user.id, f'Мы находимся по адресу: г.Ленинск-Кузнецкий пр. Ленина 41 {message.from_user.id}')

async def recipes_start(message : types.Message):
    #if message.from_user.id == ID or ID == '1151845150':
        await FSM_admin.photo.set()
        await message.reply('Загрузи фото')


async def cancel_handler(message : types.Message, state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')



async def load_photo(message : types.Message, state=FSMContext):
    #if message.from_user.id == ID or ID == '1151845150':
        async with state.proxy() as data:
            data['Photo'] = message.photo[0].file_id
        await FSM_admin.next()
        await message.reply('Теперь название')


async def get_description(message :types.Message, state=FSMContext):
    #if message.from_user.id == ID or ID == '1151845150':
        async with state.proxy() as data:
            data['Name'] = message.text
        await FSM_admin.next()
        await message.reply('Ну и теперь сам рецепт')


async def get_recipe(message :types.Message, state=FSMContext):
    #if message.from_user.id == ID or ID == '1151845150':
        async with state.proxy() as data:
            data['Recipe'] = message.text
        await message.reply('Спасибо')
        await sql_add(state)
        await state.finish()


#@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query : types.CallbackQuery):
    await sqlite_db.sql_delete(callback_query.data.replace('del ', ''))
    await callback_query.answer(f'{callback_query.data.replace("del ", "")} удалена', show_alert=True)



async def delete_recipe(message: types.Message):
    #if message.from_user.id == ID or ID == '1151845150':
    read = await sqlite_db.sql_read2()
    for ret in read:
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n{ret[2]}')
        await bot.send_message(message.from_user.id, text='^^^^', reply_markup=InlineKeyboardMarkup()\
            .add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(where_ba, commands='адми')
    dp.register_message_handler(make_changes, commands='админ')
    dp.register_message_handler(recipes_start, commands='Рецепт', state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case = True), state="*")
    dp.register_message_handler(load_photo, content_types='photo', state=FSM_admin.photo)
    dp.register_message_handler(get_description, state=FSM_admin.description)
    dp.register_message_handler(get_recipe, state=FSM_admin.recipe)
    dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del ') )
    dp.register_message_handler(delete_recipe, commands='Удалить')