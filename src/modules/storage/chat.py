from modules.entities.chat import Chat
from modules.storage.db import DbConnection   
class ChatStorage:
    def __init__(self, db:DbConnection) -> None:
        self.db = db
        self.db.execute(self._getCreateTableScript())

    def create(self, chat:Chat) -> int:
        return self.db.executeInsert("INSERT INTO chats (name) VALUES (?)", (chat.name))

    def getAll(self) -> list:
        chats = []
        data = self.db.executeSelect("SELECT id, name, created_at, updated_at FROM chats")
        for row in data:
            chat = Chat()
            chat.fromJson(row)
            chats.append(chat)
        
        return chats

    def get(self, id:str) -> Chat:
        chat = Chat()
        data = self.db.executeSelect("SELECT id, name, created_at, updated_at FROM chats WHERE id = ?", (id))
        for row in data:
            chat.fromJson(row)
        
        return chat

    def addUser(self, chatId:str, user:str) -> bool:
        affected = self.db.execute("INSERT INTO chat_users (chat_id, user_id) VALUES (?, ?)", (chatId, user))
        return affected > 0
    
    def removeUser(self, chatId:str, user:str) -> bool:
        affected = self.db.execute("DELETE FROM chat_users WHERE chat_id = ? AND user_id = ?", (chatId, user))
        return affected > 0

    def _getCreateTableScript(self) -> str:
        return """
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS chat_users (
    chat_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chat_id) REFERENCES chats(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    PRIMARY KEY (chat_id, user_id)
);
"""