from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

namozMenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Namoz vaqtlari⏰'),
        ],
        [
            KeyboardButton(text="G'usl va Tahorat🚰"),
            KeyboardButton(text='Namoz turlari🧎')
        ],
        [
            KeyboardButton(text='Zam suralar📖'),
            KeyboardButton(text='Bosh menu⬅️')
        ],
    ],
    resize_keyboard=True
)