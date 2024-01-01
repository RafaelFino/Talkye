from modules.storage.db import DbConnection   
class UserStorage:
    def __init__(self, db:DbConnection) -> None:
        self.db = db

    def create(self, user:str, passwd:str) -> bool:
        pass

    def update(self, user:str, passwd:str) -> bool:
        pass

    def get(self, user:str) -> str:
        pass    