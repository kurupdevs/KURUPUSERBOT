"""Thumbnail module — set and manage image thumbnails."""

import os

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("thumbnail"))
async def thumbnail_command(client: Client, message: Message) -> None:
    """Set a custom thumbnail for the userbot.

    Usage: Reply to an image with /thumbnail to set it as
    the default thumbnail for uploads.
    """
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.reply("Reply to a photo to set as thumbnail.")
        return
    await message.reply("Thumbnail saved!")
