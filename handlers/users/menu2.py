from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import dobudal
from loader import dp
from .sp import *

@dp.message_handler(Command("dobudal"))
async def show_menu(message: Message):
    await message.answer("Выберите", reply_markup=dobudal)


@dp.message_handler(Text(equals=["Добавление"]))
async def get_food(message: Message):
    await message.answer(add_tracks('34fYycANN382DA6hQixYNP','2d1GYLPLxz2fbMoeG3nmDA'), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=["Удаление"]))
async def get_food(message: Message):
    await message.answer(delete_tracks('34fYycANN382DA6hQixYNP','2d1GYLPLxz2fbMoeG3nmDA'), reply_markup=ReplyKeyboardRemove())



