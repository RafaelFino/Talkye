import ulid
from datetime import datetime
from modules.entities.user import User

class Message:
    def __init__(self, user: User, message: str) -> None:
        self.user = user
        self.message = message
        self.chatId = None
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.id = ulid.new().str
        
    def toJson(self):
        return {
            "id": self.id,
            "user": self.user.user
            "message": self.message,
            "timestamp": self.timestamp
        }
    
    def fromJson(self, json):
        self.id = json["id"]
        self.user = User()
        self.user.fromJson(json["user"])
        self.message = json["message"]
        self.timestamp = json["timestamp"]       