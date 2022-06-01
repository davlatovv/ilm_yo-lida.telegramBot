from aiogram import types
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types import Message




from data.config import ADMINS
from loader import dp, db, bot





@dp.message_handler(text="Barcha userlar", user_id=ADMINS)
async def get_all_users (message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer (users)


@dp.message_handler(text="Userlar soni", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    count = db.count_users()[0]
    msg = f"Bazada {count}ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0],text=msg)


@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def clean_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")
#
# @dp.message_handler(text="/send",user_id=ADMINS)
# async def send(message: types.Message):
#     users = db.select_all_users()
#     for user in users:
#         user_id = user[0]
#         a = message.message_id
#         await bot.send_message(chat_id=user_id,text=a)





