"""Example module — demonstrates bot module structure."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("example"))
async def example_command(client: Client, message: Message) -> None:
    """Example command demonstrating module structure.

    Replies with a confirmation that the example module works.
    """
    await message.reply("This is an example module!")


@Client.on_message(filters.command("source"))
async def source_command(client: Client, message: Message) -> None:
    """Show the source repository URL."""
    await message.reply("github.com/kurupdevs/KURUPUSERBOT")
