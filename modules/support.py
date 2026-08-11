"""Support module — display support channel info."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("support"))
async def support_command(client: Client, message: Message) -> None:
    """Show support channel and contact information.

    Replies with links to the support group, channel,
    and developer contact.
    """
    await message.reply(
        "Support: @kurupdevs\nChannel: @kurupchannel"
    )
