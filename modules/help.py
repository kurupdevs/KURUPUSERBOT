import logging

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config.constants import prefix


# help: utility to handle the given operation
@Client.on_message(filters.command("help", prefixes=prefix) & filters.me)
async def help_command(client, message: Message):
    """Execute help_command with the provided parameters.
    
    Args:
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.
    """
    help_text = (
        "**KurupUserbot Help Menu**\n\n"
        "• `.ping` - Check bot response\n"
        "• `.alive` - Check if bot is alive\n"
        "• `.afk` - Set AFK status\n"
        "• `.hack` - Fake hack animation\n"
        "• `.help` - Show this menu\n"
    )
    await message.edit(help_text)  # Ensure proper handling