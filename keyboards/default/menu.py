from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

favorite = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавление в фавориты"),
        ],
        [
            KeyboardButton(text="Удаление всех фаворитов")
        ],
    ],
    resize_keyboard=True
)

dobudal  = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавление"),
        ],
        [
            KeyboardButton(text="Удаление")
        ],
    ],
    resize_keyboard=True
)
spisok = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Список артистов"),
            KeyboardButton(text="Список плейлистов"),
        ],
        [
            KeyboardButton(text="Список треков в плейлисте"),
            KeyboardButton(text="Список любимых треков")
        ],
    ],
    resize_keyboard=True
)
