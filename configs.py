# (c) @RoyalKrrishna

import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", 12345))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MdiskSearchRobot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "1BVtsOKsBu7TFQF5I2edKJCpsicEA9_bYC23qa1Dg6CIxV26-MO7r5L643H4RFj9oGb2Ap3Hd_OyD2WHZ2E-eLDGAFjtaIzLczr7x7J5nWkL15z3Sx949kYs3Df1fzLtHvvAN-fUsNbAnT0Cx06pfw9jXIy31qUI8pyAnM7zhGwzz6OVfnCV3cRIb1B75UqB_T567E3hPawdXOJMHbcGvx4jOnhoNY6Nptmr2rfQXEG5QZCNk_m_RN4Aukkfey-pcFJ1DsEaMe4AfWyd9STwj0aGZTPo6B9fHP7GEdzei6z5ii95OO48zXxTlMFK7j9NdAPqfKMrLYKorw8Bm-r3thpSaiDZoA6U=")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", -100))
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    BOT_OWNER = int(os.getenv("BOT_OWNER"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG")
    START_PHOTO = os.getenv("START_PHOTO")
    HOME_TEXT = os.getenv("HOME_TEXT")
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", None)
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", ""))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 300))
    MDISK_API = os.getenv("MDISK_API", "12334")
    REPLIT_USERNAME = os.environ.get("REPLIT_USERNAME", None) # your replit username 
    REPLIT_APP_NAME = os.environ.get("REPLIT_APP_NAME", None) # your replit app name 
    REPLIT = f"https://{REPLIT_APP_NAME.lower()}.{REPLIT_USERNAME}.repl.co" if REPLIT_APP_NAME and REPLIT_USERNAME else False
    PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT")
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT")
