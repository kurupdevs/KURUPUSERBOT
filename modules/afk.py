import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import Message

logger = logging.getLogger(__name__)

AFK_USERS = {}


async def setup(client: Client):
    client.on_message(filters.command("afk", prefixes=".") & filters.me)(afk_handler)
    client.on_message(filters.private & ~filters.me)(check_afk)


async def afk_handler(client: Client, message: Message):
    reason = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else "AFK"
    AFK_USERS[message.from_user.id] = reason
    await message.edit(f"**I'm AFK now:** {reason}")


async def check_afk(client: Client, message: Message):
    if message.from_user and message.from_user.id in AFK_USERS:
        await message.reply(f"User is AFK: {AFK_USERS[message.from_user.id]}")
