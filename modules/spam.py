import asyncio
import logging
from pyrogram import filters
from pyrogram.types import Message
from config.constants import prefix

@Client.on_message(filters.command("spam", prefixes=prefix) & filters.me)
async def spam_command(client, message: Message):
    args = message.text.split(None, 2)
    if len(args) < 3:
        await message.edit("**Usage:** `.spam <count> <text>`")
        return
    try:
        count = int(args[1])
    except ValueError:
        await message.edit("**Invalid count. Must be a number.**")
        return
    text = args[2]
    await message.delete()
    for _ in range(min(count, 50)):
        await client.send_message(message.chat.id, text)
        await asyncio.sleep(0.5)