from pyrogram import Client,filters

SUPPORT_LINK="https://t.me/kurupdevs"

async def setup(c):c.on_message(filters.command("support",prefixes=".")&filters.me)(h)
async def h(c,m):await m.edit(f"**Support:** {SUPPORT_LINK}")
