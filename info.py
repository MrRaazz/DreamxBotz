import re
import os
from os import environ, getenv
from Script import script

# Utility functions
id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# ============================
# Bot Information Configuration
# ============================
SESSION = environ.get('SESSION', 'dreamxbotz_search')
API_ID = int(environ.get('API_ID', '24358501'))
API_HASH = environ.get('API_HASH', 'fa51ce8876c215d8a76c98c755e6d2d3')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# ============================
# Bot Settings Configuration
# ============================
CACHE_TIME = int(environ.get('CACHE_TIME', 150))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/56b5deb73f3b132e2bb73.jpg https://graph.org/file/5303692652d91d52180c2.jpg https://graph.org/file/425b6f46efc7c6d64105f.jpg https://graph.org/file/876867e761c6c7a29855b.jpg')).split()  # Sample pic
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/60e8a622b14796e4448ce.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/13702ae26fb05df52667c.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/242b7f1b52743938d81f1.jpg'))
FSUB_PICS = (environ.get('FSUB_PICS', 'https://graph.org/file/7478ff3eac37f4329c3d8.jpg https://graph.org/file/56b5deb73f3b132e2bb73.jpg')).split()  # Fsub pic

# ============================
# Admin, Channels & Users Configuration
# ============================
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1834715690 6522113087').split()] # Replace with the actual admin ID(s) to add
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002595666055').split()]  # Channel id for auto indexing (make sure bot is admin)

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002658887595'))  # Log channel id (make sure bot is admin)
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002462961460'))  # Bin channel id (make sure bot is admin)
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002565101416'))  # Premium logs channel id
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1002518988143').split()] #(make sure bot is admin)
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-4639985908')  # Support group id (make sure bot is admin)
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002597099142')  # Request channel id (make sure bot is admin)
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/updofydyoddh')  # Support group link (make sure bot is admin)

# FORCE_SUB 
auth_req_channel = environ.get('AUTH_REQ_CHANNEL', '-1002185732095')  # requst to join Channel for force sub (make sure bot is admin) only for bot ADMINS  
AUTH_CHANNELS = [int(channels_id) for channels_id in environ.get('AUTH_CHANNELS', '-1002507871737').split() if re.match(r'^-?\d+$', channels_id)]  # Channels for force sub (make sure bot is admin)



# ============================
# Payment Configuration
# ============================
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/e419f801841c2ee3db0fc.jpg')
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'ɴᴏ ᴀᴠᴀɪʟᴀʙʟᴇ ʀɪɢʜᴛ ɴᴏᴡ')

STAR_PREMIUM_PLANS = {
    15: "7day",
    30: "15day",    
    60: "1month", 
    120: "2month",
    220: "3month",
}

# ============================
# MongoDB Configuration
# ============================
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'dreamcinezone_files')

# If MULTIPLE_DB Is True Then Fill DATABASE_URI2 Value Else You Will Get Error.
MULTIPLE_DB = is_enabled(os.environ.get('MULTIPLE_DB', "False"), False) # Type True For Turn On MULTIPLE DB FUNTION 
DATABASE_URI2 = environ.get('DATABASE_URI2', "")

# ============================
# Movie Notification & Update Settings
# ============================
MOVIE_UPDATE_NOTIFICATION = bool(environ.get('MOVIE_UPDATE_NOTIFICATION', True))  # Notification On (True) / Off (False)
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002623792423'))  # Notification of sent to your channel
DREAMXBOTZ_IMAGE_FETCH = bool(environ.get('DREAMXBOTZ_IMAGE_FETCH', False))  # On (True) / Off (False)

# ============================
# Verification Settings
# ============================
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002512328415')) #Verification Channel Id 
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002856009901')) #If Anyone Set Your Bot In Any Group And Set Shortner In That Group Then In This Channel The All Details Come
VERIFY_IMG = environ.get("VERIFY_IMG", "https://telegra.ph/file/9ecc5d6e4df5b83424896.jpg")

TUTORIAL = environ.get("TUTORIAL", "https://t.me/dreamxbotz")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/dreamxbotz")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/dreamxbotz")

# Verification (Must Fill All Veriables. Else You Got Error
SHORTENER_API = environ.get("SHORTENER_API", "a7ac9b3012c67d7491414cf272d82593c75f6cbb")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "omegalinks.in")

SHORTENER_API2 = environ.get("SHORTENER_API2", "a7ac9b3012c67d7491414cf272d82593c75f6cbb")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "omegalinks.in")

SHORTENER_API3 = environ.get("SHORTENER_API3", "a7ac9b3012c67d7491414cf272d82593c75f6cbb")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "omegalinks.in")

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "1200"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "54000"))

