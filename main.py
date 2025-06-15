import requests
import time
import os
from keep_alive import keep_alive

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

NEWS = [
    "https://www.facebook.com/footballkitchen4u",
    "https://www.facebook.com/cheekysport",
    "https://www.facebook.com/THE.FIRM.FB",
    "https://www.facebook.com/FootballPostOfficial",
    "https://www.instagram.com/footballjoe",
    "https://www.facebook.com/skysportsgoalrush",
    "https://www.facebook.com/awaydaybible",
    "https://www.facebook.com/FourFourTwo",
    "https://www.facebook.com/BleacherReportFootball",
    "https://www.facebook.com/official433",
    "https://www.instagram.com/433/"
]

def send_news():
    for link in NEWS:
        message = f"🔥 Нова статия: {link}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, data=payload)
        time.sleep(1)

keep_alive()

while True:
    send_news()
    time.sleep(60 * 60 * 6)  # на всеки 6 часа
