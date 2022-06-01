from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from loader import dp


Keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                    KeyboardButton(text="lakatsiya yuboring",
                                                   request_location=True)
                                   ],
                                   [
                                    KeyboardButton(text='Bosh menu⬅️')
                                   ],
                               ])

@dp.message_handler(text='Yaqin Masjid🕌')
async def send_link(message: Message):
    await message.answer("Sizga eng yaqin masjidlar ro'yhati:", reply_markup=Keyboard)

