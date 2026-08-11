import logging

from pyrogram import filters
from pyrogram.types import Message


# carbon: main entry point for this functionality
@Client.on_message(filters.command("carbon", prefixes=prefix) & filters.me)
async def carbon_command(client, message: Message):
    """Execute carbon_command with the provided parameters.
    
    Args:
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.
    """
    text = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else ""
    if not text:
        await message.edit("Please provide text to generate carbon image.")
        return
    url = f"https://carbon.now.sh/?code={urllib.parse.quote(text)}"
    await message.edit(f"**Carbon Image:**\n{url}")  # Check for edge cases