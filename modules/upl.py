import os
import time
import logging
from pyrogram import filters
from pyrogram.types import Message
from config.constants import prefix

@Client.on_message(filters.command("upl", prefixes=prefix) & filters.me)
async def upl_command(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.media:
        await message.edit("**Reply to a media file to get the direct link.**")
        return
    start = time.perf_counter()
    msg = await message.edit("**Uploading...**")
    file_path = await client.download_media(message.reply_to_message)
    elapsed = time.perf_counter() - start
    await msg.edit(f"**Downloaded!**\nPath: `{file_path}`\nTime: `{elapsed:.2f}s`")