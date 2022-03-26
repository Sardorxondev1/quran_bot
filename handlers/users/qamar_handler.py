from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.qamar_keybord import (qamar_keybords,
qamar_keybord1,qamar_keybord2,qamar_keybord3,qamar_keybord4)
from keyboards.inline.callback_data import qamar_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Qamar')
async def show_qamar(message: Message):
    await message.answer(f"<b>Qamar surasini oyatlarini tanlang</b>",reply_markup=qamar_keybord1)

@dp.callback_query_handler(qamar_callback_data.filter())
async def show_qamar(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=qamar_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Qamar</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(54,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(54,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Qamar surasini oyatlarini tanlang</b>", reply_markup=qamar_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Qamar surasini oyatlarini tanlang</b>", reply_markup=qamar_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Qamar surasini oyatlarini tanlang</b>", reply_markup=qamar_keybord3)
        elif int(callback_data['items']) <= 55:
            await call.message.answer(f"<b>Qamar surasini oyatlarini tanlang</b>", reply_markup=qamar_keybord4)

    except:
        pass