import os
from pyrogram import Client,filters

TD="thumbnails"

async def setup(c):
 c.on_message(filters.command("savethumb",prefixes=".")&filters.me)(h)

async def h(c,m):
 if not m.reply_to_message or not m.reply_to_message.photo:
  await m.edit("Reply to a photo to save as thumbnail.");return
 os.makedirs(TD,exist_ok=True)
 p=os.path.join(TD,f"{m.chat.id}.jpg")
 await c.download_media(m.reply_to_message.photo,file_name=p)
 await m.edit("**Thumbnail saved!**")
