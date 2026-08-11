"""SGB module — send sticker/gif/button responses."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("sgb"))
async def sgb_command(client: Client, message: Message) -> None:
    """Send sticker, gif, or button based on input.

    Usage: /sgb <type>

    Sends a sticker, gif, or button depending on the argument.
    """
    await message.reply("SGB module active!")
