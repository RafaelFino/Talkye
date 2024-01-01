import ulid
from datetime import datetime
from modules.entities.user import User

class Message:
    def __init__(self, user: User, message: str) -> None:
        self.user = user
        self.message = message
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.id = ulid.new().str
        