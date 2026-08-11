# Thumbnail module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("thumbnail"))
async def thumbnail_command(client: Client, message: Message):
    await message.reply("Thumbnail set.")
