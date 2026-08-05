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

import os

import aiofiles
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message

from utils import modules_help, prefix
from utils.scripts import format_exc


@Client.on_message(filters.command("upl", prefix) & filters.me)
async def upload_file(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.edit("<b>Please provide a URL to upload.</b>")

    url = message.command[1]
    await message.edit("<b>Downloading file...</b>")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return await message.edit(f"<b>Failed to download file. Status: {response.status}</b>")

                filename = url.split("/")[-1] or "uploaded_file"
                filepath = os.path.join("downloads", filename)
                os.makedirs("downloads", exist_ok=True)

                async with aiofiles.open(filepath, "wb") as f:
                    await f.write(await response.read())

        await message.edit("<b>Uploading to Telegram...</b>")

        if os.path.getsize(filepath) > 50 * 1024 * 1024:
            await message.reply_document(filepath)
        else:
            await message.reply_document(filepath)

        await message.delete()
        os.remove(filepath)
    except Exception as e:
        await message.edit(format_exc(e))


modules_help["upl"] = {
    "upl [url]*": "Download and upload a file from URL",
}
