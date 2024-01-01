class User:    
    def __init__(self, user:str, token:str) -> None:
        self.user = user
        self.token = token

    def create(self) -> bool:
        return False
    
    def updatePassword(self) -> bool:
        return False
    
    def toJson(self):
        return {
            "user": self.user,
            "token": self.token
        }   
    
    def fromJson(self, json):
        self.user = json["user"]
        self.token = json["token"]
    