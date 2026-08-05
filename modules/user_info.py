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

from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

from utils import modules_help, prefix
from utils.scripts import format_exc


@Client.on_message(filters.command("info", prefix) & filters.me)
async def user_info(client: Client, message: Message):
    try:
        if message.reply_to_message:
            user = message.reply_to_message.from_user
        elif len(message.command) > 1:
            try:
                user = await client.get_users(message.command[1])
            except Exception:
                return await message.edit("<b>User not found.</b>")
        else:
            return await message.edit("<b>Reply to a message or provide a user ID/username.</b>")

        text = f"<b>User Info:</b>\n"
        text += f"<b>ID:</b> <code>{user.id}</code>\n"
        text += f"<b>First Name:</b> {user.first_name or 'N/A'}\n"
        text += f"<b>Last Name:</b> {user.last_name or 'N/A'}\n"
        text += f"<b>Username:</b> @{user.username or 'N/A'}\n"
        text += f"<b>Is Bot:</b> {user.is_bot}\n"
        text += f"<b>Is Premium:</b> {user.is_premium}\n"
        text += f"<b>Is Scam:</b> {user.is_scam}\n"
        text += f"<b>Language:</b> {user.language_code or 'N/A'}\n"

        await message.edit(text)
    except Exception as e:
        await message.edit(format_exc(e))


modules_help["user_info"] = {
    "info [user_id/username]": "Get user information",
}
