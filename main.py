import json
import os
import urllib.request
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

API_URL = "https://api.alternative.me/fng/?limit=2&format=json"
TELEGRAM_URL = "https://api.telegram.org/bot{}/sendMessage"

def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "CryptoFearGreedTelegramBot/1.0"})
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))

def send_telegram(token, chat_id, message):
    payload = json.dumps({
        "chat_id": chat_id,
        "text": message,
        "disable_web_page_preview": True
    }).encode("utf-8")
    req = urllib.request.Request(
        TELEGRAM_URL.format(token),
        data=payload,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=20) as response:
        result = json.loads(response.read().decode("utf-8"))
    if not result.get("ok"):
        raise RuntimeError("Telegram API did not confirm message delivery")

def main():
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    result = get_json(API_URL)
    rows = result.get("data", [])
    if not rows:
        raise RuntimeError("Alternative.me returned no Fear & Greed data")

    latest = rows[0]
    value = int(latest["value"])
    classification = latest["value_classification"]
    date_text = datetime.fromtimestamp(
        int(latest["timestamp"]), timezone.utc
    ).astimezone(ZoneInfo("Asia/Jakarta")).strftime("%d %B %Y")

    change_text = "Belum tersedia"
    if len(rows) > 1:
        previous = int(rows[1]["value"])
        delta = value - previous
        sign = "+" if delta > 0 else ""
        change_text = f"{sign}{delta} poin (sebelumnya {previous})"

    message = (
        "📊 CRYPTO FEAR & GREED INDEX\n\n"
        f"📅 Tanggal data: {date_text}\n"
        f"🔢 Nilai: {value}/100\n"
        f"🧭 Sentimen: {classification}\n"
        f"📈 Perubahan harian: {change_text}\n\n"
        "Sumber: https://alternative.me/crypto/fear-and-greed-index/"
    )
    send_telegram(token, chat_id, message)

if __name__ == "__main__":
    main()
