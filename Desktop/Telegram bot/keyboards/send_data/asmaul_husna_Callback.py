from aiogram.types import Message, CallbackQuery

from loader import dp
from keyboards.default.asmaul_husna_menu import ismlarMenu
from keyboards.inline.Asmaul_HusnaInline import ismlarinline1, ismlarinline2, ismlarinline3, ismlarinline4, ismlarinline5, ismlarinline10, ismlarinline6, ismlarinline7, ismlarinline8, ismlarinline9
from keyboards.default.location_button import Keyboard

@dp.message_handler(text='Asmaul Husna')
async def send_link(message: Message):
    await message.answer(""""<b>Alloh, deb chorlangiz, yoki Rahmon – Mehribon, deb chorlangiz. Qanday chorlasangizlarda (joizdir). Zero, U zotning goʻzal ismlari bordir"</b>("Al-isro" surasi, 110-oyat).""", reply_markup=ismlarMenu,parse_mode="html")

@dp.message_handler(text='Ma\'nolari')
async def follow_inline(msg: Message):
    await msg.answer("Allohning go'zal ismlarining ma'nolari", reply_markup=ismlarinline1)

@dp.message_handler(text='location')
async def follow_inline(msg: Message):
    await msg.answer("locatisiya kiriting", reply_markup=Keyboard)

@dp.callback_query_handler(text='.2')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline2)

@dp.callback_query_handler(text='.1')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline1)

@dp.callback_query_handler(text='.3')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline3)

@dp.callback_query_handler(text='.4')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline4)


@dp.callback_query_handler(text='.5')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline5)


@dp.callback_query_handler(text='.6')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline6)

@dp.callback_query_handler(text='.7')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline7)

@dp.callback_query_handler(text='.8')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline8)

@dp.callback_query_handler(text='.9')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline9)

@dp.callback_query_handler(text='.10')
async def ismlar_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=ismlarinline10)

