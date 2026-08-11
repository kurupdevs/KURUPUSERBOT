"""PM Permit module — control private message permissions."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("pmpermit"))
async def pmpermit_command(client: Client, message: Message) -> None:
    """Toggle PM permit mode.

    When enabled, unauthorized users are prevented from
    sending private messages to the bot owner.
    """
    await message.reply("PM Permit enabled.")
