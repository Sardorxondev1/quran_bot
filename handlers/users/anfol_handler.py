from loader import dp
from aiogram.types import Message,CallbackQuery
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.anfol_keybord import (anfol_keybords,
    anfol_keybord1,anfol_keybord2,anfol_keybord3,anfol_keybord4,anfol_keybord5
    )
from keyboards.inline.callback_data import anfol_callback_data
import logging
from .surah import oyat_tarjima,oyat_audio

@dp.message_handler(text_contains='Anfol')
async def show_anfol(message: Message):
    await message.answer(f"<b>Anfol surasini oyatlarini tanlang</b>",reply_markup=anfol_keybord1)

@dp.callback_query_handler(anfol_callback_data.filter())
async def show_anfol(call:CallbackQuery,callback_data: dict):
    logging.info(callback_data['items'])
    if callback_data['items'] == 'back1':
        await call.message.delete()
    elif (callback_data['items'].startswith('b') or callback_data['items'].startswith('n')):
        await call.message.edit_reply_markup(reply_markup=anfol_keybords[callback_data['items']])
    else:
        await call.message.answer(f"📖 <b>Anfol</b> surasi <b>{callback_data['items']}-oyat</b>\n \n<i>{oyat_tarjima(8,int(callback_data['items']))}</i>\n")
        await call.message.answer_audio(f"{oyat_audio(8,int(callback_data['items']))}")
        await call.answer(cache_time=60)
        await call.message.delete()
    try:
        if int(callback_data['items']) <= 16:
            await call.message.answer(f"<b>Anfol surasini oyatlarini tanlang</b>", reply_markup=anfol_keybord1)
        elif int(callback_data['items']) <= 32:
            await call.message.answer(f"<b>Anfol surasini oyatlarini tanlang</b>", reply_markup=anfol_keybord2)
        elif int(callback_data['items']) <= 48:
            await call.message.answer(f"<b>Anfol surasini oyatlarini tanlang</b>", reply_markup=anfol_keybord3)
        elif int(callback_data['items']) <= 64:
            await call.message.answer(f"<b>Anfol surasini oyatlarini tanlang</b>", reply_markup=anfol_keybord4)
        elif int(callback_data['items']) <= 75:
            await call.message.answer(f"<b>Anfol surasini oyatlarini tanlang</b>", reply_markup=anfol_keybord5)

    except:
        pass