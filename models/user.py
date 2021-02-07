class user:
    user_id = None
    is_bot = None
    first_name = None
    username = None

    def __init__(self,
                 user_id: int,
                 is_bot: bool,
                 first_name: str,
                 username: str):
        self.user_id = user_id
        self.is_bot = is_bot
        self.first_name = first_name
        self.username = username

    def __str__(self):
        return self.username
