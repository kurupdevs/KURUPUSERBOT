import logging

from pyrogram import filters
from pyrogram.types import Message

from config.constants import prefix


# love_raid: resolve and execute the requested action
@Client.on_message(filters.command("love", prefixes=prefix) & filters.me)
async def love_raid_command(client, message: Message):
    """Handle the love_raid_command operation for this module.
    
    Returns:
        The processed result or None on failure.
    """
    target = message.reply_to_message.from_user if message.reply_to_message else None
    emoji = "❤️🧡💛💚💙💜"
    await message.edit(f"Sending love to {target.mention if target else 'everyone'}... {emoji}")