import typing
from datetime import datetime, timedelta

from data.config import (
    NUMBER_DAYS_FROM_ONE_PAYMENT,
    REFERAL_REWARD,
    SUBSCRIBE_AMOUNT_BY_PLANS,
)
from database import transactions, users
from keyboards import reply
from utils import tronscan_service

if typing.TYPE_CHECKING:
    import aiogram


async def task(bot: "aiogram.Bot"):
    transactions_records = await transactions.get_new()
    for transaction in transactions_records:

        await transactions.set_status(True, database_id=transaction.id)


        user = await users.get(telegram_id=transaction.owner_telegram_id)
        current_end_date = datetime.strptime(user.days_sub_end, "%Y-%m-%d %H:%M:%S")
        new_end_date = current_end_date + timedelta(days=NUMBER_DAYS_FROM_ONE_PAYMENT * transaction.months)

        await users.update_subscription_date(
            date=new_end_date.strftime("%Y-%m-%d %H:%M:%S"),
            telegram_id=transaction.owner_telegram_id,
        )
        await bot.send_message(
            chat_id=transaction.owner_telegram_id,
            text="Congratulations, you now have access to limited functionality.",
            reply_markup=await reply.close_functionality(),
        )

