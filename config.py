import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 200))
LOGGER_ID = int(getenv("LOGGER_ID", None))
OWNER_USERNAME = getenv("OWNER_USERNAME","Itz_Zenoi")
CHAT_GROUP = getenv("CHAT_GROUP","https://t.me/Series_and_Movies_Request_Group")
OWNER_ID = int(getenv("OWNER_ID",5957500906))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/Baji-kun/M",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL","https://t.me/+mKXIX38_UpMxOTg1")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Series_and_Movies_Request_Group")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
AUTO_GCAST = getenv("AUTO_GCAST","True")
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")
PROMO = getenv("PROMO","https://graph.org/file/9476659f5ddae89b5ae9e.jpg")
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/9476659f5ddae89b5ae9e.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/9476659f5ddae89b5ae9e.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/9476659f5ddae89b5ae9e.jpg"
STATS_IMG_URL = "https://graph.org/file/568cb0b03f8c80fd06e40.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/9476659f5ddae89b5ae9e.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/cf120a5879ee7af6fa5c8.jpg"
STREAM_IMG_URL = "https://graph.org/file/086ebd3e7ae1d338ee123.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/2b01227df8735ac46fc43.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/5e0eca6f403baae74b063.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/3fe52b8f4fe34349f6c58.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/fef135796f1c62a0f93a8.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/689984de099a0edca9a7f.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:180"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
