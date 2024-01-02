from modules.entities.chat import Chat
from modules.entities.message import Message
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
    
    def update(self, chat:Chat) -> bool:
        affected = self.db.execute("UPDATE chats SET name = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?", (chat.name, chat.id))
        return affected > 0

    def get(self, chat_id:str, loadUsers:bool=False, loadMesages:bool=False) -> Chat:
        chat = Chat()
        data = self.db.executeSelect("SELECT id, name, created_at, updated_at FROM chats WHERE id = ?", (chat_id))
        for row in data:
            chat.fromJson(row)

        if loadUsers:
            users = self.db.executeSelect("SELECT user_name FROM chat_users WHERE chat_id = ?", (chat_id))
            for row in users:
                chat.users.append(row["user_name"])

        if loadMesages:
            messages = self.db.executeSelect("SELECT id, chat_id, user_name, message, created_at FROM messages WHERE chat_id = ? ORDER BY id", (chat_id))
            for row in messages:
                message = Message()
                message.fromJson(row)
                chat.messages.append(message)
            
        return chat

    def addUser(self, chat_id:str, user_name:str) -> bool:
        affected = self.db.execute("INSERT INTO chat_users (chat_id, user_name) VALUES (?, ?)", (chat_id, user_name))
        return affected > 0
    
    def removeUser(self, chat_id:str, user_name:str) -> bool:
        affected = self.db.execute("DELETE FROM chat_users WHERE chat_id = ? AND user_name = ?", (chat_id, user_name))
        return affected > 0

    def _getCreateTableScript(self) -> str:
        return """
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS chat_users (
    chat_id INTEGER NOT NULL,
    user_name INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chat_id) REFERENCES chats(id),
    FOREIGN KEY (user_name) REFERENCES users(name),
    PRIMARY KEY (chat_id, user_name)
);
"""