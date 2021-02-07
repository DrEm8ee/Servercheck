import models.user as user
import models.chat as chat


class message:
    message_id = None
    date = None
    text = None
    message_chat = None
    sender = None

    def __init__(self,
                 message_id: int,
                 date: int,
                 text: str,
                 message_chat: chat,
                 sender: user = None):
        self.message_id = message_id
        self.date = date
        self.text = text
        self.message_chat = message_chat
        self.sender = sender

    def __str__(self):
        return self.text
