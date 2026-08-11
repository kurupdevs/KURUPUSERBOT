"""Shayari module — random Urdu/Hindi poetry."""

import random

from pyrogram import Client, filters
from pyrogram.types import Message

_SHAYARI = [
    "Dil ko kya pata tha mohabbat ka naam hoga",
    "Zindagi ek safar hai suhana",
]


@Client.on_message(filters.command("shayari"))
async def shayari_command(client: Client, message: Message) -> None:
    """Send a random shayari (poetry couplet).

    Picks a random shayari from the built-in collection
    and replies with it.
    """
    await message.reply(random.choice(_SHAYARI))
