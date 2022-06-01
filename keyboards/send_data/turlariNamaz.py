from loader import dp
from aiogram.types import CallbackQuery, Message

from keyboards.inline.namozturlarInline import namozTurlari,nafl,sunnat,farz,vojib

@dp.message_handler(text='Namoz turlari🧎')
async def namozTuri(msg:Message):
    await msg.answer("Namoz haqida to'liq malumotni\n<b>«Hadis va Hayot»(<i>Shayx Muhammad Sodiq Muhammad Yusuf</i>)</b> kitobining\n 6-juzidan topshingiz mumkun...",reply_markup=namozTurlari,parse_mode="html")

@dp.callback_query_handler(text="farz")
async def namozTuri(call:CallbackQuery):
    await call.message.answer("<b>• Farz namozlari</b> - Alloh taoloning amri bilan har bir musulmon zimmasida burch hisoblangan bеsh vaqt namoz (bomdod, pеshin, asr, shom, xufton) va juma namozi hamda (musulmonlardan ba'zilarining oʻqishi bilan boshqalardan soqit boʻluvchi) janoza namozi.",reply_markup=farz,parse_mode="html")
    await call.message.delete()
@dp.callback_query_handler(text="vojib")
async def namozTuri(call: CallbackQuery):
    await call.message.answer("<b>• Vojib namozlar</b> – har kuni xuftondan soʻng oʻqiladigan vitr namozi, ramazon va qurbon hayiti namozlari, Baytullohdagi tavof namozi.",reply_markup=vojib,parse_mode="html")
    await call.message.delete()
@dp.callback_query_handler(text="sunnat")
async def namozTuri(call: CallbackQuery):
    await call.message.answer("SUNNAT",reply_markup=sunnat,parse_mode="html")
    await call.message.delete()

@dp.callback_query_handler(text="nafl")
async def namozTuri(call: CallbackQuery):
    await call.message.answer("NAFL",reply_markup=nafl,parse_mode="html")
    await call.message.delete()

@dp.callback_query_handler(text="namozturlariga")
async def besh_vaqt(call:CallbackQuery):
    await call.message.answer("Namoz haqida to'liq malumotni\n<b>«Hadis va Hayot»(<i>Shayx Muhammad Sodiq Muhammad Yusuf</i>)</b> kitobining\n 6-juzidan topshingiz mumkun...",reply_markup=namozTurlari,parse_mode="html")
    await call.message.delete()