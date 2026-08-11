# UPL module
from pyrogram import Client, filters
from pyrogram.types import Message
import os

@Client.on_message(filters.command("upl"))
async def upl_command(client: Client, message: Message):
    path = " ".join(message.command[1:])
    if not path:
        await message.reply("Usage: /upl <path>")
        return
    if os.path.exists(path):
        await client.send_document(message.chat.id, path)
    else:
        await message.reply("File not found.")
