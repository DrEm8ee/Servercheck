import requests
import json
import sys


import file_handler

from models import message
from models import user
from models import chat


class bot:
    base = None

    def __init__(self, token: str):
        self.base = "https://api.telegram.org/bot" + token

    def base_request(self, method: str, param: dict) -> str:
        req = requests.get(self.base + "/" + method, param)
        ok = json.loads(req.text)["ok"]
        if not ok:
            sys.exit("Connection Error: \n" + req.text)
        return req.text

    def send_message(self, chat_id, text):
        payload = {"chat_id": chat_id, "text": text}
        response = self.base_request("sendMessage", payload)

    def broadcast_message(self, text):
        for chat_id in file_handler.get_chat_ids():
            self.send_message(chat_id, text)

    def get_last_message(self) -> message:
        payload = {"offset": -1, "limit": 1}
        response = self.base_request("getUpdates", payload)

        message_id = int(json.loads(response)["result"][0]["message"]["message_id"])
        date = int(json.loads(response)["result"][0]["message"]["date"])
        text = str(json.loads(response)["result"][0]["message"]["text"])

        chat_id = int(json.loads(response)["result"][0]["message"]["chat"]["id"])
        chat_type = str(json.loads(response)["result"][0]["message"]["chat"]["type"])
        message_chat = chat.chat(chat_id, chat_type)

        user_id = int(json.loads(response)["result"][0]["message"]["from"]["id"])
        is_bot = bool(json.loads(response)["result"][0]["message"]["from"]["is_bot"])
        first_name = str(json.loads(response)["result"][0]["message"]["from"]["first_name"])
        username = str(json.loads(response)["result"][0]["message"]["from"]["username"])
        sender = user.user(user_id, is_bot, first_name, username)

        msg = message.message(message_id, date, text, message_chat, sender)
        return msg
