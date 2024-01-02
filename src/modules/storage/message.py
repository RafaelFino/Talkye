from modules.entities.message import Message
from modules.storage.db import DbConnection   

class MessageStorage:
    def __init__(self, db:DbConnection) -> None:
        self.db = db

    def insert(self, message:Message) -> bool:
        pass

    def getFromChat(self, chatId:str, fromId:str ="") -> list:
        pass

    def getFromUser(self, userId:str, fromId:str = "") -> list:
        pass

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