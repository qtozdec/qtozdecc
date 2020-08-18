import random
from  handlers.users.sp import list_playlists
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# # Вариант 1, как в прошлом уроке
# num = ['1', '2', '3', '4']
# buk = ['a', 'b', 'c', 'd']
buk,num = list_playlists()
# buk = list_playlists()

choice = InlineKeyboardMarkup()

for i in range(len(num)):
    button = InlineKeyboardButton(text=num[i], callback_data=buk[i])
    choice.add(button)

# Вариант 2 - с помощью row_width и insert.
# choice = InlineKeyboardMarkup(row_width=2)
#
# buy_pear = InlineKeyboardButton(text="Купить грушу", callback_data=buy_callback.new(item_name="pear", quantity=1))
# choice.insert(buy_pear)
#
# buy_apples = InlineKeyboardButton(text="Купить яблоки", callback_data="buy:apple:5")
# choice.insert(buy_apples)
#
# cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
# choice.insert(cancel_button)

# А теперь клавиатуры со ссылками на товары
# pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Купи тут", url="https://rozetka.com.ua/champion_a00225/p27223057")
#     ]
# ])
# apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Купи тут", url="https://freshmart.com.ua/product/yabloko-gala-116.html")
#     ]
# ])
