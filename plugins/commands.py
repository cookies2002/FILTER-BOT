from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_message(filters.command(["start"]))
async def start(client, message: Message):
    await message.reply_photo(
        photo="https://graph.org/file/2d3f285cf28737f30df19.jpg",
        caption=f"""Hello {message.from_user.mention} 👋

I am a Telegram Bot for Movie Channel.
You Can Watch Movies and Web Series From This Bot.

Click /help For More Details.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("My Channel", url="https://t.me/+zHCFO5MNUHc2NmU1")
                ],
                [
                    InlineKeyboardButton("My Group", url="https://t.me/Movies_Series_Mix")
                ]
            ]
        )
    )
    
