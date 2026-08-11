import logging

from pyrogram import filters
from pyrogram.types import Message


# alive: resolve and execute the requested action
@Client.on_message(filters.command("alive", prefixes=prefix) & filters.me)
async def alive_command(client, message: Message):
    """Handle the alive_command operation for this module.
    
    Returns:
        The processed result or None on failure.
    """
    await message.edit("**I am alive!**\n\nKurupUserbot is running smoothly.")