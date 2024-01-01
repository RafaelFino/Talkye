import sqlite3
from modules.storage import User
class Auth:
    def __init__(self, userStorage: ) -> None:
        self.db = None
       
    def auth(self, user: str, passwd:str) -> str:
        return False

    def validate(self, user:str, token:str) -> bool:
        return False
            
    def testConnection(self) -> bool:
        if self.db is None:
            return False

        return self.db.is_connected()
            