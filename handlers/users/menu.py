from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import spisok
from loader import dp
from .sp import *


@dp.message_handler(Command("spisok"))
async def show_menu(message: Message):
    await message.answer("Выберите", reply_markup=spisok)


@dp.message_handler(Text(equals=["Список артистов"]))
async def get_food(message: Message):
    await message.answer('\n'.join(list_artists()), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=["Список плейлистов"]))
async def get_food(message: Message):
    await message.answer('\n'.join(list_playlists()), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=["Список треков в плейлисте"]))
async def get_food(message: Message):
    await message.answer('\n'.join(list_tracks_id('34fYycANN382DA6hQixYNP')), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=["Список любимых треков"]))
async def get_food(message: Message):
    await message.answer('\n'.join(favorite_tracks()), reply_markup=ReplyKeyboardRemove())
