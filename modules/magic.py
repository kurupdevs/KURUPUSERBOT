import random
from pyrogram import Client, filters
from pyrogram.types import Message

MAGIC_RESPONSES = [
    "🎱 Yes definitely",
    "🎱 No way",
    "🎱 Ask again later",
    "🎱 Most likely",
    "🎱 Don't count on it",
    "🎱 Signs point to yes",
    "🎱 Very doubtful",
]


async def setup(client: Client):
    client.on_message(filters.command("magic", prefixes=".") & filters.me)(magic_handler)


async def magic_handler(client: Client, message: Message):
    question = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else "???"
    await message.edit(f"**Q:** {question}\n**A:** {random.choice(MAGIC_RESPONSES)}")
