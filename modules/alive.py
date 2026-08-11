"""Alive module — display bot uptime and status."""

from pyrogram import Client, filters
from pyrogram.types import Message

from core.utils import up
from config.constants import V


@Client.on_message(filters.command("alive"))
async def alive_command(client: Client, message: Message) -> None:
    """Show the userbot's current status and uptime.

    Replies with version, uptime, and a confirmation
    that the bot is running.
    """
    await message.reply(
        f"KURUPUSERBOT v{V}\n"
        f"Status: Alive\n"
        f"Uptime: {up()}"
    )
