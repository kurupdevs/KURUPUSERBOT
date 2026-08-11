# Help module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    """Show help information."""
    await message.reply("Available commands: /help, /ping, /afk, /alive")
