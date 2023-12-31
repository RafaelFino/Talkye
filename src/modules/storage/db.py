import sqlite3
import json
from modules.util.logger import Logger

class DbConnection:
    def __init__(self, connStr:str) -> None:
        self._connStr = connStr
        self.db = None

    def _testConnection(self) -> bool:
        if self.db is None:
            self.db = sqlite3.connect(self._connStr, autocommit=False)
            if self.db is None:                
                Logger.error(f"database error: Connection is not established")
                return False

        return self.db.is_connected()
    
    def close(self):
        if self.db is not None:
            self.db.close()
            self.db = None

    def commit(self):
        if self.db is not None:
            self.db.commit()
    def rollback(self):       
        if self.db is not None:
            self.db.rollback()

    def execute(self, sql:str, params:tuple=None, autoCommit:bool=True) -> int:
        if not self._testConnection():
            raise Exception("Connection is not established")

        cursor = self.db.cursor()
        ret = None
        try:
            if params is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, params)

            ret = cursor.rowcount
        except Exception as e:
            Logger.error(f"database error: {e}")
            raise e
        finally:
            if autoCommit:
                self.db.commit()
            cursor.close()

        return ret

    def executeInsert(self, sql:str, params:tuple=None, autoCommit:bool=True) -> int:
        if not self._testConnection():
            raise Exception("Connection is not established")

        cursor = self.db.cursor()
        ret = -1
        try:
            if params is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, params)

            ret = cursor.lastrowid
        except Exception as e:
            Logger.error(f"database error: {e}")
            raise e
        finally:
            if autoCommit:
                self.db.commit()

            cursor.close()

        return ret

    def query(self, sql:str, params:tuple=None, autoCommit:bool=True, json_str:bool=True):    
        if not self._testConnection():
            raise Exception("Connection is not established")
        
        cursor = self.db.cursor()

        try:
            if params is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, params)            

            ret = cursor.fetchall()

            if json_str:
                return json.dumps( [dict(ix) for ix in ret] )
            else:
                return ret
            
        except Exception as e:
            Logger.error(f"database error: {e}")
            raise e
        finally:
            if autoCommit:
                self.db.commit()

            cursor.close()
