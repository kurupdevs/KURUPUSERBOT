# Laugh module
from pyrogram import Client, filters
from pyrogram.types import Message
import random

laughs = ["Ha", "He", "Ho", "Lol", "Xdd"]

@Client.on_message(filters.command("laugh"))
async def laugh_command(client: Client, message: Message):
    await message.reply(random.choice(laughs))
