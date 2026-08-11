import logging
from pyrogram import filters
from pyrogram.types import Message
from config.constants import prefix
from utils.db import db

@Client.on_message(filters.command("setprefix", prefixes=prefix) & filters.me)
async def set_prefix_command(client, message: Message):
    new_prefix = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else None
    if not new_prefix:
        await message.edit("**Usage:** `.setprefix <new_prefix>`")
        return
    db.set("core.config", "prefix", new_prefix)
    await message.edit(f"**Prefix updated to:** `{new_prefix}`")

@Client.on_message(filters.command("prefix", prefixes=prefix) & filters.me)
async def get_prefix_command(client, message: Message):
    current = db.get("core.config", "prefix", prefix)
    await message.edit(f"**Current prefix:** `{current}`")