# ============================
# Channel & Group Links Configuration
# ============================
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Requiest_your_faw')
CHNL_LNK = environ.get('CHNL_LNK', 't.me/All_new_and_old_collecton')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/Yuvraaj233')
UPDATE_CHNL_LNK = environ.get('UPDATE_CHNL_LNK', 'https://t.me/DragonMax_Official_Updates')

# ============================
# User Configuration
# ============================
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]

# ============================
# Miscellaneous Configuration
# ============================
MAX_B_TN = environ.get("MAX_B_TN", "5")
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'Share & Support Us ♥️')
DELETE_TIME = int(environ.get("DELETE_TIME", "300"))  #  deletion time in seconds (default: 5 minutes). Adjust as per your needs.
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))  # True if you want no results messages in Log Channel
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
PM_SEARCH = bool(environ.get('PM_SEARCH', True))  # PM Search On (True) / Off (False)
EMOJI_MODE = bool(environ.get('EMOJI_MODE', False))  # Emoji status On (True) / Off (False)
BUTTON_MODE = is_enabled((environ.get('BUTTON_MODE', "False")), False) # pm & Group button or link mode (True) / Off (False)
STREAM_MODE = bool(environ.get('STREAM_MODE', False)) # Set Stream mode True or False

# ============================
# Bot Configuration
# ============================
AUTH_REQ_CHANNEL = int(auth_req_channel) if auth_req_channel and id_pattern.search(auth_req_channel) else None
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]
QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]
SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

# ============================
# Server & Web Configuration
# ============================

NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'dreamXBotz'))
MULTI_CLIENT = False
name = str(environ.get('name', 'DREAMXBOTZ'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))
else:
    ON_HEROKU = False
HAS_SSL = bool(getenv('HAS_SSL', True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

# ============================
# Reactions Configuration
# ============================
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]

# ============================
# Command Bot
# ============================
Bot_cmds = {
    "start": "Sᴛᴀʀᴛ Mᴇ Bᴀʙʏ",
    "alive": " Cʜᴇᴄᴋ Bᴏᴛ Aʟɪᴠᴇ ᴏʀ Nᴏᴛ ",
    "settings": "ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs",
    "id": "ɢᴇᴛ ɪᴅ ᴛᴇʟᴇɢʀᴀᴍ ",
    "info": "Gᴇᴛ Usᴇʀ ɪɴғᴏ ",
    "system": "sʏsᴛᴇᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ",
    "del_msg": "ʀᴇᴍᴏᴠᴇ ғɪʟᴇ ɴᴀᴍᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ɴᴏтɪғɪᴄᴀᴛɪᴏɴ...",
    "movie_update": "ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "pm_search": "ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "trendlist": "Gᴇᴛ Tᴏᴘ Tʀᴀɴᴅɪɴɢ Sᴇᴀʀᴄʜ Lɪsᴛ",
    "logs": "ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ.",
    "delete": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "users": "ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.",
    "chats": "ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ.",
    "leave": "ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.",
    "disable": "ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.",
    "ban": "ʙᴀɴ ᴀ ᴜꜱᴇʀ.",
    "unban": "ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.",
    "channel": "ɢᴇᴛ ʟɪꜱᴛ ᴏғ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘꜱ.",
    "broadcast": "ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.",
    "grp_broadcast": "ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs",
    "clear_junk": "ᴄʟᴇᴀʀ ᴜsᴇʀ ᴊᴜɴᴋ",
    "junk_group": "ᴄʟᴇᴀʀ ɢʀᴏᴜᴘ ᴊᴜɴᴋ",
    "deletefiles": "ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD ғɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.",
    "send": "ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜꜱᴇʀ.",
    "add_premium": "ᴀᴅᴅ ᴀɴʏ ᴜꜱᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.",
    "remove_premium": "ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.",
    "premium_users": "ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ.",
    "get_premium": "ɢᴇᴛ ɪɴꜰᴏ ᴏꜰ ᴀɴʏ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ.",
    "restart": "ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ."
}


#Don't Change Anything Here
if MULTIPLE_DB == False:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI
else:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI2

# ============================
# Logs Configuration
# ============================
LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for your queries.\n" if IMDB else "IMDB Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending file directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled, files will be sent in PM instead of starting the bot.\n")
LOG_STR += ("BUTTON_MODE is found, filename and file size will be shown in a single button instead of two separate buttons.\n" if BUTTON_MODE else "BUTTON_MODE is disabled, filename and file size will be shown as different buttons.\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be sent along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode is enabled, bot will be suggesting related movies if movie name is misspelled.\n" if SPELL_CHECK_REPLY else "Spell Check Mode is disabled.\n")

