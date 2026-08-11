from pyrogram import Client,filters

async def setup(c):c.on_message(filters.command("info",prefixes=".")&filters.me)(h)
async def h(c,m):
 u=m.reply_to_message.from_user if m.reply_to_message else m.from_user
 t=f"**User Info:**\nName: {u.first_name}\nID: `{u.id}`\nUsername: @{u.username or 'None'}"
 await m.edit(t)
