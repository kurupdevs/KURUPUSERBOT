import logging
from pyrogram import filters
from pyrogram.types import Message
from config.constants import prefix

@Client.on_message(filters.command("info", prefixes=prefix) & filters.me)
async def user_info_command(client, message: Message):
    target = message.reply_to_message.from_user if message.reply_to_message else message.from_user
    user = await client.get_users(target.id)
    info_text = (
        f"**User Information**\n\n"
        f"👤 Name: {user.first_name} {user.last_name or ''}\n"
        f"🆔 ID: `{user.id}`\n"
        f"👤 Username: @{user.username or 'N/A'}\n"
        f"📱 Phone: {user.phone_number or 'N/A'}\n"
        f"🤖 Bot: {'Yes' if user.is_bot else 'No'}\n"
        f"🔒 Premium: {'Yes' if user.is_premium else 'No'}\n"
    )
    await message.edit(info_text)