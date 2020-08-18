from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.default import keyboard_delete
from loader import dp
from .sp import *
from keyboards.inline.choice_buttons import choice2
from keyboards.inline.callback_datas import my_call


@dp.message_handler(Command("delete"))
async def show_menu(message: Message):
    await message.answer("Выберите", reply_markup=keyboard_delete)


@dp.message_handler(Text(equals=["Удаление всех фаворитов"]))
async def get_food(message: Message):
    await message.answer(delete_favorite_tracks(), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=["Удаление треков"]))
async def add(message: Message):
    await message.answer('Выберите плейлист для обновления', reply_markup=choice2)


@dp.callback_query_handler(my_call.filter(method="delete_tracks1"))
async def add_tracks(call: CallbackQuery, callback_data: dict):
    await call.message.answer(delete_tracksc(callback_data['playlist'], '34fYycANN382DA6hQixYNP'),
                              reply_markup=ReplyKeyboardRemove())
    await call.message.edit_reply_markup(reply_markup=None)
