from modules.storage.db import DbConnection   
class UserStorage:
    def __init__(self, db:DbConnection) -> None:
        self.db = db