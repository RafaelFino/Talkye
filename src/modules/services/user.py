from modules.entities.user import User  
from modules.storage.user import UserStorage

class UserServices:
    def __init__(self, dbConnStr:str) -> None:
        self.dbConnStr = dbConnStr

    def createUser(self, user: User) -> bool:
        pass    

    def getUser(self, user: str) -> User:
        pass

    def updateUser(self, user: User) -> bool:
        pass

    def auth(self, user: str, passwd: str) -> str:
        pass

    def validate(self, user:str, token:str) -> bool:
        return False        
    
    def createToken(self, user:str) -> str:
        pass
                