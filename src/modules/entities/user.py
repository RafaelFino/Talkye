class User:    
    def __init__(self, user:str, token:str) -> None:
        self.user = user
        self.token = token

    def auth(self, passwd:str) -> str:
        return False

    def create(self) -> bool:
        return False
    
    def validate(self) -> bool:
        return False
    
    def updatePassword(self) -> bool:
        return False