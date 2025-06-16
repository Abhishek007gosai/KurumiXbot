# +++ Made By Sanjiii [telegram username: @Urr_Sanjiii] +++

import asyncio
import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather, --⚠️ REQUIRED--
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
#Your API ID from my.telegram.org --⚠️ REQUIRED--
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org, --⚠️ REQUIRED--
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id --⚠️ REQUIRED--
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID --⚠️ REQUIRED--
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#SUPPORT_GROUP: This is used for normal users for getting help if they don't understand how to use the bot --⚠ OPTIONAL--
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "")

#Port
PORT = os.environ.get("PORT", "8050")

#Database --⚠️ REQUIRED--
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "")

VERIFY_DB = os.environ.get("VERIFY_DB", "mongodb+srv://toukaxrobot:T6mezH0agfSgyEs0@toukabot.kwabl3g.mongodb.net/?retryWrites=true&w=majority&appName=Toukabot")
DBV_NAME = os.environ.get("VERIFY_DBNAME", "Toukabot")


TOKEN_PIC = os.environ.get("TOKEN_PIC", "")


#Tutorial video for the user of your shortner on how to download.
TUT_VID = os.environ.get("TUT_VID","https://t.me/+wekKcN1tjbAxY2U1")


START_PIC = os.environ.get("START_PIC", "https://graph.org/file/8263af1da9ac363d8c580-a8912d879836f10ccd.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/9391e81b5959c012691fa-7082ef0f9fe62f2c56.jpg")

                        
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://litter.catbox.moe/bxry4e.jpg https://litter.catbox.moe/30rzzn.jpg https://litter.catbox.moe/m4c4wu.jpg https://litter.catbox.moe/uq7ichhhh9dz7rg0.jpg")).split() #Required
#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
