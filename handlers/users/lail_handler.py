from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.lail_keybord import (lail_keybords,
                                           lail_keybord1,lail_keybord2)
from keyboards.inline.callback_data import lail_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Lail')
async def show_lail(message: Message):
    await message.answer(f"<b>Lail surasini oyatlarini tanlang</b>",reply_markup=lail_keybord1)

@dp.callback_query_handler(lail_callback_data.filter())
async def show_lail(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=lail_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Lail</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(92,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(92,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Lail surasini oyatlarini tanlang</b>", reply_markup=lail_keybord1)
        elif int(callback_data['items']) <= 21:
            await call.message.answer(f"<b>Lail surasini oyatlarini tanlang</b>", reply_markup=lail_keybord2)

    except:
        pass