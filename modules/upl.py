# Upload module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("upload"))
async def upload_command(client: Client, message: Message):
    await message.reply("Upload module ready.")
