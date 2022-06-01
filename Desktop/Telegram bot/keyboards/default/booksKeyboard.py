from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

booksMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Vijdon azobi'),
            KeyboardButton(text='Musulmonning odobi'),
        ],
        [
            KeyboardButton(text='Tarixi Muhammadiy'),
            KeyboardButton(text='Iymon'),
        ],        [
            KeyboardButton(text='Ibodati islomiya'),
            KeyboardButton(text='Oisha roziyallohu anhu'),
        ],        [
            KeyboardButton(text='Payg\'ambarlar tarixi'),
            KeyboardButton(text='Jannatga eltuvchi amallar'),
        ],
        [
            KeyboardButton(text='Saodat asri(4 tom)'),
            KeyboardButton(text='Bosh menu⬅️'),

        ],
    ],
    resize_keyboard=True
)
