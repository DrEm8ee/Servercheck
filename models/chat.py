class chat:
    chat_id = None
    chat_type = None

    def __init__(self,
                 chat_id: int,
                 chat_type: str):
        self.chat_id = chat_id
        self.chat_type = chat_type

    def __str__(self):
        return self.chat_id
