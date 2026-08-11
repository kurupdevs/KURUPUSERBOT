import asyncio, random
from pyrogram import Client, filters
from pyrogram.types import Message

GALIS = ["Teri shakal dekh ke lagta hai bhagwan ne tujhe banate waqt chhutti le li thi.","Tu insaan hai ya dharti pe bojh?","Tera dimaag hai ya khali dibba?","Apni aukat mein reh."]

async def setup(c):c.on_message(filters.command("gali",prefixes=".")&filters.me)(h)
async def h(c:Client,m:Message):
 t=m.reply_to_message.from_user.mention if m.reply_to_message else "User"
 await m.edit(f"{t}, {random.choice(GALIS)}")
