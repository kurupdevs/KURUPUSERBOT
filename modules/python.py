# Python execution module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("python"))
async def python_command(client: Client, message: Message):
    await message.reply("Python module active.")
