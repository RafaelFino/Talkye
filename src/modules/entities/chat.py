from modules.entities.user import User

class Chat:
    def __init__(self) -> None:        
        self.id = None
        self.name = None    
        self.messages = [] 
        self.users = []
        self.created_at = None
        self.updated_at = None

    def send(self) -> bool:
        return
    
    def addUsers(self, user:User) -> bool:
        self.users[user.id] = user  
    
    def toJson(self):
        ret = {
            "id": self.id,
            "name": self.name,
            "messages": self.messages,
            "users": self.users
        }

        if self.created_at:
            ret["created_at"] = self.created_at

        if self.updated_at:
            ret["updated_at"] = self.updated_at 

        return ret
    
    def fromJson(self, json):
        if json is None:
            raise Exception("Json is None")
        
        if "id" in json:
            self.id = None

        if "name" in json:
            self.name = json["name"]
        
        if "messages" not in json:
            self.messages = []

        if "users" not in json:
            self.users = []

        if "created_at" in json:
            self.created_at = json["created_at"]

        if "updated_at" in json:
            self.updated_at = json["updated_at"]

