from loader import dp, bot
from aiogram.types import CallbackQuery, Message

from keyboards.inline.namozturlarInline import gusl


@dp.message_handler(text='G\'usl va Tahorat🚰')
async def namoz_turi(msg:Message):
    await msg.answer("<b>G'usul va Tahorat\n</b>",reply_markup=gusl,parse_mode="html")

@dp.callback_query_handler(text="gusl")
async def gusul(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=655,
                           protect_content=True)

@dp.callback_query_handler(text="tahorat")
async def gusul(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=564,
                           protect_content=True)