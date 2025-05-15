from flask import Flask, jsonify
import asyncio
import threading
import schedule
import time
from yts_rss import fetch_and_post_yts_feeds
from hdhub4u_rss import fetch_and_post_hdhub4u_feeds

app = Flask(__name__)
PORT = 3000

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the YT + HDHub4u RSS Bot API!"})

@app.route('/yts', methods=['GET'])
def handle_yts_feed():
    asyncio.run(fetch_and_post_yts_feeds())
    return jsonify({"message": "YTS feeds fetched and posted!"})

@app.route('/hdhub4u', methods=['GET'])
def handle_hdhub4u_feed():
    asyncio.run(fetch_and_post_hdhub4u_feeds())
    return jsonify({"message": "HDHub4u feeds fetched and posted!"})

def schedule_task():
    schedule.every(10).minutes.do(lambda: asyncio.run(fetch_and_post_yts_feeds()))
    schedule.every(10).minutes.do(lambda: asyncio.run(fetch_and_post_hdhub4u_feeds()))
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    threading.Thread(target=schedule_task, daemon=True).start()
    app.run(host='0.0.0.0', port=PORT)