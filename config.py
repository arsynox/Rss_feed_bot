from telegram import Bot

# Configuration
BOT_TOKEN = "8191342640:AAGaRoFTvc-04jhFW01VCEVNM05rBOyNYfE"
CHAT_ID = "-100267786434"

# Initialize Telegram bot
bot = Bot(token=BOT_TOKEN)

# Sets to track downloaded items
downloaded_items_yts = set()
downloaded_items_tg = set()
