import logging
from pyrogram import filters
from pyrogram.types import Message
from config.constants import prefix

@Client.on_message(filters.command("vt", prefixes=prefix) & filters.me)
async def vt_command(client, message: Message):
    text = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else ""
    if not text:
        await message.edit("**Usage:** `.vt <text>`")
        return
    voice_text = text.upper().replace(" ", "  ")
    await message.delete()
    await client.send_message(message.chat.id, f"🗣️ **Voice Text:**\n\n{voice_text}")