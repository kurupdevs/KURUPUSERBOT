"""Help module — display available commands."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("help"))
async def help_command(client: Client, message: Message) -> None:
    """Show a list of available bot commands.

    Replies with the supported commands:
    /help, /ping, /afk, /alive
    """
    await message.reply(
        "kurupuserbot Commands:\n"
        "/help - Show this help\n"
        "/ping - Check latency\n"
        "/afk - Set AFK\n"
        "/alive - Show status"
    )
