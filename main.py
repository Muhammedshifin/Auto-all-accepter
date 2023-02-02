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

START_MSG = "<b>Hai {},\nI'm a private bot of MaSTeR to Accept All users in one time</b>"
CHAT = "#chatid*


@Bot.on_message(filters.command('start') & filters.private)
async def def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))
    
@Bot.on_message(filters.command("run") & filters.user(ADMINS))
async def accept(bot, message):
    lol = await message.reply_text(
        text ='Proccesing'
    )
    await User.approve_all_chat_join_requests(CHAT)
    await lol.edit(f"Completed")
    print("Completed")
    
 

User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")

