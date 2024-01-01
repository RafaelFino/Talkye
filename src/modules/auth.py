import sqlite3
class Auth:
    def __init__(self, db:sqlite3) -> None:
        self.db = None
       
    def auth(self, user: str, passwd:str) -> str:
        return False

    def validate(self, user:str, token:str) -> bool:
        return False
            
    def testConnection(self) -> bool:
        if self.db is None:
            return False

        return self.db.is_connected()
            