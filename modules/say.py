from pyrogram import Client, filters
from pyrogram.types import Message


async def setup(client: Client):
    client.on_message(filters.command("say", prefixes=".") & filters.me)(say_handler)


async def say_handler(client: Client, message: Message):
    text = message.text.split(None, 1)
    if len(text) < 2:
        await message.edit("**Usage:** `.say <text>`")
        return
    await message.delete()
    await client.send_message(message.chat.id, text[1])
