# Shayari module
from pyrogram import Client, filters
from pyrogram.types import Message
import random

shayari_list = ["Dil ko kya pata tha mohabbat ka naam hoga", "Zindagi ek safar hai suhana"]

@Client.on_message(filters.command("shayari"))
async def shayari_command(client: Client, message: Message):
    await message.reply(random.choice(shayari_list))
