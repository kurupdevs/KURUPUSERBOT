# Alive module
from pyrogram import Client, filters
from pyrogram.types import Message
from core.utils import up
from config.constants import V

@Client.on_message(filters.command("alive"))
async def alive_command(client: Client, message: Message):
    await message.reply(f"**KURUPUSERBOT v{V}**\nUptime: {up()}")
