from telegram import Bot

# Configuration
BOT_TOKEN = "8191342640:AAG0Y5dyj_Hyoe4Lcg5b4LOyPlukO5Aq2P4"
CHAT_ID = "-100267786434"

# Initialize Telegram bot
bot = Bot(token=BOT_TOKEN)

# Sets to track downloaded items
downloaded_items_yts = set()
downloaded_items_tg = set()
