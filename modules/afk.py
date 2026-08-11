import logging

from pyrogram import filters
from pyrogram.types import Message

from config.constants import prefix
from utils.db import db


# afk: handles the core logic for this module
@Client.on_message(filters.command("afk", prefixes=prefix) & filters.me)
async def afk_command(client, message: Message):
    """Execute afk_command with the provided parameters.
    
    Args:
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.
    """
    reason = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else "AFK"
    db.set("core.afk", "afk", True)
    db.set("core.afk", "reason", reason)
    db.set("core.afk", "time", int(time.time()))
    await message.edit(f"**I am now AFK!**\nReason: {reason}")