from loader import dp, bot
from aiogram.types import Message, CallbackQuery

from keyboards.inline.duoinline import duoinline1, duoinline2, duoinline3,duoinline4,duoinline

@dp.message_handler(text='Duo')
async def duo(msg:Message):
    await msg.answer("""
1 - Alloh taolo musulmonlarni duo qilishga buyurgan
2 - Yunus a.s ning duolari (G'amni ketkazib shodlikni chaqiruvchi duo)
3 - Omad kelishi va ishlar yurishib ketishi uchun o'qiladigan duo
4 - Allohim, sendan pok rizq so'rayman
5 - Nabiy s.a.v doim o'qib yurgan duolari
6 - Dunyo va oxiratdagi muhim ishlarda o'qiladigan duo
7 - 70000 farishtani vakil qilib qo'yadigan duo
8 - Zararli narsalardan saqlanish
""",reply_markup=duoinline)

@dp.callback_query_handler(text='duoinline')
async def duo(call:CallbackQuery):
    await call.message.answer("""
1 - Alloh taolo musulmonlarni duo qilishga buyurgan
2 - Yunus a.s ning duolari (G'amni ketkazib shodlikni chaqiruvchi duo)
3 - Omad kelishi va ishlar yurishib ketishi uchun o'qiladigan duo
4 - Allohim, sendan pok rizq so'rayman
5 - Nabiy s.a.v doim o'qib yurgan duolari
6 - Dunyo va oxiratdagi muhim ishlarda o'qiladigan duo
7 - 70000 farishtani vakil qilib qo'yadigan duo
8 - Zararli narsalardan saqlanish
""",reply_markup=duoinline)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='duo1')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=538, protect_content=True)

@dp.callback_query_handler(text='duo2')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=640, protect_content=True)

@dp.callback_query_handler(text='duo3')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=559, protect_content=True)

@dp.callback_query_handler(text='duo4')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=576, protect_content=True)

@dp.callback_query_handler(text='duo5')
async def duo(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=573, protect_content=True)

@dp.callback_query_handler(text='duo6')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=577, protect_content=True)

@dp.callback_query_handler(text='duo7')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=579, protect_content=True)

@dp.callback_query_handler(text='duo8')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=574, protect_content=True)


@dp.callback_query_handler(text='duoinline1')
async def duo_callback(call:CallbackQuery):
    await call.message.answer("""
1 - Allohim, do'zaxdan saqla!
2 - Allohim to'satdan yaxshilik bo'lishini sendan so'rayman
3 - Ey Robbim, zulm ko'rishdan panoh so'rayman
4 - Allohim g'am-g'ussamni ketkaz, qarzdan halos et!
5 - Tong otganda va kech kirganda o'qiladigan duo
6 - Jamoat haqqiga o'qiladigan duo
7 - Nafsimni yomonligidan panoh tilayman
8 - "Shayton unga yaqinlasha olmaydi"
""",reply_markup=duoinline1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='duo9')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=575, protect_content=True)

@dp.callback_query_handler(text='duo10')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=578, protect_content=True)

@dp.callback_query_handler(text='duo11')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=585, protect_content=True)

@dp.callback_query_handler(text='duo12')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=580, protect_content=True)

@dp.callback_query_handler(text='duo13')
async def duo(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=561, protect_content=True)

@dp.callback_query_handler(text='duo14')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=571, protect_content=True)

@dp.callback_query_handler(text='duo15')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=582, protect_content=True)

@dp.callback_query_handler(text='duo16')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=586, protect_content=True)


@dp.callback_query_handler(text='duoinline2')
async def duo_callback(call:CallbackQuery):
    await call.message.answer("""
1 - Hojatxonaga kirayotganda
2 - Hojatxonadan chiqayotganda
3 - Tahorat qilinganda
4 - Uyga kirayotganda
5 - Uydan chiqayotganda
6 - Masjidga kirayotganda va chiqayotganda
7 - Azon va iqomatni eshitganda
8 - Azon va iqomatning o'rtasida
""",reply_markup=duoinline2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='duo17')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=601, protect_content=True)

@dp.callback_query_handler(text='duo18')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=602, protect_content=True)

@dp.callback_query_handler(text='duo19')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=587, protect_content=True)

@dp.callback_query_handler(text='duo20')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=600, protect_content=True)

@dp.callback_query_handler(text='duo21')
async def duo(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=599, protect_content=True)

@dp.callback_query_handler(text='duo22')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=588, protect_content=True)

@dp.callback_query_handler(text='duo23')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=589, protect_content=True)

@dp.callback_query_handler(text='duo24')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=583, protect_content=True)



@dp.callback_query_handler(text='duoinline3')
async def duo_callback(call:CallbackQuery):
    await call.message.answer("""
1 - Tashahhud
2 - Vitrdagi qunut duosi
3 - Namozdan keyingi duo
4 - Tongda o'qiladigan duo
5 - Nabiy s.a.v to'shaklariga yotayotganlarida o'qiydigan duolari
6 - Kech kirganda o'qiladigan duo
7 - Juma kuni Bomdod namozidan oldin o'qiladigan duo
8 - Juma kuni Kahf surasini o'qishning fazilati
""",reply_markup=duoinline3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='duo25')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=595, protect_content=True)

@dp.callback_query_handler(text='duo26')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=594, protect_content=True)

@dp.callback_query_handler(text='duo27')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=598, protect_content=True)

@dp.callback_query_handler(text='duo28')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=570, protect_content=True)

@dp.callback_query_handler(text='duo29')
async def duo(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=581, protect_content=True)

@dp.callback_query_handler(text='duo30')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=561, protect_content=True)

@dp.callback_query_handler(text='duo31')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=556, protect_content=True)

@dp.callback_query_handler(text='duo32')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=557, protect_content=True)


@dp.callback_query_handler(text='duoinline4')
async def regions_callback(call:CallbackQuery):
    await call.message.answer("""
1 - Juma surasining fazilati
2 - Voqea surasining fazilati
3 - Duhon surasining fazilati
4 - Shar'iy qo'shilishdan oldin o'qiladigan duo
5 - Yangi kiyim kiyganda
6 - "Quyosh chiqib nur sochganidan yaxshiroqdir"
7 - "Uning bu amalidan afzalroq ishni hech kim qila olmaydi"
8 - "Unga jannat vojib bo'ladi"
""",reply_markup=duoinline4)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='duo33')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=562, protect_content=True)

@dp.callback_query_handler(text='duo34')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=563, protect_content=True)

@dp.callback_query_handler(text='duo35')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=569, protect_content=True)

@dp.callback_query_handler(text='duo36')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=662, protect_content=True)

@dp.callback_query_handler(text='duo37')
async def duo(call: CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=666, protect_content=True)

@dp.callback_query_handler(text='duo38')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=665, protect_content=True)

@dp.callback_query_handler(text='duo39')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=664, protect_content=True)

@dp.callback_query_handler(text='duo40')
async def duo(call:CallbackQuery):
    await bot.copy_message(chat_id=call.from_user.id, from_chat_id='@testislomyolida', message_id=663, protect_content=True)





