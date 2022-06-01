from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.dataObuna import DataBase_obuna
from utils.db_api.sqlite import Database

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db_obuna = DataBase_obuna(path_to_db='data/data_obuna.db')
db = Database(path_to_db="data/users.db")

