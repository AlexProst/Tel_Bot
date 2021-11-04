import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, turk_keyboard, afgan_keyboard, belarus_keyboard
from loader import dp, bot



@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text='На выбор предлагаем три горячих тура.\n'
                         'Если вам ничего не нужно - жмите "Отмена"',
                         reply_markup=choice)

@dp.callback_query_handler(buy_callback.filter(item_name='Turkmenistan'))
async def buying_Turkmenistan (call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{callback_data=}")
    quantity = callback_data.get("quantity")

    await call.message.answer(f'Вы выбрали билет в Туркменистан. Билетов всего {quantity}. Счастиловго пути!',
                              reply_markup=turk_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name='Belarus'))
async def buying_Belarus (call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{callback_data=}")
    quantity = callback_data.get("quantity")

    await call.message.answer(f'Вы выбрали билет в Беларусь. Билетов осталось {quantity}. Счастиловго пути!',
                              reply_markup=belarus_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name='Afganistan'))
async def buying_Afganistan (call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{callback_data=}")
    quantity = callback_data.get("quantity")

    await call.message.answer(f'Вы выбрали билет в Афганистан. Счастиловго пути! {quantity}.',
                              reply_markup=afgan_keyboard)

@dp.callback_query_handler(text='cancel')
async def cancel_buying(call: CallbackQuery):
    await call.answer('Может быть в другой раз...', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)