import time
import logging

from pyrogram import filters
from pyrogram.types import Message

from config.constants import prefix


@Client.on_message(filters.command("ping", prefixes=prefix) & filters.me)
async def ping_command(client, message: Message):
    start = time.perf_counter()
    msg = await message.edit("**Pong!** 🏓")
    elapsed = time.perf_counter() - start
    await msg.edit(f"**Pong!** 🏓\nResponse time: `{elapsed:.3f}s`")