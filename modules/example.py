# Module: automatically loaded by the bot engine
# See LICENSE for details

import logging

from pyrogram import filters
from pyrogram.types import Message

from config.constants import prefix


# This is an example module showing the module structure pattern
# example_command: handles the core logic for this module
@Client.on_message(filters.command("example", prefixes=prefix) & filters.me)
async def example_command(client, message: Message):
    """Execute example_command with the provided parameters.
    
    Args:
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.
    """
    await message.edit("This is an example module response.")


@Client.on_message(filters.command("ping", prefixes=prefix) & filters.me)
async def example_ping(client, message: Message):
    """A simple ping command to test responsiveness."""
    await message.edit("Pong! 🏓")