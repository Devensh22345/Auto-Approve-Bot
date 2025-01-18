from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28345030"))
    API_HASH = getenv("API_HASH", "2454254a802b8a4eeb3e8ac2816f3fee")
    BOT_TOKEN = getenv("BOT_TOKEN", "7365852964:AAFsKlal2wRxWjZPxYQ4sOPaz7KJyqJaIWQ")
    FSUB = getenv("FSUB", "@DK_ANIMES")
    CHID = int(getenv("CHID", "-1002478670225"))
    SUDO = list(map(int, getenv("SUDO", "6872968794")
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://letsearn:fakefacebook602@cluster0.o0trvz0.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
