from loader import dp, bot
from aiogram.types import CallbackQuery


# FARZ_____________________


@dp.callback_query_handler(text='f:bomdod')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=686, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=692,protect_content=True)
@dp.callback_query_handler(text='f:peshin')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=680, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=694, protect_content=True)

@dp.callback_query_handler(text='f:asr')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=681, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=696, protect_content=True)

@dp.callback_query_handler(text='f:shom')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=682, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=697, protect_content=True)

@dp.callback_query_handler(text='f:xufton')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=684, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=699, protect_content=True)
@dp.callback_query_handler(text='juma')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=689, protect_content=True)

@dp.callback_query_handler(text='janoza')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=690, protect_content=True)

# SUNNAT__________________


@dp.callback_query_handler(text='s:bomdod')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=685, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=691,protect_content=True)

@dp.callback_query_handler(text='s:peshin2')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=679, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=695, protect_content=True)
@dp.callback_query_handler(text='s:peshin4')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=678, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=693,protect_content=True)

@dp.callback_query_handler(text='s:shom')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=683, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=698, protect_content=True)
@dp.callback_query_handler(text='s:xufton')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=705, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=700, protect_content=True)



# VOJIB _______________________

@dp.callback_query_handler(text='vitr')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=702, protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=701, protect_content=True)

@dp.callback_query_handler(text='hayit')
async def send_sura(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=703, protect_content=True)

