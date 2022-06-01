from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

adminMenu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Barcha userlar'),
            KeyboardButton(text='Userlar soni'),
        ],
        [
            KeyboardButton(text="send")
        ]
    ],
    resize_keyboard=True
)