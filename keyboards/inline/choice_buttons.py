from handlers.users.sp import list_playlists
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import my_call

playlists_id, playlist = list_playlists()

choice = InlineKeyboardMarkup()
choice1 = InlineKeyboardMarkup()
choice2 = InlineKeyboardMarkup()
choice3 = InlineKeyboardMarkup()
cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")

for i in range(len(playlist)):
    button_add_favorite = InlineKeyboardButton(text=playlist[i],
                                               callback_data=my_call.new(playlist=playlists_id[i], method="favorite"))
    button_add_tracks = InlineKeyboardButton(text=playlist[i],
                                             callback_data=my_call.new(playlist=playlists_id[i], method="add_tracks1"))
    button_add_tracks2 = InlineKeyboardButton(text=playlist[i],
                                              callback_data=my_call.new(playlist=playlists_id[i], method="add_tracks2"))
    button_delete_tracks = InlineKeyboardButton(text=playlist[i],
                                                callback_data=my_call.new(playlist=playlists_id[i],
                                                                          method="delete_tracks1"))
    choice.add(button_add_favorite, cancel_button)
    choice1.add(button_add_tracks, cancel_button)
    choice2.add(button_delete_tracks, cancel_button)
    choice3.add(button_add_tracks2,cancel_button)

