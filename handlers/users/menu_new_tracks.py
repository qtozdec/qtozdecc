from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from .sp import *

@dp.message_handler(Command("new_tracks"))
async def show_menu(message: Message):
    await message.answer(add_new_release(list_artists()))




