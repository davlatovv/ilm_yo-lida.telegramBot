from aiogram import executor

from loader import dp, db_obuna, db

import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands



async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)
    #users data

    try:
        db.create_table_users()
    except Exception as err:
        print(err)
    #Data ochish uchun
    try:
        db_obuna.create_table_users()
    except Exception as err:
        print(err)


    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


"""FOR OBUNA/NAMAZ"""
import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


def toshkent():
    os.system('python obuna_namaz/toshkent.py')
def andijon():
    os.system('python obuna_namaz/andijon.py')
def buxoro():
    os.system('python obuna_namaz/buxoro.py')
def guliston():
    os.system('python obuna_namaz/guliston.py')
def jizzax():
    os.system('python obuna_namaz/jizzax.py')
def margilon():
    os.system('python obuna_namaz/margilon.py')
def namangan():
    os.system('python obuna_namaz/namangan.py')
def navoi():
    os.system('python obuna_namaz/navoi.py')
def nukus():
    os.system('python obuna_namaz/nukus.py')
def qarshi():
    os.system('python obuna_namaz/qarshi.py')
def qoqon():
    os.system('python obuna_namaz/qoqon.py')
def samarqand():
    os.system('python obuna_namaz/samarqand.py')
def xiva():
    os.system('python obuna_namaz/xiva.py')


scheduler_toshkent = BackgroundScheduler()
scheduler_andijon = BackgroundScheduler()
scheduler_buxoro = BackgroundScheduler()
scheduler_guliston = BackgroundScheduler()
scheduler_jizzax = BackgroundScheduler()
scheduler_margilon = BackgroundScheduler()
scheduler_namangan = BackgroundScheduler()
scheduler_navoi = BackgroundScheduler()
scheduler_nukus = BackgroundScheduler()
scheduler_qarshi = BackgroundScheduler()
scheduler_qoqon = BackgroundScheduler()
scheduler_samarqand = BackgroundScheduler()
scheduler_xiva = BackgroundScheduler()

trigger = CronTrigger(
    year="*", month="*", day="*", hour="01", minute="01", second="1"
)
scheduler_toshkent.add_job(toshkent, trigger=trigger)
scheduler_andijon.add_job(toshkent, trigger=trigger)
scheduler_buxoro.add_job(toshkent, trigger=trigger)
scheduler_guliston.add_job(toshkent, trigger=trigger)
scheduler_jizzax.add_job(toshkent, trigger=trigger)
scheduler_margilon.add_job(toshkent, trigger=trigger)
scheduler_namangan.add_job(toshkent, trigger=trigger)
scheduler_navoi.add_job(toshkent, trigger=trigger)
scheduler_nukus.add_job(toshkent, trigger=trigger)
scheduler_qarshi.add_job(toshkent, trigger=trigger)
scheduler_qoqon.add_job(toshkent, trigger=trigger)
scheduler_samarqand.add_job(toshkent, trigger=trigger)
scheduler_xiva.add_job(toshkent, trigger=trigger)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

