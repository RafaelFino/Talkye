from modules.storage.db import DbConnection   
from modules.entities.user import User

class UserStorage:
    def __init__(self, db:DbConnection) -> None:
        self.db = db
        self.db.execute(self._getCreateTableScript())

    def create(self, user:str, passwd:str) -> int:
        return self.db.executeInsert("INSERT INTO users (name, passwd) VALUES (?, ?)", (user, passwd))

    def update(self, id:str, user:str, passwd:str) -> bool:
        affected = self.db.execute("UPDATE users SET passwd = ?, name = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?", (passwd, user, id))
        return affected > 0

    def get(self, id) -> User:
        user = User()
        data = self.db.executeSelect("SELECT id, name, passwd, created_at, updated_at FROM users WHERE id = ?", (id))
        for row in data:
            user.fromJson(row)
        
        return user       

    def _getCreateTableScript(self) -> str:
        return """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER AUTOINCREMENT,
    name TEXT PRIMARY KEY,
    passwd TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF EXISTS users_index_name
ON users(name);
"""