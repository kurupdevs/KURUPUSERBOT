#  KurupUserbot - telegram userbot
#  Copyright (C) 2020-present Kurup Userbot Organization
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio

from pyrogram import Client, filters
from pyrogram.raw.functions.account import ResetAuthorization
from pyrogram.types import Message

from utils import modules_help, prefix
from utils.db import db


@Client.on_message(filters.command("terminate", prefix) & filters.me)
async def terminate_sessions(client: Client, message: Message):
    try:
        await message.edit("<b>Fetching authorized sessions...</b>")
        sessions = (
            await client.invoke(
                pyrogram.raw.functions.account.GetAuthorizations()
            )
        ).authorizations

        if not sessions:
            return await message.edit("<b>No other authorized sessions found.</b>")

        text = f"<b>Found {len(sessions)} authorized sessions:</b>\n\n"
        for i, session in enumerate(sessions, 1):
            app_name = session.app_name
            device = session.device_model
            platform = session.platform
            current = " (current)" if session.current else ""
            text += f"{i}. <b>{app_name}</b> - {device} ({platform}){current}\n"
            text += f"   <code>hash: {session.hash}</code>\n\n"

        text += "Use <code>.terminate [hash]</code> to kill a session"
        await message.edit(text)
    except Exception as e:
        await message.edit(f"<b>Error:</b> {e}")


@Client.on_message(filters.command("sessionkiller", prefix) & filters.me)
async def session_killer_toggle(client: Client, message: Message):
    enabled = db.get("core.sessionkiller", "enabled", False)
    new_state = not enabled
    db.set("core.sessionkiller", "enabled", new_state)
    status = "<b>enabled</b>" if new_state else "<b>disabled</b>"
    await message.edit(f"Session killer {status}!")


modules_help["sessionkiller"] = {
    "sessionkiller": "Toggle session killer ON/OFF",
    "terminate": "List or terminate active sessions",
}
