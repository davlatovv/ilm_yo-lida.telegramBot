from loader import dp, bot
from aiogram.types import CallbackQuery,Message

from keyboards.inline.Asmaul_HusnaInline import ismlar

@dp.message_handler(text='Allohning 99 ismi')
async def ismlar_99(msg:Message):
    await msg.answer("<b>Allohning 99ta ismlari to'liq</b>",reply_markup=ismlar,parse_mode="html")

@dp.callback_query_handler(text="99ism")
async def send_99(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=709,
                           protect_content=True)
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=479,
                           protect_content=True)


@dp.callback_query_handler(text='..1')
async def send_ism(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=707, protect_content=True)

@dp.callback_query_handler(text='..2')
async def send_ism(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=707, protect_content=True)
 