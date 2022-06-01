from loader import dp, bot
from aiogram.types import Message, CallbackQuery

from keyboards.inline.duoinline import zikrinline,zikrinline1,zikrinline2



@dp.message_handler(text='Zikr')
async def zikr(msg:Message):
    await msg.answer("""
1 - Allohga tasbeh ayting
2 - Alloh taolo aytadi
3 - Allohga suyukli ikki kalima
4 - Buyuk sir yashiringan zikr
5 - Jannat hazinalaridan biri
6 - Zikrning afzali
7 - Istig'for kalimasi
8 - Al Iyman Al Mufassal"""
,reply_markup=zikrinline)

@dp.callback_query_handler(text='zikr1')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=636, protect_content=True)

@dp.callback_query_handler(text='zikr2')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=538, protect_content=True)

@dp.callback_query_handler(text='zikr3')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=558, protect_content=True)

@dp.callback_query_handler(text='zikr4')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=638, protect_content=True)

@dp.callback_query_handler(text='zikr5')
async def duo(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=639, protect_content=True)

@dp.callback_query_handler(text='zikr6')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=539, protect_content=True)

@dp.callback_query_handler(text='zikr7')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=553, protect_content=True)

@dp.callback_query_handler(text='zikr8')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=555, protect_content=True)



@dp.callback_query_handler(text='zikrinline')
async def zikr(call:CallbackQuery):
    await call.message.answer("""
1 - Allohga tasbeh ayting
2 - Alloh taolo aytadi
3 - Allohga suyukli ikki kalima
4 - Buyuk sir yashiringan zikr
5 - Jannat hazinalaridan biri
6 - Zikrning afzali
7 - Istig'for kalimasi
8 - Al Iyman Al Mufassal"""
,reply_markup=zikrinline)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='zikrinline1')
async def regions_callback(call: CallbackQuery):
    await call.message.answer("""
1 - Istig'for aytishning fazilati
2 - Istig'for aytish
3 - Ixlos surasini o'qish
4 - Shahodat kalimasi
5 - Toyyiba kalimasi
6 - Tavhid kalimasi
7 - Tamjid kalimasi
8 - Raddil kufr kalimasi
""",reply_markup=zikrinline1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='zikr9')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=560, protect_content=True)

@dp.callback_query_handler(text='zikr10')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=540, protect_content=True)

@dp.callback_query_handler(text='zikr11')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=542, protect_content=True)

@dp.callback_query_handler(text='zikr12')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=550, protect_content=True)

@dp.callback_query_handler(text='zikr13')
async def duo(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=548, protect_content=True)

@dp.callback_query_handler(text='zikr14')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=551, protect_content=True)

@dp.callback_query_handler(text='zikr15')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=554, protect_content=True)

@dp.callback_query_handler(text='zikr16')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=552, protect_content=True)


@dp.callback_query_handler(text='zikrinline2')
async def regions_callback(call: CallbackQuery):
    await call.message.answer("""
1 - Bomdod va shom namozlaridan keyingi zikr
2 - Namoz boshlanganda
3 - Namozdagi rukuda
4 - Rukudan bosh ko'targanda
5 - Sajda paytida
6 - Namoz tugaganda
7 - Zikr aytish
8 - Allohim meni avf et
""",reply_markup=zikrinline2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='zikr17')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=637, protect_content=True)

@dp.callback_query_handler(text='zikr18')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=590, protect_content=True)

@dp.callback_query_handler(text='zikr19')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=591, protect_content=True)

@dp.callback_query_handler(text='zikr20')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=592, protect_content=True)

@dp.callback_query_handler(text='zikr21')
async def duo(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=593, protect_content=True)

@dp.callback_query_handler(text='zikr22')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=597, protect_content=True)

@dp.callback_query_handler(text='zikr23')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=661, protect_content=True)

@dp.callback_query_handler(text='zikr24')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=660, protect_content=True)

