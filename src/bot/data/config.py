import os
from pathlib import Path

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

database_filename = "database.db"
schema_filename = "database_schema.sql"
project_filepath = Path(__file__).resolve().parent.parent.parent

sqlite_database_filepath = os.path.join(project_filepath, "db", database_filename)
sqlite_schema_filepath = os.path.join(project_filepath, "db", schema_filename)


USDT_TRC20_WALLET_ADDRESS = "TF8aSMqpwtniPN77wS2EZTTcUKaaJhyorb"

# Key - count months
# Value - subscribe amount
SUBSCRIBE_AMOUNT_BY_PLANS = {
    1: 5,
}
NUMBER_DAYS_FROM_ONE_PAYMENT = 30
SUBSCRIBE_END_NOTIFICATION_DAYS = [7, 3, 1]
REFERAL_REWARD = 5

ADMINS_ID_LIST = [1]
private_channels = {
    "Channel 1": {"id": -1234567890, "invite_url": "https://t.me/+arsengirgoryan"},
    "Channel 2": {"id": -1234567890, "invite_url": "https://t.me/+arsengirgoryan"},
    "Channel 3": {"id": -1234567890, "invite_url": "https://t.me/+arsengirgoryan"},
}

MAILING_TEXT = "Hello"
