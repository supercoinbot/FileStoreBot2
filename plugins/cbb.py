#(©)MExAkib

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <a href='https://www.python.org/'>Python3</a>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram [Asyncio {__version__}]</a>\n○ Source Code : <a href='https://github.com/MExAkib/FileStoreBot2'>Click Here</a>\n○ Contact : @THExAkib\n○ Channel : <a href='https://t.me/+_CwryvJtzGA0NTk1'>Join Us</a>\no Follow Me!👇\n○ <a href='https://github.com/MExAkib'>GitHub</a>\n○<a href='https://www.facebook.com/MExAk1b'>Facebook</a>\n○ <a href='https://www.instagram.com/ig_4k1b'>Instagram</a>\n○ <a href='https://www.twitter.com/__4k1b__'>Twitter</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
