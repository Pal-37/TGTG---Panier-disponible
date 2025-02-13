import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("TGTG_EMAIL")
PASSWORD = os.getenv("TGTG_PASSWORD")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def get_auth_token():
    url = "https://apptoogoodtogo.com/api/authenticate"
    data = {"email": EMAIL, "password": PASSWORD}
    response = requests.post(url, json=data)
    return response.json().get("access_token")

def get_available_baskets(token):
    url = "https://apptoogoodtogo.com/api/items"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=data)

if __name__ == "__main__":
    token = get_auth_token()
    while True:
        baskets = get_available_baskets(token)
        if baskets:
            send_telegram_message(f"🛒 Un panier Too Good To Go est disponible ! 🚀")
        time.sleep(300)  # Vérifie toutes les 5 minutes
