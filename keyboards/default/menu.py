from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_add = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавление в фавориты"),
        ],
        [
            KeyboardButton(text="Добавление треков"),
        ],
        [
            KeyboardButton(text="Назад"),
        ],
        ],
    resize_keyboard=True
)

keyboard_delete = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Удаление всех фаворитов")
        ],
        [
            KeyboardButton(text="Удаление треков")
        ],
        [
            KeyboardButton(text="Назад"),
        ],
    ],
    resize_keyboard=True
)
