from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AnonX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/8998ddca2f42a4fac4efd.jpg",
        caption=f"""🍁𝐂ʅιƈ𝐊🥰𝐁ҽʅσ𝐖💝𝐁υƚƚσ𝐍✨𝐓σ🙊𝐃ɱ❤️𝐎ɯɳҽɾ𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 σԃϝαƚԋҽ 🌹", url=f"https://t.me/YOUR_GODFATHER_XD")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/8998ddca2f42a4fac4efd.jpg",
        caption=f"""🍁𝐂ʅιƈ𝐊🥰𝐁ҽʅσ𝐖💝𝐁υƚƚσ𝐍✨𝐓σ🙊𝐃ɱ❤️𝐎ɯɳҽ𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 σԃϝαƚԋҽ 🌹", url=f"https://t.me/YOUR_GODFATHER_XD")
                ]
            ]
        ),
    )






@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/175b6d309dd3b2c9a2051.jpg",
        caption=f"""🍁𝐂ʅυƈ𝐊🥰𝐁ҽʅσ𝐖💝𝐁υƚƚσ𝐍✨𝐓σ🙊𝐆ҽ𝐓🌱𝐒υρρσɾ𝐓🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱𝐒υρρσɾ𝐓🌱", url=f"𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐇𝐀𝐈 𝐀𝐁 ")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/175b6d309dd3b2c9a2051.jpg",
        caption=f"""🍁𝐂ʅιƈ𝐊🥰𝐁ҽʅσ𝐖💝𝐁υƚƚσ𝐍✨𝐓σ🙊𝐆ҽ𝐓🌱𝐒υρρσ𝐓🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱𝐒υρρσɾ𝐓🌱", url=f"𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐇𝐀𝐈 𝐀𝐁")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/175b6d309dd3b2c9a2051.jpg",
        caption=f"""🍁𝐂ʅιƈ𝐊🥰𝐁ҽʅσ𝐖💝𝐁υƚƚσ𝐍✨𝐓σ🙊𝐆ҽ𝐓🌱𝐒υρρσɾ𝐓🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱𝐒υρρσɾ𝐓🌱", url=f"𝐏𝐑𝐈𝐀𝐕𝐓𝐄 𝐇𝐀𝐈 𝐀𝐁")
                ]
            ]
        ),
    )

