from loader import dp
from aiogram.types import CallbackQuery
from keyboards.inline.quranInline import quraninline, quraninline1, quraninline2, quraninline3, quraninline4, quraninline5, quraninline6, quraninline7, quraninline8


@dp.callback_query_handler(text='>')
async def regions_callback(call:CallbackQuery):
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='>1')
async def regions_callback(call:CallbackQuery):
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='<')
async def regions_callback(call:CallbackQuery):
    await call.message.answer('quron',reply_markup=quraninline)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='>2')
async def regions_callback(call:CallbackQuery):
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='<1')
async def regions_callback(call:CallbackQuery):
    await call.message.answer('01- Fotiha surasi\n02- Baqara surasi\n03- Oli Imron surasi\n04- Niso surasi\n05- Moida surasi\n06- An’om surasi\n07- A’rof surasi\n08- Anfol surasi\n09- Tavba surasi\n10- Yunus surasi\n11- Hud surasi\n12- Yusuf surasi\n13- Ra’d surasi\n14- Ibrohim surasi',reply_markup=quraninline1)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='>3')
async def regions_callback(call:CallbackQuery):
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi',reply_markup=quraninline3)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='<2')
async def regions_callback(call:CallbackQuery):
    await call.message.answer('15- Hijr surasi\n16- Nahl surasi\n17- Isro surasi\n18- Kahf surasi\n19- Maryam surasi\n20- To Ha surasi\n21- Anbiyo surasi\n22- Haj surasi\n23- Mu’minun surasi\n24- Nur surasi\n25- Furqon surasi\n26- Shu’aro surasi\n27- Naml surasi\n28- Qasos surasi',reply_markup=quraninline2)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='>4')
async def regions_callback(call: CallbackQuery):
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='<3')
async def regions_callback(call: CallbackQuery):
    await call.message.answer('29- Ankabut surasi\n30- Rum surasi\n31- Luqmon surasi\n32- Sajda surasi\n33- Ahzob surasi\n34- Saba’ surasi\n35- Fotir surasi\n36- Yosin surasi\n37- Soffat surasi\n38- Sod surasi\n39- Zumar surasi\n40- G’ofir surasi\n41- Fussilat surasi\n42- Sho’ro surasi', reply_markup=quraninline3)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='>5')
async def regions_callback(call: CallbackQuery):
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='<4')
async def regions_callback(call: CallbackQuery):
    await call.message.answer('43- Zuxruf surasi\n44- Duxon surasi\n45- Josiya surasi\n46- Ahqof surasi\n47- Muhammad surasi\n48- Fath surasi\n49- Hujurot surasi\n50- Qof surasi\n51- Zoriyot surasi\n52- Tur surasi\n53- Najm surasi\n54- Qamar surasi\n55- Rahmon surasi\n56- Voqea surasi', reply_markup=quraninline4)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='>6')
async def regions_callback(call: CallbackQuery):
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='<5')
async def regions_callback(call: CallbackQuery):
    await call.message.answer('57- Hadid surasi\n58- Mujodala surasi\n59- Hashr surasi\n60- Mumtahana surasi\n61- Sof surasi\n62- Jum’a surasi\n63- Munofiqun  surasi\n64- Tog’abun surasi\n65- Taloq surasi\n66- Tahrim surasi\n67- Mulk surasi\n68- Qalam surasi\n69- Haaqqo surasi\n70- Maorij surasi', reply_markup=quraninline5)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='>7')
async def regions_callback(call: CallbackQuery):
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='<6')
async def regions_callback(call: CallbackQuery):
    await call.message.answer('71- Nuh surasi\n72- Jin surasi\n73- Muzzammil surasi\n74- Muddassir surasi\n75- Qiyomat surasi\n76- Inson surasi\n77- Mursalot  surasi\n78- Naba’ surasi\n79- Nazi’at surasi\n80- Abasa surasi\n81- Takvir surasi\n82- Infitor surasi\n83- Mutoffifin surasi\n84- Inshiqoq surasi', reply_markup=quraninline6)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='>8')
async def regions_callback(call: CallbackQuery):
    await call.message.answer('99- Zalzala surasi\n100- Odiyat surasi\n101- Qori’a surasi\n102- Takosur surasi\n103- Asr surasi\n104- Humaza surasi\n105- Fil surasi\n106- Quraysh surasi\n107- Mo’un surasi\n108- Kavsar surasi\n109- Kofirun surasi\n110- Nasr surasi\n111- Masad surasi\n112-Ixlos surasi\n113-Falaq surasi\n114-Nos surasi', reply_markup=quraninline8)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='<7')
async def regions_callback(call: CallbackQuery):
    await call.message.answer('85- Buruj surasi\n86- Toriq surasi\n87- A’lo surasi\n88- G’oshiya surasi\n89- Fajr surasi\n90- Balad surasi\n91- Shams surasi\n92- Layl surasi\n93- Zuho surasi\n94- Sharh surasi\n95- Tiyn surasi\n96- Alaq surasi\n97- Qadr surasi\n98- Bayyina surasi', reply_markup=quraninline7)
    await call.message.delete()
    await call.answer(cache_time=60)

