from aiogram.types import Message, ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.admin import adminMenu
from keyboards.inline.regionsInline import regionInline
from aiogram.dispatcher.filters import Command



from loader import dp

@dp.message_handler(text_contains='Namoz vaqtlari⏰')
async def show_menu(message: Message):
    await message.answer('Mintaqa❓',reply_markup=regionInline)

@dp.message_handler(Command("admins"),user_id=ADMINS)
async def show_menu(message: Message):
    await message.answer("Admin menu",reply_markup=adminMenu)