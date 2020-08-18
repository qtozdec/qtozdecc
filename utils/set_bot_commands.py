from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("new_tracks", "Треки за сегодня"),
        types.BotCommand("delete", "Удаление треков"),
        types.BotCommand("add", "Добавление треков"),

    ])