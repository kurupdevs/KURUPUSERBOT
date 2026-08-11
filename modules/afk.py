"""AFK module — auto-reply when you're away from keyboard."""

import time

from pyrogram import Client, filters
from pyrogram.types import Message

AFK_DATA: dict = {}
"""In-memory store of AFK status per user ID."""


@Client.on_message(filters.command("afk"))
async def afk_command(client: Client, message: Message) -> None:
    """Set yourself as AFK with an optional reason.

    Usage: /afk [reason]

    Stores the user's AFK state in memory so other handlers
    can auto-reply when that user is mentioned.
    """
    reason = " ".join(message.command[1:]) or "No reason"
    AFK_DATA[message.from_user.id] = {"reason": reason, "time": time.time()}
    await message.reply(f"You are now AFK. Reason: {reason}")
