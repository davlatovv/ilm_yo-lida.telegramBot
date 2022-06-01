from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kbsend = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='01', callback_data='k1'),
            InlineKeyboardButton(text='02', callback_data='k2'),
            InlineKeyboardButton(text='03', callback_data='k3'),
            InlineKeyboardButton(text='04', callback_data='k4'),
            InlineKeyboardButton(text='05', callback_data='k5'),


        ],
        [
            InlineKeyboardButton(text='06', callback_data='k6'),
            InlineKeyboardButton(text='07', callback_data='k7'),
            InlineKeyboardButton(text='08', callback_data='k8'),
            InlineKeyboardButton(text='09', callback_data='k9'),
            InlineKeyboardButton(text='10', callback_data='k10'),



        ],


    ])