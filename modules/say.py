# Say module
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("say"))
async def say_command(client: Client, message: Message):
    text = " ".join(message.command[1:])
    if not text:
        await message.reply("Usage: /say <text>")
        return
    await message.delete()
    await client.send_message(message.chat.id, text)
