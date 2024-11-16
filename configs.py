# (c) @JAsuran2p0

import os


class Config(object):
	API_ID = 17833358
	API_HASH = "b52cd2b77ec1833ec5b96a9d70a363bb"
	BOT_TOKEN = "7236258270:AAGs32-LFYKmFzea4HNtKzNy3eu5MBbHSlE"
	BOT_USERNAME = "KuttyFileSharingBot"
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002105619071"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1572929036"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Merge1:Merge@cluster0.k7ungxs.mongodb.net")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002400430988")
	LOG_CHANNEL = "-1002192881598"
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Render](https://render.com)

🧑🏻‍💻 **Developer:** @JAsuran2p0

👥 **Support Group:** [Catchme](https://t.me/jasuranbots)

📢 **Updates Channel:** [JAsuran Serials](https://t.me/JAsuranserials)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @JAsuran2p0

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me/) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
