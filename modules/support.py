# Support module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("support"))
async def support_command(client: Client, message: Message):
    await message.reply("Support: @kurupdevs\nChannel: @kurupchannel")
