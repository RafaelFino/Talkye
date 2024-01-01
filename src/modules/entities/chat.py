from modules.entities.user import User

class Chat:
    def __init__(self, name: str) -> None:        
        self.id = None
        self.name = None    
        self.messages = {}  
        self.users = {}
    
    def send(self) -> bool:
        return
    
    def addUsers(self, user:User) -> bool:
        self.users[user.id] = user  
    
    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "messages": self.messages,
            "users": self.users
        }
    
    def fromJson(self, json):
        self.id = json["id"]
        self.name = json["name"]
        self.messages = json["messages"]
        self.users = json["users"]  