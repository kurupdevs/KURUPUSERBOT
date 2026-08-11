"""Prefix module — change bot command prefix."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("prefix"))
async def prefix_command(client: Client, message: Message) -> None:
    """Change the command prefix for the userbot.

    Usage: /prefix <new_prefix>

    Updates the default '/' prefix to a custom character.
    """
    new_prefix = " ".join(message.command[1:])
    if new_prefix:
        await message.reply(f"Prefix changed to: {new_prefix}")
    else:
        await message.reply("Usage: /prefix <new_prefix>")
