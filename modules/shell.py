"""Shell module — run terminal commands via the bot."""

import subprocess

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("shell"))
async def shell_command(client: Client, message: Message) -> None:
    """Execute a shell command and return the output.

    Usage: /shell <command>

    Runs the command via subprocess and replies with stdout.

    Args:
        client: The Pyrogram client.
        message: The trigger message containing the command.
    """
    cmd = " ".join(message.command[1:])
    if cmd:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True
        )
        await message.reply(f"```\n{result.stdout}\n```")
