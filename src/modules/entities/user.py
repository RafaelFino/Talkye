class User:    
    def __init__(self, user:str, token:str) -> None:
        self.id
        self.user = user
        self.token = token
        self.created_at = None
        self.updated_at = None        

    def create(self) -> bool:
        return False
    
    def updatePassword(self) -> bool:
        return False
    
    def toJson(self):
        ret = {}
        if self.id:
            ret["id"] = self.id

        if self.user:
            ret["user"] = self.user 

        if self.token:
            ret["token"] = self.token       

        return ret
    
    def fromJson(self, json):
        if json is None:
            raise Exception("Json is None")
        
        if "user" not in json:
            raise Exception("Json does not have user key")
        
        self.user = json["user"]        

        if "token" in json:
            self.token = json["token"]    
        
        if "id" in json:
            self.id = json["id"]

        if "created_at" in json:
            self.created_at = json["created_at"]

        if "updated_at" in json:
            self.updated_at = json["updated_at"]        