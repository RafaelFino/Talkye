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