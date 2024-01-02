from modules.util import Logger
from modules.entities.chat import Chat
from modules.entities.message import Message
from modules.entities.user import User  
from modules.storage.chat import ChatStorage
from modules.storage.message import MessageStorage
from modules.broker import Broker
from modules.storage.db import DbConnection

class ChatServices:
    def __init__(self) -> None:
        self.broker = None  
        self.chatStorage = None
        self.messageStorage = None

    def init(self, dbConnStr:str, natsServer:str):
        self.dbConnStr = dbConnStr
        self.natsServer = natsServer

        try:
            self.dbConn = DbConnection(self.dbConnStr)
            self.chatStorage = ChatStorage(self.dbConn)
            self.messageStorage = MessageStorage(self.dbConn)
            self.broker = Broker(self.natsServer, self._onMessage)

            self.chats = self.chatStorage.getAll()
        except Exception as e:
            Logger.error(f"chat service error: {e}")
    
    def _onMessage(self, message: Message):       
        # implement web socket to send message to client
        pass
    def sendMessage(self, message: Message) -> int:
        try:
            chat = self.chatStorage.get(message.chat_id)
        except:
            raise Exception("Chat not found")

        try:
            message.id = self.messageStorage.create(message)
            self.broker.publish(str(message.chat_id), message.toJson())
        except Exception as e:  
            Logger.error(f"chat service error: {e}")
            raise e

        return message.id
        
    def getMessages(self, chat_id: str, from_id: str = "") -> list:
        if chat_id not in self.chats:
            Logger.error(f"chat service error: chat {chat_id} not found")
            return []   
        
        try:
            messages = self.messageStorage.getFromChat(chat_id, from_id)
        except Exception as e:
            Logger.error(f"chat service error: {e}")
            raise e

        return messages

    def createChat(self, chat: Chat) -> bool:        
        try:
            id = self.chatStorage.create(chat)
            chat.id = id
            self.chats[chat.id] = chat
            
        except Exception as e:
            Logger.error(f"chat service error: {e}")
            return False

        return True            

    def getChats(self) -> {}:
        return self.chats

    def getChat(self, chat_id: str, loadUsers:bool=False, loadMessages:bool=False) -> Chat:
        if chat_id not in self.chats:
            Logger.error(f"chat service error: chat {chat_id} not found")
            return None
        
        chat = self.chats[chat_id]
        
        if loadUsers or loadMessages:
            try:
                chat = self.chatStorage.get(chat_id, loadUsers, loadMessages)
            except Exception as e:
                Logger.error(f"chat service error: {e}")
                raise e        

        return chat

    def addUser(self, chat_id: str, user_name: str) -> bool:
        if chat_id not in self.chats:
            Logger.error(f"chat service error: chat {chat_id} not found")
            return None

        ret = False

        try:
            ret = self.chatStorage.addUser(chat_id, user_name)
        except Exception as e:
            Logger.error(f"chat service error: {e}")
            raise e

        return ret

    def removeUser(self, chat_id: str, user_name: str) -> bool:
        if chat_id not in self.chats:
            Logger.error(f"chat service error: chat {chat_id} not found")
            return None

        ret = False

        try:
            ret = self.chatStorage.removeUser(chat_id, user_name)
        except Exception as e:
            Logger.error(f"chat service error: {e}")
            raise e

        return ret       
