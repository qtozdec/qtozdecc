from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import favorite
from loader import dp
from .sp import *

@dp.message_handler(Command("favorite"))
async def show_menu(message: Message):
    await message.answer("Выберите", reply_markup=favorite)


@dp.message_handler(Text(equals=["Добавление в фавориты"]))
async def get_food(message: Message):
    await message.answer(add_to_favorite_tracks('2d1GYLPLxz2fbMoeG3nmDA'), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=["Удаление всех фаворитов"]))
async def get_food(message: Message):
    await message.answer(delete_favorite_tracks(), reply_markup=ReplyKeyboardRemove())