from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

sbsend = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='01', callback_data='s1'),
            InlineKeyboardButton(text='02', callback_data='s2'),
            InlineKeyboardButton(text='03', callback_data='s3'),
            InlineKeyboardButton(text='04', callback_data='s4'),
            InlineKeyboardButton(text='05', callback_data='s5'),

        ],
        [
            InlineKeyboardButton(text='06', callback_data='s6'),
            InlineKeyboardButton(text='07', callback_data='s7'),
            InlineKeyboardButton(text='08', callback_data='s8'),
            InlineKeyboardButton(text='09', callback_data='s9'),
            InlineKeyboardButton(text='10', callback_data='s10'),

        ],


    ])