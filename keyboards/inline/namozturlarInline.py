from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

namozTurlari = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='NAMOZ QOIDALARI', callback_data='namozqoidalari')
        ],
        [
            InlineKeyboardButton(text='FARZ NAMOZLAR', callback_data='farz')
        ],
        [
            InlineKeyboardButton(text='VOJIB NAMOZLAR', callback_data='vojib')
        ],
        [
            InlineKeyboardButton(text='SUNNAT NAMOZLAR', callback_data='sunnat')
        ],
        [
            InlineKeyboardButton(text='NAFL NAMOZLAR', callback_data='nafl')
        ],
    ])

namozQoidalari= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='', callback_data='')
        ]
    ])

farz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🌄️Bomdod Namozi', callback_data='f:bomdod')
        ],
        [
            InlineKeyboardButton(text='🌇Peshin Namozi', callback_data='f:peshin')
        ],
        [
            InlineKeyboardButton(text='🌆Asr Namozi', callback_data='f:asr')
        ],
        [
            InlineKeyboardButton(text='️🏙Shom Namozi', callback_data='f:shom')
        ],
        [
            InlineKeyboardButton(text='🌃Xufton Namozi', callback_data='f:xufton')
        ],
        [
            InlineKeyboardButton(text='Juma Namozi(Jamoat)', callback_data='juma')
        ],
        [
            InlineKeyboardButton(text='Janoza Namozi(Jamoat)', callback_data='janoza')
        ],
        [
            InlineKeyboardButton(text='Namoz turlariga⬅️', callback_data='namozturlariga')
        ],
    ])

vojib = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Vitr Namozi', callback_data='vitr')
        ],
        [
            InlineKeyboardButton(text='Ramazon va Qurbon Hayit Namozlari', callback_data='hayit')
        ],
        [
            InlineKeyboardButton(text='Baytullohdagi Tavof Namozi', callback_data='tavof')
        ],
        [
            InlineKeyboardButton(text='Namoz turlariga⬅️', callback_data='namozturlariga')
        ],
    ])

sunnat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🌄️Bomdod namozi', callback_data='s:bomdod')
        ],
        [
            InlineKeyboardButton(text='🌇Peshin namozi(4 rakat)', callback_data='s:peshin4')
        ],
        [
            InlineKeyboardButton(text='🌇Peshin namozi(2 rakat)', callback_data='s:peshin2')
        ],
        [
            InlineKeyboardButton(text='️🏙Shom namozi', callback_data='s:shom')
        ],
        [
            InlineKeyboardButton(text='🌃Xufton namozi', callback_data='s:xufton')
        ],
        [
            InlineKeyboardButton(text='Namoz turlariga⬅️', callback_data='namozturlariga')
        ],
    ])


nafl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Tahajjud namozi', callback_data='bomdod')
        ],
        [
            InlineKeyboardButton(text='Istixora namozi', callback_data='peshin')
        ],
        [
            InlineKeyboardButton(text='', callback_data='asr')
        ],
        [
            InlineKeyboardButton(text='', callback_data='shom')
        ],
        [
            InlineKeyboardButton(text='', callback_data='xufton')
        ],
        [
            InlineKeyboardButton(text='Namoz turlariga⬅️', callback_data='namozturlariga')
        ],
    ])

gusl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='G\'usl', callback_data='gusl')
        ],
        [
            InlineKeyboardButton(text='Tahorat', callback_data='tahorat')
        ],

    ])
