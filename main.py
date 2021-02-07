import datetime
import os
import sys
import time

import file_handler
from bot import bot as telegram

token = None
target = ""
bot = None
online = None
since = None


def is_online(host: str = "127.0.0.1") -> bool:
    state = os.system("ping -c 1 " + host)
    if state == 0:
        return True
    else:
        return False


def loop():
    last_id = bot.get_last_message().message_chat.chat_id

    if not file_handler.chat_id_exists(last_id):
        file_handler.add_chat_id(last_id)

    if not file_handler.get_chat_ids():
        sys.exit("No Telegram Chats found. Please send '/start' to the Bot and start them.")

    global online
    global since

    if is_online(target) != online:
        online = not online
        if online:
            bot.broadcast_message("Target is online now! \nIt was down since " + since)
        else:
            bot.broadcast_message("Target is offline! \nIt was up since " + since)
        since = str(datetime.datetime.now().replace(microsecond=0))

    time.sleep(10)
    loop()


if __name__ == '__main__':
    file_handler.init_files()
    token = file_handler.get_token()
    target = file_handler.get_target()
    online = is_online(target)
    since = str(datetime.datetime.now().replace(microsecond=0))
    bot = telegram(token)
    bot.broadcast_message("Check for " + target + " started.")

    loop()
