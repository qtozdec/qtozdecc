from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from keyboards.default import spisok
from loader import dp
from .sp import *
from keyboards.inline.choice_buttons import choice,buk,num

@dp.message_handler(Command("spisok"))
async def show_menu(message: Message):
    await message.answer("Выберите", reply_markup=spisok)


@dp.message_handler(Text(equals=["Список артистов"]))
async def get_food(message: Message):
    await message.answer('\n'.join(list_artists()), reply_markup=ReplyKeyboardRemove())



@dp.message_handler(Text(equals=["Список плейлистов"]))
async def show_items(message: Message):
    await message.answer(text="test",
                         reply_markup=choice)

@dp.callback_query_handler(text = buk)
async def cancel_buying(call: CallbackQuery):
    # Ответим в окошке с уведомлением!
    await call.answer(call.data, show_alert=False)

    # Вариант 1 - Отправляем пустую клваиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(reply_markup=None)

@dp.message_handler(Text(equals=["Список треков в плейлисте"]))
async def get_food(message: Message):
    await message.answer('\n'.join(list_tracks_id('34fYycANN382DA6hQixYNP')), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=["Список любимых треков"]))
async def get_food(message: Message):
    await message.answer('\n'.join(favorite_tracks()), reply_markup=ReplyKeyboardRemove())
