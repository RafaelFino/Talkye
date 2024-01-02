from modules.entities.message import Message
from modules.storage.db import DbConnection   

class MessageStorage:
    def __init__(self, db:DbConnection) -> None:
        self.db = db
        self.db.execute(self._getCreateTableScript())

    def insert(self, message:Message) -> int:
        return self.db.executeInsert("INSERT INTO messages (chat_id, user_name, message) VALUES (?, ?, ?)", (message.chatId, message.user, message.message))

    def getFromChat(self, chat_id:str, from_id:str ="") -> list:
        messages = []
        data = self.db.executeSelect("SELECT id, chat_id, user_name, message, created_at FROM messages WHERE chat_id = ? AND id > ? ORDER BY id", (chat_id, from_id))
        for row in data:
            message = Message()
            message.fromJson(row)
            messages.append(message)
        
        return messages

    def getFromUser(self, user_name:str, fromId:str = "") -> list:
        messages = []
        data = self.db.executeSelect("SELECT id, chat_id, user_name, message, created_at FROM messages WHERE user_name = ? AND id > ? ORDER BY chat_id, id", (user_name, fromId))
        for row in data:
            message = Message()
            message.fromJson(row)
            messages.append(message)
        
        return messages

    def _createTableScript(self) -> str:
        return """
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id INTEGER NOT NULL,
    user_name TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chat_id) REFERENCES chats(id),
    FOREIGN KEY (user_name) REFERENCES users(name)
);

CREATE INDEX IF EXISTS messages_index_chat_id
ON messages(chat_id);

CREATE INDEX IF EXISTS messages_index_user_name
ON messages(user_name);
"""