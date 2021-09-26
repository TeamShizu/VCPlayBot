import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCkrzaAK_3xx_KcTIQy5WsHvvPzc93S2EdL3MRskCJf9mQFJEC9jof2TKffZWIk2x45llJy9ELVtbRpJc9njGJtmCTcAZpzToV1Ufi9FVcd8LxsBIsIsllYHTqyxWeL2wL9Ihp7rghrWudGyBpeDeyrprRoAOerN4j-PNMbZYGzIGhco1RL7QNpAz6LsrKp0Y8W4RcBxxAcf8p6EaXZKP4khY3BJi5iVaoRn6SvSdnySGkceVQqUFtWpVmfNlt0np76CpeqCgPLAIvNinLdSNU2eqrdGALiidqEGZj6WMT3PJGkdvhtm5XuUKm5HdYKJkr1E71EsERdQ5XOoUo_NF-meHuwLwA")
BOT_TOKEN = getenv("BOT_TOKEN","1940261617:AAE-fCJODko9gAuQYI8J2RvDkIF5mo-K3Ho")
BOT_NAME = getenv("BOT_NAME","taskill")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", " chat_with_friends_sl")
BG_IMAGE = getenv("BG_IMAGE", " .https://telegra.ph/Taskil-music-bot-09-26.png")
admins = {2021371951}
API_ID = int(getenv("API_ID","8267931"))
API_HASH = getenv("API_HASH","4721285cd3901fde69a387d69954dd7b")
BOT_USERNAME = getenv("BOT_USERNAME","music_player_yahaluwo_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "music_player_s")
OWNER_NAME = getenv("OWNER_NAME", "praveenkawshalya")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "chat_with_friends_sl")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlayBot2.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/QueenArzoo/VCPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
ARQ_API_KEY = getenv("ARQ_API_KEY","KWTPVR-QZIHPO-FQRBFT-YMCFPO-ARQ" )
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "797768146").split()))
