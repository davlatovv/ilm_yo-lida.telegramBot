from loader import dp, bot
from aiogram.types import Message, CallbackQuery

from keyboards.inline.duoinline import salovatinline

@dp.message_handler(text='Salovat')
async def salovat(msg:Message):
    await msg.answer("""
1 - Alloh talo aytadi
2 - Payg'ambarimiz s.a.v ga salovat aytishning fazilati
3 - Qisqa salovat
4 - Yo Alloh Payg'ambarimiz s.a.v ga va u zotning oilalariga rahmat ayla
5 - Eng afzal va go'zal salovat
6 - Salovat 
7 - Tashahhuddan keyingi salovat
8 - Qisqa salovat""",reply_markup=salovatinline)


@dp.callback_query_handler(text='salovat1')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=642, protect_content=True)

@dp.callback_query_handler(text='salovat2')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=645, protect_content=True)

@dp.callback_query_handler(text='salovat3')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=647, protect_content=True)

@dp.callback_query_handler(text='salovat4')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=643, protect_content=True)

@dp.callback_query_handler(text='salovat5')
async def duo(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=667, protect_content=True)

@dp.callback_query_handler(text='salovat6')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=644, protect_content=True)

@dp.callback_query_handler(text='salovat7')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=596, protect_content=True)

@dp.callback_query_handler(text='salovat8')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=541, protect_content=True)