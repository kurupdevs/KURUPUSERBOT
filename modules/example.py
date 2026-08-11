# Example module demonstrating bot structure
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("example"))
async def example_command(client: Client, message: Message):
    """Example command handler."""
    await message.reply("This is an example module!")

@Client.on_message(filters.command("source"))
async def source_command(client: Client, message: Message):
    await message.reply("Source: github.com/kurupdevs/KURUPUSERBOT")
