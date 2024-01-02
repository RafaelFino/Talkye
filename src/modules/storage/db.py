import sqlite3

class DbConnection:
    def __init__(self, connStr:str) -> None:
        self._connStr = connStr

    def connect(self):
        self.db = sqlite3.connect(self._connStr, autocommit=False)

    def _testConnection(self) -> bool:
        if self.db is None:
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

    def execute(self, sql:str, params:tuple=None, autoCommit:bool=True):
        if not self._testConnection():
            raise Exception("Connection is not established")

        cursor = self.db.cursor()
        ret = None
        try:
            if params is None:
                ret = cursor.execute(sql)
            else:
                ret = cursor.execute(sql, params)

            return ret                
        except Exception as e:
            raise e
        finally:
            if autoCommit:
                self.db.commit()
            cursor.close()

        

    def query(self, sql:str, params:tuple=None, autoCommit:bool=True) -> list:    
        if not self._testConnection():
            raise Exception("Connection is not established")

        cursor = self.db.cursor()
        try:
            if params is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, params)

            return cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            if autoCommit:
                self.db.commit()

            cursor.close()

    def queryOne(self, sql:str, params:tuple=None, autoCommit:bool=True) -> list:    
        if not self._testConnection():
            raise Exception("Connection is not established")

        cursor = self.db.cursor()
        try:
            if params is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, params)

            return cursor.fetchone()
        except Exception as e:
            raise e
        finally:
            if autoCommit:
                self.db.commit()

            cursor.close()    