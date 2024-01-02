from modules.entities.message import Message
from modules.storage.db import DbConnection   

class MessageStorage:
    def __init__(self, db:DbConnection) -> None:
        self.db = db
        self.db.execute(self._getCreateTableScript())

    def insert(self, message:Message) -> int:
        return self.db.executeInsert("INSERT INTO messages (chat_id, user_id, message) VALUES (?, ?, ?)", (message.chatId, message.userId, message.message))

    def getFromChat(self, chatId:str, fromId:str ="") -> list:
        messages = []
        data = self.db.executeSelect("SELECT id, chat_id, user_id, message, created_at FROM messages WHERE chat_id = ? AND id > ? ORDER BY id", (chatId, fromId))
        for row in data:
            message = Message()
            message.fromJson(row)
            messages.append(message)
        
        return messages

    def getFromUser(self, userId:str, fromId:str = "") -> list:
        messages = []
        data = self.db.executeSelect("SELECT id, chat_id, user_id, message, created_at FROM messages WHERE user_id = ? AND id > ? ORDER BY chat_id, id", (userId, fromId))
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
    user_id TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chat_id) REFERENCES chats(id)
);

CREATE INDEX IF EXISTS messages_index_chat_id
ON messages(chat_id);

CREATE INDEX IF EXISTS messages_index_user_id
ON messages(user_id);
"""