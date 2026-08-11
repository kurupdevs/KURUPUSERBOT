# Sendmod module for file sending
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("sendmod"))
async def sendmod_command(client: Client, message: Message):
    await message.reply("Sendmod module ready.")
