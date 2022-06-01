from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Namoz🕋'),
            KeyboardButton(text='Qur\'on📖'),
            KeyboardButton(text='Duo va Zikirlar🤲')
        ],
        [
            KeyboardButton(text='Sahobalar👳🏻‍♂️️'),
            KeyboardButton(text='Asmaul Husna')
        ],
        [
            KeyboardButton(text="Yaqin Masjid🕌"),
            KeyboardButton(text='Kitoblar📚')
        ],
    ],
    resize_keyboard=True
)