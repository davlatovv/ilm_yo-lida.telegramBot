from loader import dp, bot
from aiogram.types import Message, CallbackQuery
from data.dataNamaz import db


def bugun_toshkent():
    bugun = dict(db.get_toshkent()[0])
    key = [*bugun.keys()]
    value = [*bugun.values()]
    return (f"  📍Mintaqa - {value[12]}\n" + f"<b>{value[1]}</b> " + f"{value[0]} "+f"<b>2022</b> - <b>{value[3]}</b> {value[4]} <b>1443</b>\n\n"
            + f"    📆<i>{value[5]}</i>\n\n"
            + f"    🌌 {key[6]}: " + f" <b>{value[6]}</b>\n " + f"   🌄 {key[7]}: " + f" <b>{value[7]}</b>\n "
            + f"   🌇 {key[8]}: " + f" <b>{value[8]}</b>\n " + f"   🌆 {key[9]}: " + f" <b>{value[9]}</b>\n "
            + f"   🏙 {key[10]}: " + f" <b>{value[10]}</b>\n " + f"   🌃 {key[11]}: " + f" <b>{value[11]}</b>\n")

def bugun_andijon():
    bugun = dict(db.get_andijon()[0])
    key = [*bugun.keys()]
    value = [*bugun.values()]
    return (f"  📍Mintaqa - {value[12]}\n" + f"<b>{value[1]}</b> " + f"{value[0]} "+f"<b>2022</b> - <b>{value[3]}</b> {value[4]} <b>1443</b>\n\n"
            + f"    📆<i>{value[5]}</i>\n\n"
            + f"    🌌 {key[6]}: " + f" <b>{value[6]}</b>\n " + f"   🌄 {key[7]}: " + f" <b>{value[7]}</b>\n "
            + f"   🌇 {key[8]}: " + f" <b>{value[8]}</b>\n " + f"   🌆 {key[9]}: " + f" <b>{value[9]}</b>\n "
            + f"   🏙 {key[10]}: " + f" <b>{value[10]}</b>\n " + f"   🌃 {key[11]}: " + f" <b>{value[11]}</b>\n")
#
def bugun_buxoro():
    bugun = dict(db.get_buxoro()[0])
    key = [*bugun.keys()]
    value = [*bugun.values()]
    return (f"  📍Mintaqa - {value[12]}\n" + f"<b>{value[1]}</b> " + f"{value[0]} "+f"<b>2022</b> - <b>{value[3]}</b> {value[4]} <b>1443</b>\n\n"
            + f"    📆<i>{value[5]}</i>\n\n"
            + f"    🌌 {key[6]}: " + f" <b>{value[6]}</b>\n " + f"   🌄 {key[7]}: " + f" <b>{value[7]}</b>\n "
            + f"   🌇 {key[8]}: " + f" <b>{value[8]}</b>\n " + f"   🌆 {key[9]}: " + f" <b>{value[9]}</b>\n "
            + f"   🏙 {key[10]}: " + f" <b>{value[10]}</b>\n " + f"   🌃 {key[11]}: " + f" <b>{value[11]}</b>\n")
#
def bugun_guliston():
    bugun = dict(db.get_guliston()[0])
    key = [*bugun.keys()]
    value = [*bugun.values()]
    return (f"  📍Mintaqa - {value[12]}\n" + f"<b>{value[1]}</b> " + f"{value[0]} "+f"<b>2022</b> - <b>{value[3]}</b> {value[4]} <b>1443</b>\n\n"
            + f"    📆<i>{value[5]}</i>\n\n"
            + f"    🌌 {key[6]}: " + f" <b>{value[6]}</b>\n " + f"   🌄 {key[7]}: " + f" <b>{value[7]}</b>\n "
            + f"   🌇 {key[8]}: " + f" <b>{value[8]}</b>\n " + f"   🌆 {key[9]}: " + f" <b>{value[9]}</b>\n "
            + f"   🏙 {key[10]}: " + f" <b>{value[10]}</b>\n " + f"   🌃 {key[11]}: " + f" <b>{value[11]}</b>\n")
#
def bugun_samarqand():
    bugun = dict(db.get_samarqand()[0])
    key = [*bugun.keys()]
    value = [*bugun.values()]
    return (f"  📍Mintaqa - {value[12]}\n" + f"<b>{value[1]}</b> " + f"{value[0]} "+f"<b>2022</b> - <b>{value[3]}</b> {value[4]} <b>1443</b>\n\n"
            + f"    📆<i>{value[5]}</i>\n\n"
            + f"    🌌 {key[6]}: " + f" <b>{value[6]}</b>\n " + f"   🌄 {key[7]}: " + f" <b>{value[7]}</b>\n "
            + f"   🌇 {key[8]}: " + f" <b>{value[8]}</b>\n " + f"   🌆 {key[9]}: " + f" <b>{value[9]}</b>\n "
            + f"   🏙 {key[10]}: " + f" <b>{value[10]}</b>\n " + f"   🌃 {key[11]}: " + f" <b>{value[11]}</b>\n")
