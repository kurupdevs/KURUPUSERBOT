"""Laugh module — send random laughing reactions."""

import random

from pyrogram import Client, filters
from pyrogram.types import Message

_LAUGHS = ["Ha", "He", "Ho", "Lol", "Xdd"]


@Client.on_message(filters.command("laugh"))
async def laugh_command(client: Client, message: Message) -> None:
    """Send a random laughing expression.

    Picks a random laugh string from the collection and replies.
    """
    await message.reply(random.choice(_LAUGHS))
