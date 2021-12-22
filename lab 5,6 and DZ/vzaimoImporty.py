from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()

#tok=os.getenv('TOKEN')
#print(tok)

#bot = Bot(token=os.getenv('TOKEN'))
bot=Bot(token="[DELETED]")

dp = Dispatcher(bot, storage=storage)

