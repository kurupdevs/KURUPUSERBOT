# Shayari module for poetry sharing
from pyrogram import Client, filters
from pyrogram.types import Message
import random

SHAYARI = [
    "Dil dhadakta hai teri yaad mein...",
    "Mohabbat mein hum kya karein...",
    "Zindagi ek safar hai suhana...",
]

@Client.on_message(filters.command("shayari"))
async def shayari_command(client: Client, message: Message):
    await message.reply(random.choice(SHAYARI))
