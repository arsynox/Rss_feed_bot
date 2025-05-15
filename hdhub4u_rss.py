import requests
from bs4 import BeautifulSoup
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def fetch_hdhub4u_updates():
    url = 'https://hdhub4u.football/'
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/120.0.0.0 Safari/537.36'
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch HDHub4u: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    updates = []

    for post in soup.select('article'):
        title_tag = post.select_one('h2 a')
        if not title_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = title_tag['href']
        if not link.startswith('http'):
            link = url.rstrip('/') + '/' + link.lstrip('/')

        updates.append({'title': title, 'link': link})

    return updates

def fetch_and_post_hdhub4u_feeds():
    updates = fetch_hdhub4u_updates()
    for update in updates:
        message = f"{update['title']}\n{update['link']}"
        send_to_telegram(message)

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'disable_web_page_preview': True
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"[ERROR] Failed to send message to Telegram: {e}")