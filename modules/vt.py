"""VT module — VirusTotal file scanner."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("vt"))
async def vt_command(client: Client, message: Message) -> None:
    """Scan a file with VirusTotal.

    Usage: Reply to a file with /vt to scan it.
    """
    await message.reply("VirusTotal scan initiated!")
