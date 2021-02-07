import os
import sys


def init_files():
    if not os.path.exists("config.txt"):
        open("config.txt", "x")
        write_defaults()

    if not os.path.exists("chats.txt"):
        open("chats.txt", "x")


def write_defaults():
    with open("config.txt", "a") as file_handle:
        file_handle.write('%s\n' % "TOKEN")
        file_handle.write('%s\n' % "TARGET")

    file_handle.close()


def get_token() -> str:
    config = []
    with open("config.txt", "r") as file_handle:
        for line in file_handle:
            current_line = line[:-1]
            config.append(current_line)

    if config[0] == "TOKEN":
        sys.exit("Invalid Token")
    else:
        return config[0]


def get_target() -> str:
    config = []
    with open("config.txt", "r") as file_handle:
        for line in file_handle:
            current_line = line[:-1]
            config.append(current_line)

    return config[1]


def get_chat_ids() -> [int]:
    ids = []
    with open("chats.txt", "r") as file_handle:
        for line in file_handle:
            current_line = line[:-1]
            ids.append(current_line)
    file_handle.close()
    return ids


def chat_id_exists(chat_id: int) -> bool:
    # TDDO FIX BUG
    for ids in get_chat_ids():
        if int(ids) == int(chat_id):
            return True

    return False


def add_chat_id(chat_id: int):
    with open("chats.txt", "a") as file_handle:
        file_handle.write('%s\n' % chat_id)

    file_handle.close()
