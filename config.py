import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","8060061"))
API_HASH = getenv("API_HASH","0a19238a019c119cea065eae38cebcd2")

BOT_TOKEN = getenv("BOT_TOKEN","7312074776:AAESKL9QWisPkrjCyZ6B0a9u10A7NGfQKaw")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Somu:Somu@somu.xbkiklu.mongodb.net/?retryWrites=true&w=majority&appName=Somu")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID","-1002100433415"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "ρнαηтσм 𝐗 𝐌υʂι𝐂")

OWNER_ID = list(map(int, getenv("OWNER_ID", "7070591202").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/KALI-OFFICIAL1/Test")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/silent_aura")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/silent_aura")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQG0OpUAtMPk9jZNnTG6a56908hEYdsd5PBfgFR62-zkIewOnsyCVWpMTezL-iVSijF5Pw8VvahlXALF1e9TYzsKqyR7YF_pDCmY4gy2YcOEeS82DEm-liEJdAsm-NuQi1t3kF2xX4VKEPwl0oBtOD0OLxDeuN__KPvx2tHJjLYI-jrdua8r6dc2nWm2BHWT5-KiTh0ms1g4W5I0F38t_NaugKP2-UvBjwVxksondU1nT9a8M2p0HUaWYFxuzba-pRtS-pdYTnNODRg4k2TjNzxoMWK0HyILoSjSqJCxh_B3bi62MEAqa16A61ow_6owr9mnnuunFwGpjsT1PRIv2JQ0eFYidQAAAAGbzo9oAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/af8e81a9a3f788ddafd1c.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/b11d2a1aecf02143b96c7.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/af8e81a9a3f788ddafd1c.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/af8e81a9a3f788ddafd1c.jpg"

STATS_IMG_URL = "https://telegra.ph/file/abfcd5d3edd7ea7cd5c1b.jpg"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/abfcd5d3edd7ea7cd5c1b.jpg"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/abfcd5d3edd7ea7cd5c1b.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/abfcd5d3edd7ea7cd5c1b.jpg"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/b11d2a1aecf02143b96c7.jpg"

YOUTUBE_IMG_URL = "https://telegra.ph/file/af8e81a9a3f788ddafd1c.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/b11d2a1aecf02143b96c7.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/b11d2a1aecf02143b96c7.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/b11d2a1aecf02143b96c7.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/b11d2a1aecf02143b96c7.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/af8e81a9a3f788ddafd1c.jpg"
