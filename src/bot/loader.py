import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from data.config import BOT_TOKEN
from logzero import logfile, logger
from utils import (
    ban_users_from_channels,
    decrease_subscription_days,
    subscription_checker,
)

if not os.path.exists("logs/"):
    os.system("mkdir logs")
logfile("logs/bot.log")
# BOT_TOKEN="7850411563:AAGYdZjrovj48VjFi-e_k20tKunreTs2AVw"
# bot = Bot(token="7850411563:AAGYdZjrovj48VjFi-e_k20tKunreTs2AVw", parse_mode=ParseMode.HTML)
bot = Bot(token="7850411563:AAGYdZjrovj48VjFi-e_k20tKunreTs2AVw", default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

tasks_scheduler = AsyncIOScheduler()
tasks_scheduler.add_job(subscription_checker.task, "interval", minutes=1, args=(bot,))
tasks_scheduler.add_job(
    decrease_subscription_days.task, "interval", days=1, args=(bot,)
)
tasks_scheduler.add_job(ban_users_from_channels.task, "interval", days=1, args=(bot,))
