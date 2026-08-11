# Shell command module
from pyrogram import Client, filters
from pyrogram.types import Message
import subprocess

@Client.on_message(filters.command("shell"))
async def shell_command(client: Client, message: Message):
    cmd = " ".join(message.command[1:])
    if cmd:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        await message.reply(f"```\n{result.stdout}\n```")
