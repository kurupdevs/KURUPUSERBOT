import random
from pyrogram import Client, filters
from pyrogram.types import Message

LAUGHS = [
    "😂😂😂", "🤣🤣🤣", "😆😆😆", "😹😹😹",
    "LMAO", "ROFL", "LOLOL", "HAHAHA",
]


async def setup(client: Client):
    client.on_message(filters.command("laugh", prefixes=".") & filters.me)(laugh_handler)


async def laugh_handler(client: Client, message: Message):
    count = min(int(message.text.split()[-1]) if message.text.split()[-1].isdigit() else 1, 5)
    await message.edit(random.choice(LAUGHS) * count)
