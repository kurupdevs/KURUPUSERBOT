import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message


async def setup(client: Client):
    client.on_message(filters.command("carbon", prefixes=".") & filters.me)(carbon_handler)


async def carbon_handler(client: Client, message: Message):
    text = message.text.split(None, 1)
    if len(text) < 2:
        await message.edit("**Usage:** `.carbon <code>`")
        return
    code = text[1]
    await message.edit("**Generating carbon...**")
    url = f"https://carbon.now.sh/?code={code.replace(' ', '+')}"
    await message.edit(f"**Carbon URL:** {url}")
