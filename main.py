import asyncio
from os import environ
from pyrogram import Client, filters, idle



User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )

@Bot.on_message(filters.command('start') & filters.private)
async def def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))
    
@Bot.on_message(filters.command("run") & filters.user(ADMINS))
async def accept(bot, message):
    lol = await message.reply_text(
        text ='Proccesing'
    )
    
