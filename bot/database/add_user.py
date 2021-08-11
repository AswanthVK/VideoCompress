from bot.localisation import Localisation
#from helpers.database.access_db import db
from bot.database import Database
from bot import BIN_CHANNEL
from pyrogram import Client
from pyrogram.types import Message
from bot import (
  DATABASE_URL,
  SESSION_NAME
  )

db = Database(DATABASE_URL, SESSION_NAME)

async def AddUserToDatabase(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        if BIN_CHANNEL is not None:
            await bot.send_message(
                int(BIN_CHANNEL),
                #f"#NEW_USER: \n\nNew User [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id}) started @{(await bot.get_me()).username} !!"
                f"#NEW_USER: \n\nNew User <code>{cmd.from_user.first_name}</code> started @{(await bot.get_me()).username} !!"
            )
