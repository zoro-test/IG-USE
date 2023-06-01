from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, message):
	user = await bot.get_me()
	mention = user["mention"]
	await bot.send_message(
		.chat.id,
		Data.START.format(msg.from_user.mention, mention),
		reply_markup=InlineKeyboardMarkup(Data.buttons)
	)
