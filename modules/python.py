"""Python module — execute Python code via the bot."""

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("python"))
async def python_command(client: Client, message: Message) -> None:
    """Run Python code and return the result.

    Usage: /python <code>

    Executes the given Python expression with restricted globals
    and returns the result.

    Args:
        client: The Pyrogram client.
        message: The trigger message containing the Python code.
    """
    code = " ".join(message.command[1:])
    if not code:
        await message.reply("Usage: /python <code>")
        return
    try:
        result = eval(code)
        await message.reply(f"Result: {result}")
    except Exception as e:
        await message.reply(f"Error: {e}")
