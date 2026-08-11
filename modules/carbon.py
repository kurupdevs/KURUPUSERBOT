# Carbon module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("carbon"))
async def carbon_command(client: Client, message: Message):
    code = " ".join(message.command[1:])
    if not code:
        await message.reply("Usage: /carbon <code>")
        return
    url = f"https://carbon.now.sh/?code={code}"
    await message.reply(f"Carbon: {url}")