#
def bugun_namangan():
    bugun = dict(db.get_namangan()[0])
    key = [*bugun.keys()]
    value = [*bugun.values()]
    return (f"  📍Mintaqa - {value[12]}\n" + f"<b>{value[1]}</b> " + f"{value[0]} "+f"<b>2022</b> - <b>{value[3]}</b> {value[4]} <b>1443</b>\n\n"
            + f"    📆<i>{value[5]}</i>\n\n"
            + f"    🌌 {key[6]}: " + f" <b>{value[6]}</b>\n " + f"   🌄 {key[7]}: " + f" <b>{value[7]}</b>\n "
            + f"   🌇 {key[8]}: " + f" <b>{value[8]}</b>\n " + f"   🌆 {key[9]}: " + f" <b>{value[9]}</b>\n "
            + f"   🏙 {key[10]}: " + f" <b>{value[10]}</b>\n " + f"   🌃 {key[11]}: " + f" <b>{value[11]}</b>\n")
#
def bugun_navoi():
    bugun = dict(db.get_navoi()[0])
    key = [*bugun.keys()]
    value = [*bugun.values()]
    return (f"  📍Mintaqa - {value[12]}\n" + f"<b>{value[1]}</b> " + f"{value[0]} "+f"<b>2022</b> - <b>{value[3]}</b> {value[4]} <b>1443</b>\n\n"
            + f"    📆<i>{value[5]}</i>\n\n"
            + f"    🌌 {key[6]}: " + f" <b>{value[6]}</b>\n " + f"   🌄 {key[7]}: " + f" <b>{value[7]}</b>\n "
            + f"   🌇 {key[8]}: " + f" <b>{value[8]}</b>\n " + f"   🌆 {key[9]}: " + f" <b>{value[9]}</b>\n "
            + f"   🏙 {key[10]}: " + f" <b>{value[10]}</b>\n " + f"   🌃 {key[11]}: " + f" <b>{value[11]}</b>\n")
#
def bugun_jizzax():
    bugun = dict(db.get_jizzax()[0])
    key = [*bugun.keys()]
    value = [*bugun.values()]
    return (f"  📍Mintaqa - {value[12]}\n" + f"<b>{value[1]}</b> " + f"{value[0]} "+f"<b>2022</b> - <b>{value[3]}</b> {value[4]} <b>1443</b>\n\n"
            + f"    📆<i>{value[5]}</i>\n\n"
            + f"    🌌 {key[6]}: " + f" <b>{value[6]}</b>\n " + f"   🌄 {key[7]}: " + f" <b>{value[7]}</b>\n "
            + f"   🌇 {key[8]}: " + f" <b>{value[8]}</b>\n " + f"   🌆 {key[9]}: " + f" <b>{value[9]}</b>\n "
            + f"   🏙 {key[10]}: " + f" <b>{value[10]}</b>\n " + f"   🌃 {key[11]}: " + f" <b>{value[11]}</b>\n")
#
def bugun_nukus():
    bugun = dict(db.get_nukus()[0])
    key = [*bugun.keys()]
    value = [*bugun.values()]
    return (f"  📍Mintaqa - {value[12]}\n" + f"<b>{value[1]}</b> " + f"{value[0]} "+f"<b>2022</b> - <b>{value[3]}</b> {value[4]} <b>1443</b>\n\n"
            + f"    📆<i>{value[5]}</i>\n\n"
            + f"    🌌 {key[6]}: " + f" <b>{value[6]}</b>\n " + f"   🌄 {key[7]}: " + f" <b>{value[7]}</b>\n "
            + f"   🌇 {key[8]}: " + f" <b>{value[8]}</b>\n " + f"   🌆 {key[9]}: " + f" <b>{value[9]}</b>\n "
            + f"   🏙 {key[10]}: " + f" <b>{value[10]}</b>\n " + f"   🌃 {key[11]}: " + f" <b>{value[11]}</b>\n")
#
def bugun_qarshi():
    bugun = dict(db.get_qarshi()[0])
    key = [*bugun.keys()]
    value = [*bugun.values()]
    return (f"  📍Mintaqa - {value[12]}\n" + f"<b>{value[1]}</b> " + f"{value[0]} "+f"<b>2022</b> - <b>{value[3]}</b> {value[4]} <b>1443</b>\n\n"
            + f"    📆<i>{value[5]}</i>\n\n"
            + f"    🌌 {key[6]}: " + f" <b>{value[6]}</b>\n " + f"   🌄 {key[7]}: " + f" <b>{value[7]}</b>\n "
            + f"   🌇 {key[8]}: " + f" <b>{value[8]}</b>\n " + f"   🌆 {key[9]}: " + f" <b>{value[9]}</b>\n "
            + f"   🏙 {key[10]}: " + f" <b>{value[10]}</b>\n " + f"   🌃 {key[11]}: " + f" <b>{value[11]}</b>\n")
