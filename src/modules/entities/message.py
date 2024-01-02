import ulid
from datetime import datetime
from modules.entities.user import User

class Message:
    def __init__(self) -> None:
        self.user_name = None
        self.message = None
        self.chat_id = None
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.id = None
        
    def toJson(self):
        ret = {
            "user_name": self.user_name,
            "chat_id": self.chat_id,
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

        if "user_name" in json:
            self.user_name = json["user_name"]

        if "chat_id" in json:
            self.chat_id = json["chat_id"]    

        if "message" in json:
            self.message = json["message"]

        if "timestamp" in json:
            self.timestamp = json["timestamp"]