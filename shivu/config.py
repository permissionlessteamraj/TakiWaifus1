class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7524032836"
    sudo_users = "8285724366", "8285724366", "8285724366"
    GROUP_ID = -1002576801363
    TOKEN = "8239143373:AAGMmo7xi3bdVIsr3Q2e9iZWB1uRAHbLGgY"
    mongo_url = "mongodb+srv://rj5706603:O95nvJYxapyDHfkw@cluster0.fzmckei.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://envs.sh/K-U.jpg/IMG20251004387.jpg", "https://envs.sh/K-U.jpg/IMG20251004387.jpg", "https://envs.sh/K-U.jpg/IMG20251004387.jpg"]
    SUPPORT_CHAT = "narzofamily"
    UPDATE_CHAT = "narzoxbot"
    BOT_USERNAME = "@narzowaifubot"
    CHARA_CHANNEL_ID = "-1002991438744"
    api_id = 23562992
    api_hash = "e070a310ca3e76ebc044146b9829237c"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
