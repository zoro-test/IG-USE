from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start_command(bot, message):
	
	user = await bot.get_me()
	mention = user["mention"]
	await bot.send_message(
		essage.id,
		Data.START.format(Message.from_user.id, mention),
		reply_markup=InlineKeyboardMarkup(Data.buttons)
	)
