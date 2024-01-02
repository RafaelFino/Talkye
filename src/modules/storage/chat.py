from modules.models.chat import Chat
from modules.storage.db import DbConnection   
class ChatStorage:
    def __init__(self, db:DbConnection) -> None:
        self.db = db



    def create(self, chat:Chat) -> bool:
        pass

    def getAll(self) -> list:
        pass

    def get(self, id:str) -> Chat:
        pass

    def addUser(self, chatId:str, user:str) -> bool:
        pass

    def removeUser(self, chatId:str, user:str) -> bool:
        pass

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