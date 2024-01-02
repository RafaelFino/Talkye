import ulid
from datetime import datetime
from modules.entities.user import User

class Message:
    def __init__(self, userId: int, chatId: int, message: str) -> None:
        self.userId = userId
        self.message = message
        self.chatId = None
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.id = None
        
    def toJson(self):
        ret = {
            "userId": self.userId,
            "chatId": self.chatId,
            "message": self.message,
            "timestamp": self.timestamp
        }

        if self.id:
            ret["id"] = self.id 

        return ret
    
    def fromJson(self, json):
        if json is None:
            raise Exception("Json is None")
        
        if "id" in json:
            self.id = json["id"]

        if "userId" in json:
            self.userId = json["userId"]

        if "chatId" in json:
            self.chatId = json["chatId"]    

        if "message" in json:
            self.message = json["message"]

        if "timestamp" in json:
            self.timestamp = json["timestamp"]