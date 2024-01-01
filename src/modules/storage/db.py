import sqlite3

class DbConnection:
    def __init__(self, connStr:str) -> None:
        self.db = sqlite3.connect(connStr)

    def testConnection(self) -> bool:
        if self.db is None:
            return False

        return self.db.is_connected()