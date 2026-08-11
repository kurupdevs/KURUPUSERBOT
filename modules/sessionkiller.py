import logging
from pyrogram import filters, raw
from pyrogram.types import Message
from config.constants import prefix
from utils.db import db

@Client.on_message(filters.command("killsession", prefixes=prefix) & filters.me)
async def killsession_command(client, message: Message):
    if not db.get("core.sessionkiller", "enabled", False):
        await message.edit("**Session killer is disabled.**")
        return
    await message.edit("**Fetching active sessions...**")
    auths = await client.invoke(raw.functions.account.GetAuthorizations())
    auth_hashes = db.get("core.sessionkiller", "auths_hashes", [])
    killed = 0
    for auth in auths.authorizations:
        if auth.hash not in auth_hashes:
            try:
                await client.invoke(raw.functions.account.ResetAuthorization(hash=auth.hash))
                killed += 1
            except Exception:
                pass
    await message.edit(f"**Terminated {killed} unauthorized sessions.**")