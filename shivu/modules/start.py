import random
from html import escape 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler

from shivu import application, PHOTO_URL, SUPPORT_CHAT, UPDATE_CHAT, BOT_USERNAME, db, GROUP_ID
from shivu import pm_users as collection 


async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    username = update.effective_user.username

    user_data = await collection.find_one({"_id": user_id})

    if user_data is None:
        
        await collection.insert_one({"_id": user_id, "first_name": first_name, "username": username})
        
        await context.bot.send_message(chat_id=GROUP_ID, 
                                       text=f"New user Started The Bot..\n User: <a href='tg://user?id={user_id}'>{escape(first_name)})</a>", 
                                       parse_mode='HTML')
    else:
        
        if user_data['first_name'] != first_name or user_data['username'] != username:
            
            await collection.update_one({"_id": user_id}, {"$set": {"first_name": first_name, "username": username}})

    

    if update.effective_chat.type== "private":
        
        
        caption = f"""
        ***𝐇𝐄𝐋𝐋𝐎...*** 💫

***I ᴀᴍ Aɴ Oᴘᴇɴ Sᴏᴜʀᴄᴇ Cʜᴀʀᴀᴄᴛᴇʀ Cᴀᴛᴄʜᴇʀ Bᴏᴛ..Aᴅᴅ Mᴇ ɪɴ Yᴏᴜʀ ɢʀᴏᴜᴘ.. Aɴᴅ I ᴡɪʟʟ sᴇɴᴅ Rᴀɴᴅᴏᴍ Cʜᴀʀᴀᴄᴛᴇʀs Aғᴛᴇʀ.. ᴇᴠᴇʀʏ 𝟷𝟶𝟶 ᴍᴇssᴀɢᴇs ɪɴ Gʀᴏᴜᴘ... Usᴇ /Guess ᴛᴏ.. Cᴏʟʟᴇᴄᴛ ᴛʜᴀᴛ Cʜᴀʀᴀᴄᴛᴇʀs ɪɴ Yᴏᴜʀ Cᴏʟʟᴇᴄᴛɪᴏɴ.. ᴀɴᴅ sᴇᴇ Cᴏʟʟᴇᴄᴛɪᴏɴ ʙʏ ᴜsɪɴɢ /Harem... Sᴏ ᴀᴅᴅ ɪɴ Yᴏᴜʀ ɢʀᴏᴜᴘs ᴀɴᴅ Cᴏʟʟᴇᴄᴛ Yᴏᴜʀ ʜᴀʀᴇᴍ.***
        """
        
        keyboard = [
            [InlineKeyboardButton("💞Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ💞", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("✨Sᴜᴘᴘᴏʀᴛ✨", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("Uᴘᴅᴀᴛᴇ💫", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs🌟", callback_data='help'),
            [InlineKeyboardButton("Sᴏᴜʀᴄᴇ 😁", url=f'https://t.me/Andi_mandi_sandi_tu_hai_randi/13')],
            [InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇᴅ💥", url=f'https://t.me/anime_fan_owner')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        photo_url = random.choice(PHOTO_URL)

        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption, reply_markup=reply_markup, parse_mode='markdown')

    else:
        photo_url = random.choice(PHOTO_URL)
        keyboard = [
            [InlineKeyboardButton("💞Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ💞", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("✨Sᴜᴘᴘᴏʀᴛ✨", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("Uᴘᴅᴀᴛᴇ💫", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs🌟", callback_data='help'),
            [InlineKeyboardButton("Sᴏᴜʀᴄᴇ 😁", url=f'https://t.me/Andi_mandi_sandi_tu_hai_randi/13')],
            [InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇᴅ💥", url=f'https://t.me/anime_fan_owner')]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption="🎴Alive!?... \n connect to me in PM For more information ",reply_markup=reply_markup )

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'help':
        help_text = """
    ***Help Section:***
    
***Help Section:
    
***/guess: Tᴏ Gᴜᴇss ᴄʜᴀʀᴀᴄᴛᴇʀ (ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘ)***
***/fav: Aᴅᴅ Yᴏᴜʀ ғᴀᴠ***
***/trade : Tᴏ ᴛʀᴀᴅᴇ Cʜᴀʀᴀᴄᴛᴇʀs***
***/gift: Gɪᴠᴇ ᴀɴʏ Cʜᴀʀᴀᴄᴛᴇʀ ғʀᴏᴍ Yᴏᴜʀ Cᴏʟʟᴇᴄᴛɪᴏɴ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴜsᴇʀ.. (ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs)***
***/collection: Tᴏ sᴇᴇ Yᴏᴜʀ Cᴏʟʟᴇᴄᴛɪᴏɴ***
***/topgroups : Sᴇᴇ Tᴏᴘ Gʀᴏᴜᴘs.. Pᴘʟ Gᴜᴇssᴇs Mᴏsᴛ ɪɴ ᴛʜᴀᴛ Gʀᴏᴜᴘs***
***/top: Tᴏᴏ Sᴇᴇ Tᴏᴘ Usᴇʀs***
***/ctop : Yᴏᴜʀ CʜᴀᴛTᴏᴘ***
***/changetime: Cʜᴀɴɢᴇ Cʜᴀʀᴀᴄᴛᴇʀ ᴀᴘᴘᴇᴀʀ ᴛɪᴍᴇ (ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ Gʀᴏᴜᴘs)***
   """
        help_keyboard = [[InlineKeyboardButton("⤾ Bᴀᴄᴋ", callback_data='back')]]
        reply_markup = InlineKeyboardMarkup(help_keyboard)
        
        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=help_text, reply_markup=reply_markup, parse_mode='markdown')

    elif query.data == 'back':

        caption = f"""
        ***𝐇𝐄𝐋𝐋𝐎...*** 💫

***I ᴀᴍ Aɴ Oᴘᴇɴ Sᴏᴜʀᴄᴇ Cʜᴀʀᴀᴄᴛᴇʀ Cᴀᴛᴄʜᴇʀ Bᴏᴛ..Aᴅᴅ Mᴇ ɪɴ Yᴏᴜʀ ɢʀᴏᴜᴘ.. Aɴᴅ I ᴡɪʟʟ sᴇɴᴅ Rᴀɴᴅᴏᴍ Cʜᴀʀᴀᴄᴛᴇʀs Aғᴛᴇʀ.. ᴇᴠᴇʀʏ 𝟷𝟶𝟶 ᴍᴇssᴀɢᴇs ɪɴ Gʀᴏᴜᴘ... Usᴇ /Guess ᴛᴏ.. Cᴏʟʟᴇᴄᴛ ᴛʜᴀᴛ Cʜᴀʀᴀᴄᴛᴇʀs ɪɴ Yᴏᴜʀ Cᴏʟʟᴇᴄᴛɪᴏɴ.. ᴀɴᴅ sᴇᴇ Cᴏʟʟᴇᴄᴛɪᴏɴ ʙʏ ᴜsɪɴɢ /Harem... Sᴏ ᴀᴅᴅ ɪɴ Yᴏᴜʀ ɢʀᴏᴜᴘs ᴀɴᴅ Cᴏʟʟᴇᴄᴛ Yᴏᴜʀ ʜᴀʀᴇᴍ***
        """

        
        keyboard = [
            [InlineKeyboardButton("💞Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ💞", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("✨Sᴜᴘᴘᴏʀᴛ✨", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("Uᴘᴅᴀᴛᴇ💫", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs🌟", callback_data='help'),
            [InlineKeyboardButton("SOURCE", url=f'https://t.me/Andi_mandi_sandi_tu_hai_randi/13'),
            [InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇᴅ💥", url=f'https://t.me/anime_fan_owner')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=caption, reply_markup=reply_markup, parse_mode='markdown')


application.add_handler(CallbackQueryHandler(button, pattern='^help$|^back$', block=False))
start_handler = CommandHandler('start', start, block=False)
application.add_handler(start_handler)
