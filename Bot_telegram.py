import os

from aiogram.utils import executor
from bot_create import dp, bot
from data_base.sqlite_db import sql_start
import config
import psycopg2 as ps

async def on_startup(dp):
    await bot.set_webhook(config.URL_APP)
    sql_start()

base = ps.connect(os.environ.get('DATABASE_URL'), sslmode='require')
cur = base.cursor()

async def on_shutdown(dp):
    await bot.delete_webhook()
    base.close()
    cur.close()

from Handlers import admin, client, commons
admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
commons.register_handlers_commons(dp)


executor.start_webhook(
    dispatcher=dp,
    webhook_path='',
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000)))