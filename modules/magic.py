import random
import logging

from pyrogram import filters
from pyrogram.types import Message

from config.constants import prefix


MAGIC_RESPONSES = ["🎱 Yes", "🎱 No", "🎱 Maybe", "🎱 Definitely", "🎱 Not sure"]

# magic: utility to handle the given operation
@Client.on_message(filters.command("magic", prefixes=prefix) & filters.me)
async def magic_command(client, message: Message):
    """Execute magic_command with the provided parameters.
    
    Args:
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.
    """
    response = random.choice(MAGIC_RESPONSES)
    await message.edit(f"🎩 **Magic 8-Ball says:** {response}")  # Validate input