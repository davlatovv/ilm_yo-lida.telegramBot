import schedule
import requests

from data.config import BOT_TOKEN
from loader import db_obuna
from data.dataNamaz import db

ids = db_obuna.select_all_users()
for i in range(len(ids)):
    ids[i] = ids[i][0]

CHAT_IDS = ids
TOKEN = BOT_TOKEN
counter = 0


def send_text(token:str, chat_id_list: list, text: str):
    for chat_id in chat_id_list:
        requests.post(
            url=f'https://api.telegram.org/bot{token}/sendMessage',
            data={'chat_id': chat_id, 'text': text}
        )


def bomdod():
    global counter
    send_text(TOKEN, CHAT_IDS, "🌌Bomdod vaqti bo'ldi! \n\n«Albatta, namoz mo'minlarga vaqtida farz qilingandir»\n(Niso surasi 103-oyat)")
    counter += 1

def quyosh():
    global counter
    send_text(TOKEN, CHAT_IDS, "🌄Quyosh chiqdi!\n\nAbdulloh ibn Amr ibn Os roziyallohu anhudan rivoyat qilinadi:\n«Rasululloh sollallohu alayhi vasallamdan namozlarning vaqti haqida so‘raldi. Bas, u zot:\n«Bomdod namozining vaqti quyoshning avvalgi shoxi chiqmaguncha…» dedilar».")
    counter += 1


def peshin():
    global counter
    send_text(TOKEN, CHAT_IDS, "🌇Peshin vaqti bo'ldi! \n\n«Albatta, namoz mo'minlarga vaqtida farz qilingandir»\n(Niso surasi 103-oyat)")
    counter += 1


def asr():
    global counter
    send_text(TOKEN, CHAT_IDS, "🌆Asr vaqti bo'ldi! \n\n«Albatta, namoz mo'minlarga vaqtida farz qilingandir»\n(Niso surasi 103-oyat)")
    counter += 1


def shom():
    global counter
    send_text(TOKEN, CHAT_IDS, "🏙Shom vaqti bo'ldi! \n\n«Albatta, namoz mo'minlarga vaqtida farz qilingandir»\n(Niso surasi 103-oyat)")
    counter += 1


def xufton():
    global counter
    send_text(TOKEN, CHAT_IDS, "🌃Xufton vaqti bo'ldi! \n\n«Albatta, namoz mo'minlarga vaqtida farz qilingandir»\n(Niso surasi 103-oyat)")
    counter += 1


def set_namoz_time(b,q, p, a, sh, x):
    schedule.every().day.at(b).do(bomdod)
    schedule.every().day.at(q).do(quyosh)
    schedule.every().day.at(p).do(peshin)
    schedule.every().day.at(a).do(asr)
    schedule.every().day.at(sh).do(shom)
    schedule.every().day.at(x).do(xufton)
    while counter < 6:
        schedule.run_pending()

'''Samarqand'''
samarqand = dict(db.get_samarqand()[0])
keysS = [*samarqand.keys()]
valueS = [*samarqand.values()]

set_namoz_time(valueS[6],valueS[7],valueS[8],valueS[9],valueS[10],valueS[11])