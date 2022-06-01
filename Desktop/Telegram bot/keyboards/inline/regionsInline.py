from  aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

regionInline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Toshkent', callback_data='toshkent'),
        ],
        [
            InlineKeyboardButton(text='Andijon', callback_data='andijon'),
            InlineKeyboardButton(text='Buxoro', callback_data='buxoro'),

        ],
        [
            InlineKeyboardButton(text='Guliston', callback_data='guliston'),
            InlineKeyboardButton(text='Samarqand', callback_data='samarqand'),

        ],
        [
            InlineKeyboardButton(text='Namangan', callback_data='namangan'),
            InlineKeyboardButton(text='Navoiy', callback_data='navoi'),

        ],
        [
            InlineKeyboardButton(text='Jizzax', callback_data='jizzax'),
            InlineKeyboardButton(text='Nukus', callback_data='nukus'),

        ],
        [
            InlineKeyboardButton(text='Qarshi', callback_data='qarshi'),
            InlineKeyboardButton(text='Qo\'qon', callback_data='qoqon'),
        ],
        [
            InlineKeyboardButton(text='Xiva', callback_data='xiva'),
            InlineKeyboardButton(text='Marg\'ilon', callback_data='margilon')
        ],
    ])

