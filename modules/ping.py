"""Ping module — measure bot response latency."""

import time

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("ping"))
async def ping_command(client: Client, message: Message) -> None:
    """Measure and display bot response time in milliseconds.

    Replies with 'Pong!' then edits to show the round-trip
    latency between sending and receiving the reply.
    """
    start = time.time()
    msg = await message.reply("Pong!")
    end = time.time()
    await msg.edit(f"Pong! `{round((end - start) * 1000, 2)}ms`")
