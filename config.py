#----------------------------------- https://github.com/m4mallu/gofilesbot --------------------------------------------#

import os
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "gofilesbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5605460243:AAGW0kD-gVPEQS35DLByasPF8jRJnFWiqlw")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "7546772"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "b81a0dd9129f5cf3e0011295f2e38724")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQBzJ5QAEs3FzWUnA9tUwkc3bpUayve_OAI7IjS2JEfk1_6UqjZMgnVzGMh1llNfRA9C0SMWygsPAEPlOqnegNyFydxuEQ1LViYQDSQPNIHL5If3fgqEOkBe6ezR5opzv4jukRBvhar16dbRuKd0Otvmjl8nOScww0tcTlRaIQY-B5YosiTk7Glaxj739GBbYNrFSOj-hlBKwXosfwIqut_ZJVOcET1m5YhYSwHMsCXVnPFJ2AEgRrojw3RdEy8iOHnDKp9EENWWVKJEIJ0eyqvUCbI6yW0wLl-nwn-_JookCYrOie7mPRK3_4Bj-hHvjTvwE_333p5rRk4XleeA55EEUmqSpAAAAAF8wqhSAA")

    # ID of Channels from which the bot should search files
    CHANNELS = set(int(x) for x in os.environ.get("CHANNELS", "-1002042282508").split())

    # Authorized users to perform delete messages in group
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "948247711").split())

# ------------------------------------------ Optional Variables ------------------------------------------------------ #
    # Username of the group to tag in sending medias
    GROUP_U_NAME = os.environ.get("GROUP_U_NAME", "@jokes199")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
