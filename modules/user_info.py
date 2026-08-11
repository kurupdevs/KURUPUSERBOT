"""User Info module — display Telegram user details."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("info"))
async def info_command(client: Client, message: Message) -> None:
    """Display information about the current user.

    Shows the user's display name and Telegram ID.
    """
    user = message.from_user
    info_text = f"Name: {user.first_name}\nID: {user.id}"
    await message.reply(info_text)
