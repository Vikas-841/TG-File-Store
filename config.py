import os

API_ID = int(os.environ.get("API_ID", 21818796))
API_HASH = os.environ.get("API_HASH", "7873fd3de9343c2a52ad75aacd0e9f13")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6882915473:AAHFovp2r4ZhqWykx4famfyUm29v1PnYt3U")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", -1001875834087)
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", 5932230962))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "5932230962").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
