#mport sqlite3 as sq
from bot_create import bot
import psycopg2 as ps
import os

def sql_start():
    global base, cursor_base
    base = ps.connect(os.environ.get('DATABASE_URL'), sslmode='require')
    cursor_base = base.cursor()
    #if base:
    #   print('Base OK')
    #cursor_base.execute('CREATE TABLE IF NOT EXISTS recipes(photo TEXT, description TEXT PRIMARY_KEY, recipe TEXT)')
    #base.commit()

async def sql_add(state):
    async with state.proxy() as data:
        cursor_base.execute(f"INSERT INTO recipes VALUES ({tuple(data.values())})")
        base.commit()

async def sql_read(message):
    for return_recipe in cursor_base.execute("SELECT * FROM recipes").fetchall():
        await bot.send_photo(message.from_user.id, return_recipe[0], f'{return_recipe[1]}\n{return_recipe[2]}')

async def sql_read2():
    return cursor_base.execute("SELECT * FROM recipes").fetchall()

async def sql_delete(data):
    cursor_base.execute("DELETE FROM recipes WHERE Name == ?", (data,))
    base.commit()

