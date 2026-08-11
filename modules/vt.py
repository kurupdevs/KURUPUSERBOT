from pyrogram import Client,filters

async def setup(c):
 c.on_message(filters.command("vt",prefixes=".")&filters.me)(h)

async def h(c,m):
 if not m.reply_to_message:
  await m.edit("Reply to a message to view details.");return
 u=m.reply_to_message.from_user
 t=f"**View Target:**\nName: {u.first_name}\nID: `{u.id}`\nUsername: @{u.username or 'None'}"
 await m.edit(t)
