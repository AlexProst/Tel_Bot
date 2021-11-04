from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import URL_Turkmenistan, URL_Bellarus,URL_Afganistan
from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=3)

Afganistan = InlineKeyboardButton(text="в Афганистан", callback_data=buy_callback.new(item_name="Afganistan", quantity=10))
choice.insert(Afganistan)

Turkmenistan = InlineKeyboardButton(text="в Туркменистан", callback_data=buy_callback.new(item_name="Turkmenistan", quantity=3))
choice.insert(Turkmenistan)

Belarus = InlineKeyboardButton(text="в Беларусь", callback_data=buy_callback.new(item_name="Belarus", quantity=5))
choice.insert(Belarus)

cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
choice.insert(cancel_button)

turk_keyboard=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Купи тут", url=URL_Turkmenistan)
        ]
    ])


afgan_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купи тут", url= URL_Afganistan)
    ]
    ])


belarus_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купи тут", url= URL_Bellarus)
    ]
    ])


