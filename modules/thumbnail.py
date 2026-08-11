import os
import logging
from pyrogram import filters
from pyrogram.types import Message
from config.constants import prefix

@Client.on_message(filters.command("thumbnail", prefixes=prefix) & filters.me)
async def thumbnail_command(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.edit("**Reply to an image to set as thumbnail.**")
        return
    photo = message.reply_to_message.photo
    file_path = await client.download_media(photo, file_name="thumbnail.jpg")
    await message.edit(f"**Thumbnail saved!** `{file_path}`")