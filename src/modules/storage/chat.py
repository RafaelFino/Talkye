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




