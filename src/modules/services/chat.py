from modules.entities.chat import Chat
from modules.entities.message import Message
from modules.entities.user import User  
from modules.storage.chat import ChatStorage
from modules.storage.message import MessageStorage

class ChatServices:
    def __init__(self, dbConnStr:str) -> None:
        self.dbConnStr = dbConnStr
        
    def sendMessage(self, message: str):
        pass

    def getMessages(self, chatId: str, fromId: str = "") -> list:
        pass

    def createChat(self, chat: Chat) -> bool:
        pass

    def getChats(self) -> list:
        pass

    def getChat(self, id: str) -> Chat:
        pass    

    def addUser(self, chatId: str, user: str) -> bool:
        pass    

    def removeUser(self, chatId: str, user: str) -> bool:
        pass

    def subscribe(self, chatId: str, user: str) -> bool:
        pass

    def unsubscribe(self, chatId: str, user: str) -> bool:
        pass    

