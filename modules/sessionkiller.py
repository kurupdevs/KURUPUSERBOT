# Session Killer module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("sessionkiller"))
async def sessionkiller_command(client: Client, message: Message):
    await message.reply("Session killer ready!")
