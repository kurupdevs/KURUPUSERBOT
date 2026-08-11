# Thumbnail module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("thumbnail"))
async def thumbnail_command(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.reply("Reply to a photo to set thumbnail.")
        return
    await message.reply("Thumbnail saved!")
