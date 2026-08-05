# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
# Modified for KurupUserbot

import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message

from utils import config, modules_help, prefix
from utils.scripts import format_exc


@Client.on_message(filters.command("vt", prefix) & filters.me)
async def virus_total(client: Client, message: Message):
    if not config.vt_key or config.vt_key == "123456779:ABCDE":
        return await message.edit("<b>VT API key not configured. Set VT_KEY in .env</b>")

    if message.reply_to_message and message.reply_to_message.document:
        await message.edit("<b>Scanning with VirusTotal...</b>")
        try:
            file_path = await message.reply_to_message.download()

            async with aiohttp.ClientSession() as session:
                # Upload file
                with open(file_path, "rb") as f:
                    async with session.post(
                        "https://www.virustotal.com/api/v3/files",
                        headers={"x-apikey": config.vt_key},
                        data={"file": f},
                    ) as resp:
                        result = await resp.json()

                if "data" in result:
                    analysis_id = result["data"]["id"]
                    await message.edit(
                        f"<b>File uploaded for analysis!</b>\n"
                        f"<b>Analysis ID:</b> <code>{analysis_id}</code>\n"
                        f"<a href='https://www.virustotal.com/gui/file/{analysis_id}'>View Report</a>"
                    )
                else:
                    await message.edit(f"<b>Error:</b> {result}")
        except Exception as e:
            await message.edit(format_exc(e))
    else:
        await message.edit("<b>Reply to a file to scan it with VirusTotal.</b>")


modules_help["vt"] = {
    "vt [reply_to_file]": "Scan file with VirusTotal",
}
