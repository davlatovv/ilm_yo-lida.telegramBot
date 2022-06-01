import sqlite3

from keyboards.inline.namazvaqtInline import namozVaqtInlineT,namozVaqtInlineA,namozVaqtInlineB,namozVaqtInlineG,namozVaqtInlineJ,namozVaqtInlineM,namozVaqtInlineS,namozVaqtInlineX,namozVaqtInlineNuk,namozVaqtInlineNam,namozVaqtInlineNav,namozVaqtInlineQar,namozVaqtInlineQoq
from keyboards.inline.obunaInline import obunaInlineQar,obunaInlineNuk,obunaInlineQoq,obunaInlineNav,obunaInlineNam,obunaInlineT,obunaInlineS,obunaInlineG,obunaInlineB,obunaInlineA,obunaInlineX,obunaInlineM,obunaInlineJ
from keyboards.inline.regionsInline import regionInline

from loader import dp, db_obuna
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text='toshkent')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    try:
        if db_obuna.select_user(id=call.from_user.id,name=name):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕: O'chirish❌", reply_markup=obunaInlineT)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔔: Yoqish✅", reply_markup=namozVaqtInlineT)
    except sqlite3.InternalError and sqlite3.IntegrityError and sqlite3.InterfaceError:
        pass
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='andijon')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    try:
        if db_obuna.select_user(id=call.from_user.id,name=name):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕: O'chirish❌", reply_markup=obunaInlineA)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔔: Yoqish✅", reply_markup=namozVaqtInlineA)
    except sqlite3.InternalError and sqlite3.IntegrityError and sqlite3.InterfaceError:
        pass
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='buxoro')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    try:
        if db_obuna.select_user(id=call.from_user.id,name=name):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕: O'chirish❌",reply_markup=obunaInlineB)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔔: Yoqish✅", reply_markup=namozVaqtInlineB)
    except sqlite3.InternalError and sqlite3.IntegrityError and sqlite3.InterfaceError:
        pass
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='guliston')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    try:
        if db_obuna.select_user(id=call.from_user.id,name=name):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕: O'chirish❌", reply_markup=obunaInlineG)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔔: Yoqish✅", reply_markup=namozVaqtInlineG)
    except sqlite3.InternalError and sqlite3.IntegrityError and sqlite3.InterfaceError:
        pass
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='samarqand')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    try:
        if db_obuna.select_user(id=call.from_user.id,name=name):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕: O'chirish❌", reply_markup=obunaInlineS)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔔: Yoqish✅", reply_markup=namozVaqtInlineS)
    except sqlite3.InternalError and sqlite3.IntegrityError and sqlite3.InterfaceError:
        pass
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='namangan')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    try:
        if db_obuna.select_user(id=call.from_user.id,name=name):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕: O'chirish❌", reply_markup=obunaInlineNam)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔔: Yoqish✅", reply_markup=namozVaqtInlineNam)
    except sqlite3.InternalError and sqlite3.IntegrityError and sqlite3.InterfaceError:
        pass
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='navoi')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    try:
        if db_obuna.select_user(id=call.from_user.id,name=name):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕: O'chirish❌", reply_markup=obunaInlineNav)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔔: Yoqish✅", reply_markup=namozVaqtInlineNav)
    except sqlite3.InternalError and sqlite3.IntegrityError and sqlite3.InterfaceError:
        pass
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='jizzax')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    try:
        if db_obuna.select_user(id=call.from_user.id,name=name):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕: O'chirish❌",reply_markup=obunaInlineJ)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔔: Yoqish✅", reply_markup=namozVaqtInlineJ)
    except sqlite3.InternalError and sqlite3.IntegrityError and sqlite3.InterfaceError:
        pass
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='nukus')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    try:
        if db_obuna.select_user(id=call.from_user.id,name=name):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕: O'chirish❌", reply_markup=obunaInlineNuk)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔔: Yoqish✅", reply_markup=namozVaqtInlineNuk)
    except sqlite3.InternalError and sqlite3.IntegrityError and sqlite3.InterfaceError:
        pass
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='qarshi')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    try:
        if db_obuna.select_user(id=call.from_user.id,name=name):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕: O'chirish❌", reply_markup=obunaInlineQar)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔔: Yoqish✅", reply_markup=namozVaqtInlineQar)
    except sqlite3.InternalError and sqlite3.IntegrityError and sqlite3.InterfaceError:
        pass
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='qoqon')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    try:
        if db_obuna.select_user(id=call.from_user.id,name=name):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕: O'chirish❌", reply_markup=obunaInlineQoq)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔔: Yoqish✅", reply_markup=namozVaqtInlineQoq)
    except sqlite3.InternalError and sqlite3.IntegrityError and sqlite3.InterfaceError:
        pass
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='xiva')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    try:
        if db_obuna.select_user(id=call.from_user.id,name=name):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕: O'chirish❌", reply_markup=obunaInlineX)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔔: Yoqish✅", reply_markup=namozVaqtInlineX)
    except sqlite3.InternalError and sqlite3.IntegrityError and sqlite3.InterfaceError:
        pass
    await call.answer(cache_time=60)
@dp.callback_query_handler(text='margilon')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    name = call.from_user.full_name
    try:
        if db_obuna.select_user(id=call.from_user.id,name=name):
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔕: O'chirish❌", reply_markup=obunaInlineM)
        else:
            await call.message.answer("Bugun📅: bugungi namoz vaqtlari \nEslatma🔔: Yoqish✅", reply_markup=namozVaqtInlineM)
    except sqlite3.InternalError and sqlite3.IntegrityError and sqlite3.InterfaceError:
        pass
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='qaytish')
async def regions_callback(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer("Mintaqa❓",reply_markup=regionInline)




