from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.default import keyboard_add
from loader import dp
from .sp import *
from keyboards.inline.callback_datas import my_call
from keyboards.inline.choice_buttons import choice, choice1


@dp.message_handler(Command("add"))
async def show_menu(message: Message):
    await message.answer("Выберите", reply_markup=keyboard_add)


@dp.message_handler(Text(equals=["Добавление в фавориты"]))
async def get_food(message: Message):
    await message.answer('Выберите плейлист для обновления', reply_markup=choice)


@dp.callback_query_handler(my_call.filter(method="favorite"))
async def add_favorite(call: CallbackQuery, callback_data: dict):
    await call.message.answer(add_to_favorite_tracks(callback_data['playlist']),
                              reply_markup=ReplyKeyboardRemove())
    await call.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(Text(equals=["Добавление треков"]))
async def add(message: Message):
    await message.answer('Выберите плейлист для обновления', reply_markup=choice1)


@dp.callback_query_handler(my_call.filter(method="add_tracks1"))
async def add_tracks(call: CallbackQuery, callback_data: dict):
    # k =
    await call.message.answer(add_tracksc(callback_data['playlist'], '34fYycANN382DA6hQixYNP'),
                              reply_markup=ReplyKeyboardRemove())
    await call.message.edit_reply_markup(reply_markup=None)


@dp.message_handler(text="Назад")
async def get_food(message: Message):
    await message.answer('Назад', reply_markup=ReplyKeyboardRemove())
