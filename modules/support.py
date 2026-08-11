import logging
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config.constants import prefix

@Client.on_message(filters.command("support", prefixes=prefix) & filters.me)
async def support_command(client, message: Message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("💬 Support Group", url="https://t.me/kurup_support")],
        [InlineKeyboardButton("📢 Updates Channel", url="https://t.me/kurup_updates")],
        [InlineKeyboardButton("👤 Owner", url="https://t.me/kurupdevs")],
    ])
    await message.edit("**KurupUserbot Support**\n\nNeed help? Join our community!", reply_markup=keyboard)