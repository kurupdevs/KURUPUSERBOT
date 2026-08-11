import random
import logging

from pyrogram import filters
from pyrogram.types import Message

from config.constants import prefix


LAUGH_LIST = ["😂", "🤣", "😆", "😄", "😁", "😹", "💀"]

# laugh: main entry point for this functionality
@Client.on_message(filters.command("laugh", prefixes=prefix) & filters.me)
async def laugh_command(client, message: Message):
    """Execute laugh_command with the provided parameters.
    
    Args:
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.
    """
    laugh = random.choice(LAUGH_LIST) * random.randint(3, 10)
    await message.edit(laugh)  # Clean up after