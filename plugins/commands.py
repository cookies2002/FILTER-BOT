from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
from info import PICS, CHNL_LNK, GRP_LNK, SUPPORT_CHAT, CLONE_MODE
from database.users_chats_db import db
from Script import script  # for START_TXT

# Define your bot username and bot name manually here
U_NAME = "TechVJBot"
B_NAME = "Tech VJ Filter Bot"

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    try:
        await message.react(emoji=random.choice(["👋", "😊", "🔥"]), big=True)
    except:
        pass

    # For Groups
    if message.chat.type in ["group", "supergroup"]:
        buttons = [[
            InlineKeyboardButton('⤬ Add me to your group ⤬', url=f'http://t.me/{U_NAME}?startgroup=true')
        ],[
            InlineKeyboardButton('Support Group', url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton('Movie Group', url=GRP_LNK)
        ],[
            InlineKeyboardButton('Join Update Channel', url=CHNL_LNK)
        ]]
        await message.reply(
            script.START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, U_NAME, B_NAME),
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True
        )
        return

    # Private chat
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)

    buttons = [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about')
    ],[
        InlineKeyboardButton('Join Update Channel', url=CHNL_LNK)
    ]]
    if CLONE_MODE:
        buttons.append([InlineKeyboardButton('Create Your Own Clone Bot', callback_data='clone')])

    await message.reply_photo(
        photo=random.choice(PICS),
        caption=script.START_TXT.format(message.from_user.mention, U_NAME, B_NAME),
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=enums.ParseMode.HTML
    )
    
