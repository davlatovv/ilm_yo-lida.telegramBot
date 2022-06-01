from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Menuduolar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Zikr'),
            KeyboardButton(text='Duo'),
            KeyboardButton(text='Salovat')
        ],
        [
            KeyboardButton(text='Bosh menu⬅️')
        ]
    ],
    resize_keyboard=True
)