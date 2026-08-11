# Session killer module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("killsession"))
async def killsession_command(client: Client, message: Message):
    await message.reply("Session killed.")
