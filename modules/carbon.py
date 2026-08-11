# Carbon image generation module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("carbon"))
async def carbon_command(client: Client, message: Message):
    await message.reply("Carbon module active.")
