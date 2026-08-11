import random
from pyrogram import Client, filters
from pyrogram.types import Message

SHAYARIS = [
    "तेरी यादों ने हमें तन्हा कर दिया, वरना हम तो ख़ुश थे ज़माने की भीड़ में।",
    "दिल में तुम हो, दिमाग में तुम हो, लगता है हमारे पूरे वजूद में तुम हो।",
    "कुछ लोग ज़िंदगी में मिलते हैं सिर्फ यादें बनाने के लिए।",
    "मोहब्बत में हमने ये सबक सीखा है, जो पास होता है उसी से दिल टूटता है।",
    "हमने तो दिल में रख लिया तुम्हें यादों की तरह।",
]


async def setup(client: Client):
    client.on_message(filters.command("shayari", prefixes=".") & filters.me)(shayari_handler)


async def shayari_handler(client: Client, message: Message):
    await message.edit(f"📝 **Shayari:**\n\n{random.choice(SHAYARIS)}")
