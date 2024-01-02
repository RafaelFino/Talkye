import asyncio
import nats
from nats.errors import ConnectionClosedError, TimeoutError, NoServersError
from modules.uitl.logger import Logger    

from modules.entities.message import ChatMessage
from class Borker:
    def __init__(self) -> None:        
        self.nc = None
        self.messageCallback = None
        self.subscriptions = {}
        
    def connect(self, natsServer:str, messageCallback) -> bool:
        try:
            self.nc = nats.connect(natsServer)
            self.messageCallback = messageCallback
        except ConnectionClosedError:
            Logger.error(f"broker error: Connection is not established")
        except TimeoutError:
            Logger.error(f"broker error: Timeout")
        except NoServersError:
            Logger.error(f"broker error: No servers")

        return self.nc is not None
    
    def _testConnection(self) -> bool:
        if self.nc is None:
            Logger.error(f"broker error: Connection is not established")
            return False

        return True

    def publish(self, message:ChatMessage):
        if not self._testConnection():
            raise Exception("Connection is not established")
        
        self.nc.publish(str(message.chat_id), message.toJson())

    def subscribe(self, topic: str):
        if not self._testConnection():
            raise Exception("Connection is not established")        
        
        self.sub[topic] = self.nc.subscribe(topic, cb=self.message_handler)

    async def message_handler(self, msg):
        chatMessage = ChatMessage()
        chatMessage.fromJson(msg.data.decode())        

        if self.messageCallback is not None:
            try:
                await self.messageCallback(chatMessage)
            except Exception as e:
                Logger.error(f"broker error: {e}")
        else:
            Logger.error(f"broker error: message callback is None")
            raise Exception("message callback is None")
        
        msg.ack()