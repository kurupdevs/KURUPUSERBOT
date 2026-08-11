# SGB module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("sgb"))
async def sgb_command(client: Client, message: Message):
    await message.reply("SGB module active!")
