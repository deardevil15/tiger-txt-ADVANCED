import os

API_ID = API_ID = 25202754

API_HASH = os.environ.get("API_HASH", "cb0cad0ddf750e217b78d0a7d6c8b76a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7111065909:AAFh0VH252kobjuu8Om57hiHhSocw6AgQe8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6092522172))

LOG = -1002079134560

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "26921911").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


