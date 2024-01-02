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

    def _getCreateTableScript(self) -> str:
        return """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT PRIMARY KEY,
    passwd TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX IF EXISTS users_index_id 
ON users(id);

CREATE INDEX IF EXISTS users_index_name
ON users(name);
"""