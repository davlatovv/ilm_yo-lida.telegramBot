from keyboards.inline.obunaInline import obunaInlineNuk,obunaInlineQar,obunaInlineQoq,obunaInlineJ,obunaInlineM,obunaInlineX,obunaInlineNam,obunaInlineNav,obunaInlineA,obunaInlineB,obunaInlineG,obunaInlineS,obunaInlineT
from keyboards.inline.namazvaqtInline import namozVaqtInlineT,namozVaqtInlineA,namozVaqtInlineB,namozVaqtInlineG,namozVaqtInlineJ,namozVaqtInlineM,namozVaqtInlineS,namozVaqtInlineX,namozVaqtInlineNuk,namozVaqtInlineNam,namozVaqtInlineNav,namozVaqtInlineQar,namozVaqtInlineQoq
from data.config import ADMINS
from app import scheduler_toshkent,scheduler_buxoro,scheduler_andijon,scheduler_jizzax,scheduler_qarshi,scheduler_navoi,scheduler_samarqand,scheduler_guliston,scheduler_margilon,scheduler_namangan,scheduler_qoqon,scheduler_xiva,scheduler_nukus


import sqlite3
from loader import dp, bot, db_obuna
from aiogram.types import CallbackQuery



"""Toshkent"""
@dp.callback_query_handler(text='obuna:toshkent')
async def inline_follow1(call:CallbackQuery):
    scheduler_toshkent.start()
    await call.message.edit_reply_markup(reply_markup=obunaInlineT)
    name = call.from_user.full_name
    try:
        db_obuna.add_user(id=call.from_user.id,
                          name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

@dp.callback_query_handler(text='ochir:toshkent')
async def inline_follow1(call: CallbackQuery):
    scheduler_toshkent.shutdown()
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineT)
    name = call.from_user.full_name
    try:
        db_obuna.delete_user(id=call.from_user.id,
                             name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

""""Buxoro"""
@dp.callback_query_handler(text='obuna:buxoro')
async def inline_follow1(call: CallbackQuery):
    scheduler_buxoro.start()
    await call.message.edit_reply_markup(reply_markup=obunaInlineB)
    name = call.from_user.full_name
    try:
        db_obuna.add_user(id=call.from_user.id,
                          name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

@dp.callback_query_handler(text='ochir:buxoro')
async def inline_follow1(call: CallbackQuery):
    scheduler_buxoro.shutdown()
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineB)
    name = call.from_user.full_name
    try:
        db_obuna.delete_user(id=call.from_user.id,
                             name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

""""Andijon"""
@dp.callback_query_handler(text='obuna:andijon')
async def inline_follow1(call: CallbackQuery):
    scheduler_andijon.start()
    await call.message.edit_reply_markup(reply_markup=obunaInlineA)
    name = call.from_user.full_name
    try:
        db_obuna.add_user(id=call.from_user.id,
                          name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

@dp.callback_query_handler(text='ochir:andijon')
async def inline_follow1(call: CallbackQuery):
    scheduler_andijon.shutdown()
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineA)
    name = call.from_user.full_name
    try:
        db_obuna.delete_user(id=call.from_user.id,
                             name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

""""Guliston"""
@dp.callback_query_handler(text='obuna:guliston')
async def inline_follow1(call: CallbackQuery):
    scheduler_guliston.start()
    await call.message.edit_reply_markup(reply_markup=obunaInlineG)
    name = call.from_user.full_name
    try:
        db_obuna.add_user(id=call.from_user.id,
                          name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

@dp.callback_query_handler(text='ochir:guliston')
async def inline_follow1(call: CallbackQuery):
    scheduler_guliston.shutdown()
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineG)
    name = call.from_user.full_name
    try:
        db_obuna.delete_user(id=call.from_user.id,
                             name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

""""Jizzax"""
@dp.callback_query_handler(text='obuna:jizzax')
async def inline_follow1(call: CallbackQuery):
    scheduler_jizzax.start()
    await call.message.edit_reply_markup(reply_markup=obunaInlineJ)
    name = call.from_user.full_name
    try:
        db_obuna.add_user(id=call.from_user.id,
                          name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

@dp.callback_query_handler(text='ochir:jizzax')
async def inline_follow1(call: CallbackQuery):
    scheduler_jizzax.shutdown()
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineJ)
    name = call.from_user.full_name
    try:
        db_obuna.delete_user(id=call.from_user.id,
                             name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

""""Margilon"""
@dp.callback_query_handler(text='obuna:margilon')
async def inline_follow1(call: CallbackQuery):
    scheduler_margilon.start()
    await call.message.edit_reply_markup(reply_markup=obunaInlineM)
    name = call.from_user.full_name
    try:
        db_obuna.add_user(id=call.from_user.id,
                          name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

@dp.callback_query_handler(text='ochir:margilon')
async def inline_follow1(call: CallbackQuery):
    scheduler_margilon.shutdown()
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineM)
    name = call.from_user.full_name
    try:
        db_obuna.delete_user(id=call.from_user.id,
                             name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

""""Namangan"""
@dp.callback_query_handler(text='obuna:namangan')
async def inline_follow1(call: CallbackQuery):
    scheduler_namangan.start()
    await call.message.edit_reply_markup(reply_markup=obunaInlineNam)
    name = call.from_user.full_name
    try:
        db_obuna.add_user(id=call.from_user.id,
                          name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

@dp.callback_query_handler(text='ochir:namangan')
async def inline_follow1(call: CallbackQuery):
    scheduler_namangan.shutdown()
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineNam)
    name = call.from_user.full_name
    try:
        db_obuna.delete_user(id=call.from_user.id,
                             name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

""""Navoiy"""
@dp.callback_query_handler(text='obuna:navoi')
async def inline_follow1(call: CallbackQuery):
    scheduler_navoi.start()
    await call.message.edit_reply_markup(reply_markup=obunaInlineNav)
    name = call.from_user.full_name
    try:
        db_obuna.add_user(id=call.from_user.id,
                          name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

@dp.callback_query_handler(text='ochir:navoi')
async def inline_follow1(call: CallbackQuery):
    scheduler_navoi.shutdown()
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineNav)
    name = call.from_user.full_name
    try:
        db_obuna.delete_user(id=call.from_user.id,
                             name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

""""Nukus"""
@dp.callback_query_handler(text='obuna:nukus')
async def inline_follow1(call: CallbackQuery):
    scheduler_nukus.start()
    await call.message.edit_reply_markup(reply_markup=obunaInlineNuk)
    name = call.from_user.full_name
    try:
        db_obuna.add_user(id=call.from_user.id,
                          name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

@dp.callback_query_handler(text='ochir:nukus')
async def inline_follow1(call: CallbackQuery):
    scheduler_nukus.shutdown()
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineNuk)
    name = call.from_user.full_name
    try:
        db_obuna.delete_user(id=call.from_user.id,
                             name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

""""Qoqon"""
@dp.callback_query_handler(text='obuna:qoqon')
async def inline_follow1(call: CallbackQuery):
    scheduler_qoqon.start()
    await call.message.edit_reply_markup(reply_markup=obunaInlineQoq)
    name = call.from_user.full_name
    try:
        db_obuna.add_user(id=call.from_user.id,
                          name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

@dp.callback_query_handler(text='ochir:qoqon')
async def inline_follow1(call: CallbackQuery):
    scheduler_qoqon.shutdown()
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineQoq)
    name = call.from_user.full_name
    try:
        db_obuna.delete_user(id=call.from_user.id,
                             name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

""""Qarshi"""
@dp.callback_query_handler(text='obuna:qarshi')
async def inline_follow1(call: CallbackQuery):
    scheduler_qarshi.start()
    await call.message.edit_reply_markup(reply_markup=obunaInlineQar)
    name = call.from_user.full_name
    try:
        db_obuna.add_user(id=call.from_user.id,
                          name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

@dp.callback_query_handler(text='ochir:qarshi')
async def inline_follow1(call: CallbackQuery):
    scheduler_qarshi.shutdown()
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineQar)
    name = call.from_user.full_name
    try:
        db_obuna.delete_user(id=call.from_user.id,
                             name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

""""Samarqand"""
@dp.callback_query_handler(text='obuna:samarqand')
async def inline_follow1(call: CallbackQuery):
    scheduler_samarqand.start()
    await call.message.edit_reply_markup(reply_markup=obunaInlineS)
    name = call.from_user.full_name
    try:
        db_obuna.add_user(id=call.from_user.id,
                          name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

@dp.callback_query_handler(text='ochir:samarqand')
async def inline_follow1(call: CallbackQuery):
    scheduler_samarqand.shutdown()
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineS)
    name = call.from_user.full_name
    try:
        db_obuna.delete_user(id=call.from_user.id,
                             name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

""""Xiva"""
@dp.callback_query_handler(text='obuna:xiva')
async def inline_follow1(call: CallbackQuery):
    scheduler_xiva.start()
    await call.message.edit_reply_markup(reply_markup=obunaInlineX)
    name = call.from_user.full_name
    try:
        db_obuna.add_user(id=call.from_user.id,
                          name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")

@dp.callback_query_handler(text='ochir:xiva')
async def inline_follow1(call: CallbackQuery):
    scheduler_xiva.shutdown()
    await call.message.edit_reply_markup(reply_markup=namozVaqtInlineX)
    name = call.from_user.full_name
    try:
        db_obuna.delete_user(id=call.from_user.id,
                             name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS, text=f"{err}")








