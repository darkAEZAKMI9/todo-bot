import os
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

TOKEN = os.getenv("BOT_TOKEN") or "YOUR_TOKEN_HERE"

def create_bot():
    return DefaultBotProperties(parse_mode=ParseMode.HTML)