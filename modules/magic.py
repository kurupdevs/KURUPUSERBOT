# Magic tricks module
from pyrogram import Client, filters
from pyrogram.types import Message
import random

@Client.on_message(filters.command("magic"))
async def magic_command(client: Client, message: Message):
    responses = ["Yes", "No", "Maybe", "Ask again later"]
    await message.reply(random.choice(responses))
