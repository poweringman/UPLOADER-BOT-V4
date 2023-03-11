import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1327268321:AAFUwEDdbioryZum46inGwbsNEfe6NIjW64")

    API_ID = int(os.environ.get("API_ID", 14157511))

    API_HASH = os.environ.get("API_HASH", "0bf7c2521f57a94f1d699ced3c3cbf63")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "671292689").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001739515008")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @upload_fast_bot"

    DATABASE_URL = os.environ.get("DATABASE_URL", "")

    SESSION_NAME = os.environ.get("SESSION_NAME", "upload_fast_bot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001739515008))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "671292689"))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001739515008")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "upload_fast_bot")

    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))

    PRO_USERS.append(OWNER_ID)