#
def bugun_qoqon():
    bugun = dict(db.get_qoqon()[0])
    key = [*bugun.keys()]
    value = [*bugun.values()]
    return (f"  📍Mintaqa - {value[12]}\n" + f"<b>{value[1]}</b> " + f"{value[0]} "+f"<b>2022</b> - <b>{value[3]}</b> {value[4]} <b>1443</b>\n\n"
            + f"    📆<i>{value[5]}</i>\n\n"
            + f"    🌌 {key[6]}: " + f" <b>{value[6]}</b>\n " + f"   🌄 {key[7]}: " + f" <b>{value[7]}</b>\n "
            + f"   🌇 {key[8]}: " + f" <b>{value[8]}</b>\n " + f"   🌆 {key[9]}: " + f" <b>{value[9]}</b>\n "
            + f"   🏙 {key[10]}: " + f" <b>{value[10]}</b>\n " + f"   🌃 {key[11]}: " + f" <b>{value[11]}</b>\n")
    print(bugun)
#
def bugun_xiva():
    bugun = dict(db.get_xiva()[0])
    key = [*bugun.keys()]
    value = [*bugun.values()]
    return (f"  📍Mintaqa - {value[12]}\n" + f"<b>{value[1]}</b> " + f"{value[0]} "+f"<b>2022</b> - <b>{value[3]}</b> {value[4]} <b>1443</b>\n\n"
            + f"    📆<i>{value[5]}</i>\n\n"
            + f"    🌌 {key[6]}: " + f" <b>{value[6]}</b>\n " + f"   🌄 {key[7]}: " + f" <b>{value[7]}</b>\n "
            + f"   🌇 {key[8]}: " + f" <b>{value[8]}</b>\n " + f"   🌆 {key[9]}: " + f" <b>{value[9]}</b>\n "
            + f"   🏙 {key[10]}: " + f" <b>{value[10]}</b>\n " + f"   🌃 {key[11]}: " + f" <b>{value[11]}</b>\n")
#
def bugun_margilon():
    bugun = dict(db.get_margilon()[0])
    key = [*bugun.keys()]
    value = [*bugun.values()]
    return (f"  📍Mintaqa - {value[12]}\n" + f"<b>{value[1]}</b> " + f"{value[0]} "+f"<b>2022</b> - <b>{value[3]}</b> {value[4]} <b>1443</b>\n\n"
            + f"    📆<i>{value[5]}</i>\n\n"
            + f"    🌌 {key[6]}: " + f" <b>{value[6]}</b>\n " + f"   🌄 {key[7]}: " + f" <b>{value[7]}</b>\n "
            + f"   🌇 {key[8]}: " + f" <b>{value[8]}</b>\n " + f"   🌆 {key[9]}: " + f" <b>{value[9]}</b>\n "
            + f"   🏙 {key[10]}: " + f" <b>{value[10]}</b>\n " + f"   🌃 {key[11]}: " + f" <b>{value[11]}</b>\n")
#


"""CALLBACK_QUERY_HANDLER"""

@dp.callback_query_handler(text='bugun:toshkent')
async def inline_today_toshkent(call: CallbackQuery):
    today = bugun_toshkent()
    await bot.send_message(chat_id=call.from_user.id, text=today, parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:andijon')
async def inline_today_andijon(call: CallbackQuery):
    today = bugun_andijon()
    await bot.send_message(chat_id=call.from_user.id, text=today, parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:buxoro')
async def inline_today_buxoro(call: CallbackQuery):
    today = bugun_buxoro()
    await bot.send_message(chat_id=call.from_user.id, text=today, parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:guliston')
async def inline_today_guliston(call: CallbackQuery):
    today = bugun_guliston()
    await bot.send_message(chat_id=call.from_user.id, text=today, parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:samarqand')
async def inline_today_sqmqrqand(call: CallbackQuery):
    today = bugun_samarqand()
    await bot.send_message(chat_id=call.from_user.id, text=today, parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:namangan')
async def inline_today_namangan(call: CallbackQuery):
    today = bugun_namangan()
    await bot.send_message(chat_id=call.from_user.id, text=today, parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:navoi')
async def inline_today_navoi(call: CallbackQuery):
    today = bugun_navoi()
    await bot.send_message(chat_id=call.from_user.id, text=today, parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:jizzax')
async def inline_today_jizzax(call: CallbackQuery):
    today = bugun_jizzax()
    await bot.send_message(chat_id=call.from_user.id, text=today, parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:nukus')
async def inline_today_nukus(call: CallbackQuery):
    today = bugun_nukus()
    await bot.send_message(chat_id=call.from_user.id, text=today, parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:qarshi')
async def inline_today_qarshi(call: CallbackQuery):
    today = bugun_qarshi()
    await bot.send_message(chat_id=call.from_user.id, text=today, parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:qoqon')
async def inline_today_qoqon(call: CallbackQuery):
    today = bugun_qoqon()
    await bot.send_message(chat_id=call.from_user.id, text=today, parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:xiva')
async def inline_today_xiva(call: CallbackQuery):
    today = bugun_xiva()
    await bot.send_message(chat_id=call.from_user.id, text=today, parse_mode="html")
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='bugun:margilon')
async def inline_today_margilon(call: CallbackQuery):
    today = bugun_margilon()
    await bot.send_message(chat_id=call.from_user.id, text=today, parse_mode="html")
    await call.answer(cache_time=60)

