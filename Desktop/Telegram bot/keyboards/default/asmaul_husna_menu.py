from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ismlarMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Allohning 99 ismi'),
            KeyboardButton(text="Ma'nolari")
        ],
        [
            KeyboardButton(text='Bosh menu⬅️')
        ],
    ],
    resize_keyboard=True
)