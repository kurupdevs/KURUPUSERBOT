import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message

HACK_ANIMATIONS = [
    "Initializing hack sequence...",
    "Connecting to target... ✅",
    "Bypassing firewall... [████████░░] 80%",
    "Decrypting password... ********",
    "Access granted! 🎯 Target compromised.",
]


async def setup(client: Client):
    client.on_message(filters.command("fakehack", prefixes=".") & filters.me)(fake_hack_handler)


async def fake_hack_handler(client: Client, message: Message):
    await message.edit("🔴 **Starting hack...**")
    for line in random.choice([HACK_ANIMATIONS]):
        await message.edit(line)
        await asyncio.sleep(0.8)
    await message.edit("✅ **Hack complete!** (just kidding 😂)")
