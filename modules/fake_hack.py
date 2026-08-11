"""Fake Hack module — simulated hacking animation."""

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("hack"))
async def hack_command(client: Client, message: Message) -> None:
    """Simulate a hacking sequence with a typing animation.

    Edits the message through several 'hacking' stages
    to create a fun fake hack effect.

    Args:
        client: The Pyrogram client.
        message: The trigger message.
    """
    msg = await message.reply("Starting hack...")
    for stage in (
        "Connecting to server...",
        "Bypassing firewall...",
        "Injecting payload...",
        "Access granted!",
    ):
        await asyncio.sleep(1)
        await msg.edit(stage)
