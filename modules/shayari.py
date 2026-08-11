import random
import logging
from pyrogram import filters
from pyrogram.types import Message
from config.constants import prefix

SHAYARI_LIST = [
    "तेरी यादों ने हमें तन्हा कर दिया, वरना हम तो ख़ुश थे ज़माने की भीड़ में।",
    "दिल में तुम हो, दिमाग में तुम हो, लगता है हमारे पूरे वजूद में तुम हो।",
    "कुछ लोग ज़िंदगी में मिलते हैं सिर्फ यादें बनाने के लिए, और कुछ यादें बन जाती हैं ज़िंदगी।",
    "मोहब्बत में हमने ये सबक सीखा है, जो पास होता है उसी से दिल टूटता है।",
    "हमने तो दिल में रख लिया तुम्हें यादों की तरह, पर तुम्हें तो हम भूल गए।",
]

@Client.on_message(filters.command("shayari", prefixes=prefix) & filters.me)
async def shayari_command(client, message: Message):
    shayari = random.choice(SHAYARI_LIST)
    await message.edit(f"📝 **Shayari:**\n\n{shayari}")