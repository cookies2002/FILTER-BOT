from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
from info import PICS, temp, script, CHNL_LNK, GRP_LNK, SUPPORT_CHAT, CLONE_MODE

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    try:
        await message.react(emoji="👋", big=True)
    except:
        pass

    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        buttons = [[
            InlineKeyboardButton('⤬ Add me to your group ⤬', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
        ],[
            InlineKeyboardButton('Support Group', url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton('Movie Group', url=GRP_LNK)
        ],[
            InlineKeyboardButton('Join Update Channel', url=CHNL_LNK)
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(
            script.START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
        return

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

    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(
        photo=random.choice(PICS),  # Make sure PICS list has valid image URLs
        caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )
    
