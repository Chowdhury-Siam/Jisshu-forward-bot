from os import environ 

class Config:
    API_ID = environ.get("API_ID", "28986163")
    API_HASH = environ.get("API_HASH", "07225d0de9bee70666517315d2174171")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7113359681:AAHBCfDqJ8wDKJo4ItIk2nbe7LXwO-s478w") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://siamchowdhury88888:4A9JTKbenH7AKfdF@siam80.9lqthzx.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forwardboiw1t")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6941649360').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
