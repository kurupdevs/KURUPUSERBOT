"""Gali Raid module — send gaali-themed raid messages."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("gali_raid"))
async def gali_raid_command(client: Client, message: Message) -> None:
    """Send a gaali-themed raid of messages.

    Sends a series of gaali (slang) messages to the chat.
    """
    await message.reply("Gali raid started!")
