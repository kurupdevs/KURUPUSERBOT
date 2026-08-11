"""Magic module — fun magic tricks and responses."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("magic"))
async def magic_command(client: Client, message: Message) -> None:
    """Perform a magic trick.

    Replies with a random magic-themed response.
    """
    await message.reply("✨ Magic! The bot is working!")
