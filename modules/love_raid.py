"""Love Raid module — send love-themed spam messages."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("love_raid"))
async def love_raid_command(client: Client, message: Message) -> None:
    """Send a love-themed raid of messages.

    Sends a series of heart and love emojis to the chat.
    """
    await message.reply("❤️ Love raid incoming! ❤️")
