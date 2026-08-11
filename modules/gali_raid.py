# Gali raid module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("gali"))
async def gali_command(client: Client, message: Message):
    await message.reply("Gali raid initiated!")
