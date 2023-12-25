class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6117482949"
    sudo_users = "6765826972", "6765826972"
    GROUP_ID = -1002119971614
    TOKEN = "6980178795:AAEBUZDJsLta5IbcXBRaq3pSjhAZMXFvrlM"
    mongo_url = "mongodb+srv://kuldiprathod2003:kuldiprathod2003@cluster0.wxqpikp.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/2767b2d21e0667a81a364.jpg", "https://telegra.ph/file/091c080e387799aad5536.jpg", "https://telegra.ph/file/1926c7c608d2c2b891ff1.jpg"]
    SUPPORT_CHAT = "anime_x_god_group"
    UPDATE_CHAT = "anime_x_god"
    BOT_USERNAME = "taki_waifus_bot"
    CHARA_CHANNEL_ID = "-1002017843882"
    api_id = 25997075
    api_hash = "8f7d4aba2280fa063694064beba34d7d"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
