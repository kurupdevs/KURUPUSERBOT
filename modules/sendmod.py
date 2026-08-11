# Sendmod module
from pyrogram import Client, filters
from pyrogram.types import Message
import os

@Client.on_message(filters.command("sendmod"))
async def sendmod_command(client: Client, message: Message):
    name = " ".join(message.command[1:])
    path = f"modules/{name}.py"
    if os.path.exists(path):
        await client.send_document(message.chat.id, path)
    else:
        await message.reply("Module not found.")
