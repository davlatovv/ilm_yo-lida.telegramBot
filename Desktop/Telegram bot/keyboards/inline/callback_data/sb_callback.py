from keyboards.inline.sb_inline import sbsend
from loader import dp, bot
from aiogram.types import CallbackQuery,ReplyKeyboardRemove
from keyboards.inline import sb_inline
from aiogram.types import Message

@dp.callback_query_handler(text='s1')
async def send_sb1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=517, protect_content=True)

@dp.callback_query_handler(text='s2')
async def send_sb1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=520, protect_content=True)

@dp.callback_query_handler(text='s3')
async def send_sb1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=522, protect_content=True)

@dp.callback_query_handler(text='s4')
async def send_sb1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=524, protect_content=True)

@dp.callback_query_handler(text='s5')
async def send_sb1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=526, protect_content=True)

@dp.callback_query_handler(text='s6')
async def send_sb1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=528, protect_content=True)

@dp.callback_query_handler(text='s7')
async def send_sb1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=530, protect_content=True)

@dp.callback_query_handler(text='s8')
async def send_sb1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=532, protect_content=True)

@dp.callback_query_handler(text='s9')
async def send_sb1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=534, protect_content=True)

@dp.callback_query_handler(text='s10')
async def send_sb1(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=536, protect_content=True)