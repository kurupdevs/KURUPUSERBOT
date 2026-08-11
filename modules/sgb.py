import logging
from pyrogram import filters
from pyrogram.types import Message
from config.constants import prefix

@Client.on_message(filters.command("sgb", prefixes=prefix) & filters.me)
async def sgb_command(client, message: Message):
    text = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else ""
    if not text and not message.reply_to_message:
        await message.edit("**Usage:** `.sgb <text>` or reply to a message")
        return
    if message.reply_to_message:
        text = message.reply_to_message.text or ""
    parts = text.split(":", 1)
    name = parts[0].strip() if parts else "User"
    msg = parts[1].strip() if len(parts) > 1 else text
    await message.delete()
    await client.send_message(message.chat.id, f"**{name}:** {msg}")