import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "17822592"))
    API_HASH = os.environ.get("API_HASH", "a20b3dbbe07ed695563b4609a3e62012")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "578811855")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://idol:hari813143@idol.cukivnu.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "idol")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'idol')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002180166462"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Royalbomma813_Bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
