from telegram import Bot

# Configuration
BOT_TOKEN = "63180009:AAFYNSsQkPuvUIr1ugL82zSeefqwZPt7Z"
CHAT_ID = "-10024186162"

# Initialize Telegram bot
bot = Bot(token=BOT_TOKEN)

# Sets to track downloaded items
downloaded_items_yts = set()
downloaded_items_tg = set()
