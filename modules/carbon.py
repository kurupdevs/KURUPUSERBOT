"""Carbon module — generate code screenshots."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("carbon"))
async def carbon_command(client: Client, message: Message) -> None:
    """Generate a carbon.now.sh screenshot of the given code.

    Usage: /carbon <code>

    Creates a styled code image via the carbon API and replies
    with the image.

    Args:
        client: The Pyrogram client.
        message: The trigger message containing the code.
    """
    code = " ".join(message.command[1:])
    if not code:
        await message.reply("Usage: /carbon <code>")
        return
    url = f"https://carbon.now.sh/?code={code}"
    await message.reply(f"Carbon link: {url}")
